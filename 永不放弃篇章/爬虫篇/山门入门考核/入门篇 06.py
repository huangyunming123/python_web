import json

import execjs

import requests

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://mashangpa.com/problem-detail/6/",
    "s": "3d43b967eb62813aaedad234b641bf53",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "tt": "1750226267781",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}
cookies = {
    "sessionid": "53ntpl1p4si5gv1itvpfs6p8tnqr1hsy",
    "Hm_lvt_0d2227abf9548feda3b9cb6fddee26c0": "1750073299,1750150177",
    "HMACCOUNT": "5BAC04C46223486D",
    "Hm_lpvt_0d2227abf9548feda3b9cb6fddee26c0": "1750222052"
}
url = "https://mashangpa.com/api/problem-detail/6/data/"
# params = {
#     "page": "5"
# }
# response = requests.get(url, headers=headers, cookies=cookies, params=params)
#
# print(response.text)
# print(response.json())

result = 0
for i in range(1, 21):
    with open('入门篇06辅助.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
        js = execjs.compile(js_code)
        params = {
            "page": i
        }
        newHeader = js.call('s')
        print(newHeader)
        # {s: '20aceee689680d12e07cd82578db6fda', tt: 1750228936093}
        headers['s'] = newHeader['s']
        headers['tt'] = str(newHeader['tt'])
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        res = js.call('xxxxoooo',  response.json()['t'])
        arr = json.loads(res).get('current_array')
        print(arr)
        for j in arr:
            result += j
print(result)
