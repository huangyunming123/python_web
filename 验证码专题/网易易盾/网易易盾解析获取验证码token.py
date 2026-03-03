import json

import requests
import execjs #调用js 用的

js = execjs.compile(open('带数组的解密函数包含web打包.js', 'r', encoding='utf-8').read())
cb = js.call('window.getCB')
#  先从解释器第一个开始找解密的位置

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://dun.163.com/",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Google Chrome\";v=\"144\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
cookies = {
    "_ga": "GA.1.280e710f21d02.f089948344c46b61746a",
    "_ntes_nnid": "36279c98292a5d4bc9e9e130c7a75d26,1769409086559",
    "_ntes_nuid": "36279c98292a5d4bc9e9e130c7a75d26",
    "Hm_lvt_4671c5d502135636b837050ec6d716ce": "1770715817",
    "HMACCOUNT": "F9080EB0E616319B",
    "__root_domain_v": ".163.com",
    "_qddaz": "QD.952670715817376",
    "Hm_lpvt_4671c5d502135636b837050ec6d716ce": "1770780428"
}
url = "https://c.dun.163.com/api/v3/get"
params = {
    "referer": "https://dun.163.com/trial/jigsaw",
    "zoneId": "CN31",
    "dt": "a6Sw2cmg5vNBF0QFBFKCsHF8/A6heCP/",
    "irToken": "+Bmq+Fp5S7VBNwRVFVLH8SHJn7MZ9Sdu",
    "id": "07e2387ab53a4d6f930b8d9a9be71bdf",
    "fp": "/7lu4TLk7WPvrAfBUQZJ3OXSNvXrnRErfk7fX8WyurN\\Dj4SKtQIMhftWZRGOwEqXrjinSPboBst6X7foQQ/jJKYqgbo/oE+bc33mWk4WuA+m3qbZIAs2qra6IZHvxwgReEUAV8+X9ht5x8JfQnhn88eLQxPJV\\Cgc1lDddWy+gMz0yJ:1770781155428",
    "https": "true",
    "type": "2",
    "version": "2.28.5",
    "dpr": "2",
    "dev": "1",
    "cb": cb,
    "ipv6": "false",
    "runEnv": "10",
    "group": "",
    "scene": "",
    "lang": "zh-CN",
    "sdkVersion": "",
    "loadVersion": "2.5.4",
    "iv": "4",
    "user": "",
    "width": "320",
    "audio": "false",
    "sizeType": "10",
    "smsVersion": "v3",
    "token": "9b8563f6d2be4119b3946dcb44c58fb8",
    "callback": "__JSONP_ih8syib_2"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
# print(response.text)
#  因为不是正常json  所以要处理一下返回值
res = response.text.split('ib_2(')[1].split(')')[0]
data = json.loads(res)['data']

bg = data['bg'][0]
token = data['token']
front = data['front'][0]
print(bg,'\n', token,'\n', front)


import requests

res = requests.get(bg)
open('bg.png', 'wb').write(res.content)

res = requests.get(front)
open('full.png', 'wb').write(res.content)

import ddddocr

det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)

with open('bg.png', 'rb') as f:
    background_bytes = f.read()

with open('full.png', 'rb') as f:
    target_bytes = f.read()

res = det.slide_match(target_bytes, background_bytes)

print(res)
