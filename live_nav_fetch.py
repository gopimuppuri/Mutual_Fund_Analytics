import requests
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

funds = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, code in funds.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data['data'])

    filename = f"data/raw/{fund_name}.csv"

    df.to_csv(filename, index=False)

    print(f"{fund_name} downloaded successfully")