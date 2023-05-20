import requests
from fake_useragent import UserAgent
import os


ua = UserAgent()

url = os.environ.get("URL")
headers = {'User-Agent': ua.chrome}
resp = requests.get(url, headers=headers, verify=False, timeout=5)


# Validations & Get SID
if resp.status_code == 200:
    data = resp.json()
    sid = data['sid']
    print(f"Your sid is {sid}")
else:
    print('No connection to server')
