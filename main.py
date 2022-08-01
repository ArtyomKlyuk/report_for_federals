from core import ReportFederals

LINKS = {2: {
    'Зарегистр. учреждений': ["https://pro.culture.ru/new/subordinate/organizations?status=accepted&subordinations=",
                              "&createDateStart=01.04.2000&createDateEnd=30.06.2022"],
    'Активных учреждений': ["https://pro.culture.ru/new/subordinate/organizations?status=accepted&subordinations=",
                            "&createDateStart=01.04.2000&createDateEnd=30.06.2022&activeUsers=true"],
    'Добавлено событий всего': [
        "https://pro.culture.ru/new/subordinate/events?createDateStart=01.04.2022&createDateEnd=30.06.2022"
        "&subordinations="],
    'Онлайн-событий': ["https://pro.culture.ru/new/subordinate/events?tags=731&subordinations=",
                       "&createDateStart=01.04.2022&createDateEnd=30.06.2022"],
    'Счетчиков на конец квартала': ["https://pro.culture.ru/new/pixels?subordinations=",
                                    "&createDateStart=01.06.2000&createDateEnd=30.06.2022"]
}, 1: {
    'Зарегистр. учреждений': ["https://pro.culture.ru/new/subordinate/organizations?status=accepted&subordinations=",
                              "&createDateStart=01.04.2000&createDateEnd=31.03.2022"],
    'Активных учреждений': ["https://pro.culture.ru/new/subordinate/organizations?status=accepted&subordinations=",
                            "&createDateStart=01.04.2000&createDateEnd=31.03.2022&activeUsers=true"],
    'Добавлено событий всего': [
        "https://pro.culture.ru/new/subordinate/events?createDateStart=01.01.2022&createDateEnd=31.03.2022"
        "&subordinations="],
    'Онлайн-событий': ["https://pro.culture.ru/new/subordinate/events?tags=731&subordinations=",
                       "&createDateStart=01.01.2022&createDateEnd=31.03.2022"],
    'Счетчиков на конец квартала': ["https://pro.culture.ru/new/pixels?subordinations=",
                                    "&createDateStart=01.06.2000&createDateEnd=31.03.2022"]}}
addresses = {
    1:  r"D:\Codes\report_for_federals\report 1 кв.xlsx",
    2:  r"D:\Codes\report_for_federals\report 2 кв.xlsx"
}
# rep1 = ReportFederals(addresses[1])
# rep1.auth_pro_culture()
# rep1.get_report(LINKS[1])
rep2 = ReportFederals(addresses[2])
rep2.auth_pro_culture()
rep2.get_report(LINKS[2])