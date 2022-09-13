import requests
import re
import time
from bs4 import BeautifulSoup

if __name__ == '__main__':
    response = requests.get("https://119app1.fdkc.gov.tw/tyfdapp/webControl?page=Tfqve7Vz8sjTOllavM2iqQ==&f=IC2SZJqIMDj1EwKMezrgvw==")

    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("tr", class_="table_tr1")
    squad = table.find("td", string=re.compile("分隊$")).get_text()
    print(squad)

    if squad != "None":
        address = table.find("td", string=re.compile(".高雄市")).get_text().strip()
        case_class = table.find("td", string=re.compile('緊急救護|其他|火')).get_text()
        case_category = table.find("td", string=re.compile('急病|車禍|路倒|創傷|其他')).get_text()
        print(address)
        print(case_class)
        print(case_category)
        headers = {
            "Authorization": "Bearer " + "I4rSzp6xoZf1B9Cj3ZC3c06gsujh5VjO2nK5rdT2lmc",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        Gmap = "https://maps.google.com.tw/maps?f=q&hl=zh-TW&geocode=&q=" + address
        params = {"message":  squad +"派遣令" + '\n' + case_class + "-" + case_category + '\n' + Gmap}


#        print(params)
#        r = requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params)
#        print(r.status_code)  # 200
