from xmlrpc.client import DateTime

import execjs
import requests
import json

with open('山西政府v4.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
    js = execjs.compile(js_code)

    res = js.call('getData',date)
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "form-token": "ea0b035b15bc442872aa9f6e9cb4f90f",
        "nsssjss": "SYep+EjIGDW0v/i7NADLswszP7LYZd3KhMynWNihI71dMTinCS3+GYGoUnxsDX+nHf2B9wS5NAbu+vlVGjAhm+uzMEcQ3edvcV1ct5DVOMCenV9Xn4J4yGzYTSrSMApdZekwCbwAMKDbCd4ODMEKj679YqReO2hQbUkHBY75b30=",
        "origin": "https://shanxisheng-zfcgdzmcgov.cn",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://shanxisheng-zfcgdzmcgov.cn/gpmall-main-web/basic/sxNotice",
        "regioncode": "140001000",
        "regionguid": "140001",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sign": "5a4c2689279c0509a890bef42abeb43e",
        "sitecode": "sxzfcg",
        "siteguid": "6883226032309207040",
        "time": "1755240770002",
        "timestamp": "1755240769998",
        "url": "/gateway/gpmall-bpoc/notice/v1/ignore/getNoticeList",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        "webapp": "1"
    }
    cookies = {
        "webapp": "1",
        "siteCode": "sxzfcg",
        "siteGuid": "6883226032309207040",
        "regioncode": "140001000",
        "regionguid": "140001",
        "theme": "default",
        "regionpguid": "232",
        "rootregionguid": "232",
        "isOpenArea": "true",
        "platform": "0",
        "regionname": "%E7%9C%81%E6%9C%AC%E7%BA%A7"
    }
    url = "https://shanxisheng-zfcgdzmcgov.cn/gateway/gpmall-bpoc/notice/v1/ignore/getNoticeList"
    data = {
        "regionGuid": "232",
        "regionCode": "140000000",
        "agreementTypeCode": "",
        "pageSize": 10,
        "pageNum": 1,
        "noticeType": "0"
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, data=data)

    print(response.text)
    print(response)