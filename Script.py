import os
import time
from openpyxl import Workbook
import requests
from fake_useragent import UserAgent



ua = UserAgent()
url = os.environ.get("URL")
password = os.environ.get('Pass')
data_list = []
workbook = Workbook()
worksheet = workbook.active

headers = {'User-Agent': ua.chrome}
resp = requests.get(url, headers=headers, verify=False, timeout=5)
data = resp.json()
sid = data['sid']


# Validations & Get SID
if resp.status_code == 200:
    data = resp.json()
    sid = data['sid']
    print(f"Your sid is {sid}")
else:
    print('No connection to server')


def find_dict(lst, key, value):
    return [d for d in lst if key in d and d[key] == value]


while True:
    cheks = f"https://10.79.3.10:8080/pos_events?password={password}"
    chek = requests.get(cheks, headers=headers, verify=False, timeout=5)
    datacheks = chek.json()
    chek.raise_for_status()
    if chek.status_code == 200:
        print("All is OK!")


    target_key = 'type'
    target_value = 'POSNG_RECEIPT_FINAL_RESULT'  #  type is always == "POSNG_RECEIPT_FINAL_RESULT


    result = find_dict(datacheks, target_key, target_value)
    print(result)
    for item in result:
        if item['value'] not in data_list:
            worksheet.append([item['key'], item['value']])
            data_list.append(item['value'])

    workbook.save('output.xlsx')

    time.sleep(1)


