import time

import requests
import pandas as pd

check_deployed = False
while not check_deployed:
    print("running",time.strftime("%H:%M:%S", time.localtime()))
    df = pd.read_html(
        "https://119app1.fdkc.gov.tw/tyfdapp/webControl?page=Tfqve7Vz8sjTOllavM2iqQ==&f=IC2SZJqIMDj1EwKMezrgvw=="
        , encoding='utf-8', header=0)[0]
    if df.at[0, df.columns[5]] == '成功分隊':
        check_deployed = True
        deployed_time = df.at[0, df.columns[1]]
        case_class = df.at[0, df.columns[2]]
        case_category = df.at[0, df.columns[3]]
        address = df.at[0, df.columns[4]]
        squad = df.at[0, df.columns[5]]

        headers = {
            "Authorization": "Bearer " + "I4rSzp6xoZf1B9Cj3ZC3c06gsujh5VjO2nK5rdT2lmc",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        Gmap = "https://maps.google.com.tw/maps?f=q&hl=zh-TW&geocode=&q=" + df.at[0, df.columns[4]]
        params = {"message": df.at[0, df.columns[5]] + " 派遣令" + '\n' + df.at[0, df.columns[2]] + "-" + df.at[
            0, df.columns[3]] + '\n' + Gmap}

        print(params)
        r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=params)

        print(r.status_code)  # 200
        print("notice deployed")

    time.sleep(1)

print("Process Closed")