import os
import time
import json
import hashlib
from curl_cffi import requests

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://search.jd.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://search.jd.com/Search?keyword=%E7%94%B5%E8%84%91&enc=utf-8&pvid=a128f88d0b0b440993eaf7073983012f",
    "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "x-referer-page": "https://search.jd.com/Search",
    "x-rp-client": "h5_1.0.0"
}
cookies = {}


def sha256_hash(data):
    hash_obj = hashlib.sha256(data.encode('utf-8'))
    return hash_obj.hexdigest()


url = "https://api.m.jd.com/api"

jd_params = {
    "enc": "utf-8",
    "pvid": "ecd79c13d7dd458ab8293861ceb70f6a",
    "area": "1_72_55653_0",
    "page": 1,
    "new_interval": True,
    "s": 49
}

paramsH5sign = {
    'appid': 'search-pc-java',
    'functionId': "pc_search_searchWare",
    'client': 'pc',
    'clientVersion': '1.0.0',
    't': str(int(time.time() * 1000)),
    'body': sha256_hash(json.dumps(jd_params))
}

response = requests.post("localhost:5000/api/data", json={"params": paramsH5sign})

h5st_info = response.json()["result"]
print('h5st_info ->', h5st_info)
params = {
    "appid": "search-pc-java",
    "t": [
        str(int(time.time() * 1000))
    ],
    "client": "pc",
    "clientVersion": "1.0.0",
    "uuid": "1745841960334352365307",
    "keyword": "电脑",
    "functionId": "pc_search_getShopAndWare",
    "body": jd_params,  # 接口请求的body为明文
    "x-api-eid-token": "jdd03QJJ7DOUYP7T5O2IKSRFQANXZJYHALCU3ECRYXYVSULUXN7DODVWDAGUVYK2WLOTISQ3XQ7U7G5PP57CC2QFRLQFA5AAAAAMYYUR7TVIAAAAACORWVTOFTVSAUQX",
    "h5st": h5st_info["h5st"]
}
response = requests.get(url, headers=headers, cookies=cookies, params=params, impersonate='chrome101')

print(response.text)
print(response)
