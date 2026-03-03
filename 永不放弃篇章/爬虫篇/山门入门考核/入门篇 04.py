import json
import time

import execjs
import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://mashangpa.com/problem-detail/4/",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}
cookies = {
    "sessionid": "53ntpl1p4si5gv1itvpfs6p8tnqr1hsy",
    "Hm_lvt_0d2227abf9548feda3b9cb6fddee26c0": "1750073299,1750150177",
    "HMACCOUNT": "5BAC04C46223486D",
    "Hm_lpvt_0d2227abf9548feda3b9cb6fddee26c0": "1750213803"
}
url = "https://mashangpa.com/api/problem-detail/4/data/"
params = {
    "page": "5",
    "sign": "20fb91c0987631a0ae4dfe8450897b2f",
    "_ts": "1750213813833"
}
# response = requests.get(url, headers=headers, cookies=cookies, params=params)
#
# print(response.json())
# print(response)


result = 0
for i in range(1, 21):
    with open('入门篇04辅助.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
        js = execjs.compile(js_code)
        timeInt = str(int(time.time() * 1000))
        key = 'tuling' + timeInt + str(i)
        res = js.call('getToken',key)
        params = {
            "page": i,
            "sign": res,
            "_ts": timeInt
        }
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        arr = response.json().get('current_array')
        for j in arr:
            result += j
print(result)
