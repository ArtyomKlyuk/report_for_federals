from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import openpyxl
import time


from Auths import gmail, password


class ReportFederals:
    def __init__(self, source):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=self.options)
        self.source = source
        self.wb = openpyxl.load_workbook(self.source)
        self.report_sheet = self.wb.get_sheet_by_name(self.wb.get_sheet_names()[0])
        self.region_id = self.wb.get_sheet_by_name(self.wb.get_sheet_names()[1])

    def auth_pro_culture(self):
        driver = self.driver

        driver.get('https://pro.culture.ru/new/auth/login')
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "ant-input").send_keys(gmail)
        time.sleep(1)
        driver.find_elements(By.CLASS_NAME, 'ant-input')[1].send_keys(password)
        WebDriverWait(driver, timeout=30).until(lambda x: driver.find_element(By.CSS_SELECTOR,
                                                                              ".ant-btn.ant-btn-primary")).click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".main-form_organization-link").click()
        time.sleep(3)

    def get_ids(self, region_id):

        regions = dict()
        for i in range(2, 87):
            regions[region_id[f"A{i}"].value] = region_id[f"B{i}"].value
        return regions

    def click_button_events(self, url):
        driver = self.driver
        x = 0
        while x == 0:
            try:
                button = WebDriverWait(driver, timeout=70).until(lambda find_button: driver.find_element(By.XPATH,
                                                                                                         "/html/body/div[1]/div["
                                                                                                         "1]/div[3]/div["
                                                                                                         "1]/div/div/div/div["
                                                                                                         "2]/div/div/div["
                                                                                                         "1]/button"))
                button.click()
                return 1
            except:
                driver.get(url)

    def click_button(self):
        driver = self.driver

        try:
            button = WebDriverWait(driver, timeout=60).until(lambda find_button: driver.find_element(By.XPATH,
                                                                                                     "/html/body/div[1]/div["
                                                                                                     "1]/div[3]/div["
                                                                                                     "1]/div/div/div/div["
                                                                                                     "2]/div/div/div["
                                                                                                     "1]/button"))
            button.click()
            return 1
        except:
            return 0

    # def check_amount(self, text, type):
    #     if ''.join(text.strip(
    #
    #             f"{type} (количество: ").strip(")").split()) != '0' and type in text:
    #         return True
    #     return False

    def get_amount(self, type: str):
        driver = self.driver
        flag = "количество"
        if type == "Счетчики":

            if WebDriverWait(driver, timeout=60).until(lambda check_amount:
                                                       flag in driver.find_element(By.XPATH,
                                                                                   "/html/body/div[1]/div[1]/div[3]/div["
                                                                                   "1]/div "
                                                                                   "/div/div/div[1]/div/div[2]/div/div["
                                                                                   "1]/span").text and ''.join(
                                                           driver.find_element(
                                                               By.XPATH, "/html/body/div[1]/div[1]/div[3]/div["
                                                                         "1]/div "
                                                                         "/div/div/div[1]/div/div[2]/div/div["
                                                                         "1]/span").text.strip(
                                                               f"{type} ({flag}: ").strip(")").split()) != '0'):

                amounts = ''.join(driver.find_element(By.XPATH,
                                                      "/html/body/div[1]/div[1]/div[3]/div["
                                                      "1]/div "
                                                      "/div/div/div[1]/div/div[2]/div/div["
                                                      "1]/span").text.strip(

                    f"{type} ({flag}: ").strip(")").split())
            else:
                amounts = "Отсутсвует"
        else:
            if WebDriverWait(driver, timeout=60).until(lambda check_amount:
                                                       flag in driver.find_element(By.XPATH,
                                                                                   "/html/body/div[1]/div[1]/div[3]/div["
                                                                                   "1]/div "
                                                                                   "/div/div/div[1]/div/div[2]/div/div["
                                                                                   "1]/span").text):

                amounts = ''.join(driver.find_element(By.XPATH,
                                                      "/html/body/div[1]/div[1]/div[3]/div["
                                                      "1]/div "
                                                      "/div/div/div[1]/div/div[2]/div/div["
                                                      "1]/span").text.strip(

                    f"{type} ({flag}: ").strip(")").split())
            else:
                amounts = "Отсутсвует"

        return amounts

    def get_counters_amount(self):
        flag = 'количество'

    def get_report(self, links: dict):
        driver = self.driver
        report_sheet = self.report_sheet
        region_ids = self.get_ids(self.region_id)
        # fields_for_check = ['B', 'C', 'E', 'G']  # 'D' - события
        fields_for_check = ['D']  # - события

        NUMBER_FOR_FIELDS = '1'
        events = ['событий', 'События']
        orgs = ['учреждений', 'Учреждения']
        counters = 'Счетчики'
        for i in range(23, 102):
            subject = report_sheet[f"A{i}"].value
            reg_id = region_ids.get(subject)
            if reg_id is None:
                continue
            reg_id = str(reg_id)
            for letter in fields_for_check:
                field = report_sheet[f"{letter + NUMBER_FOR_FIELDS}"].value
                link = links[field]
                if len(link) == 1:
                    url = link[0] + reg_id
                else:
                    url = link[0] + reg_id + link[1]
                driver.get(url)
                if orgs[0] in field:
                    self.click_button()
                    amount = self.get_amount(orgs[1])

                elif events[0] in field:
                    if self.click_button_events(url) == 1:
                        amount = self.get_amount(events[1])
                    else:
                        amount = 0

                else:
                    amount = self.get_amount(counters)
                report_sheet[f"{letter + str(i)}"] = int(amount)
                print(f"{field} в {subject} = {amount}")
            if i % 10 == 0:
                self.wb.save(self.source)
        self.wb.save(self.source)
        driver.close()
        driver.quit()
