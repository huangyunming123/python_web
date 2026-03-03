import requests
import json


headers = {
    "Accept": "application/json",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://fuwu.nhsa.gov.cn",
    "Referer": "https://fuwu.nhsa.gov.cn/nationalHallSt/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "X-Tingyun": "c=B|4Nl_NnGbjwY;x=2c1349acbc2a44b9",
    "channel": "web",
    "contentType": "application/x-www-form-urlencoded",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "x-tif-nonce": "K5pFxDUY",
    "x-tif-paasid": "undefined",
    # "x-tif-signature": "d41bebeade3e40b84ee7387b7061bbdff51bbcaca3d523674a7df30194333753",
    "x-tif-timestamp": "1724814356"
}
cookies = {
    "amap_local": "110000",
    "gb_nthl_sessionId": "aa8c120a058b4d45a2219cb35a9d987a",
    "https_waf_cookie": "6b9956d0-b200-443f73edd1370d6d86211197196ee3218950",
    "yb_header_active": "-1"
}
url = "https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/CommQuery/queryFixedHospital"
data = {
    "data": {
        "data": {
            "encData": "3DFBCA4667B978F639BB23B95DCE4CC74CE34C33DC32F1068E9E23CA546C9EA87C9AEB18BAC9645BDA8D9C02BE7640B09F9EDFA86D993D31D43BF8F311A6B49246A733513B9D7FA150A1097A3B0DF19D23AE57A579165AFFE7C8E189FF7C2FE98F18DA6981D0598239780FA7C358D03DDCA72DB9D7E46A1FC083358BDB8F72C20602F95D92716984A66B8ADBBEC944436812D63DF0F07F2178EBA1DD03B373F0A97A9D6E94EDAD43A0A62C75C728481F"
        },
        "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
        "version": "1.0.0",
        "encType": "SM4",
        "signType": "SM2",
        "timestamp": 1724814356,
        "signData": "4xFSc3H4O1CwNUCn5kZAQW6wLcul9WxDc/9VwwCbsf00zfzI/rK6vcL0tRaoio3xqPr62RIiLeMcN+UY0d4PoA=="
    }
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response.json())