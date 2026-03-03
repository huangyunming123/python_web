import json

import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://mashangpa.com/problem-detail/1/",
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
    "Hm_lpvt_0d2227abf9548feda3b9cb6fddee26c0": "1750150629"
}
url = "https://mashangpa.com/api/problem-detail/1/data/"

res = 0
for i in range(1, 21):
    params = {
        "page": i
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    arr = json.loads(response.text).get('current_array')
    for i in arr:
        res += i
print(res)