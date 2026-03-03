import execjs
import requests
import json

for i in range(1,3):
    with open('数位观察解密.js', 'r', encoding='utf-8') as f:
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": "https://www.swguancha.com",
            "Pragma": "no-cache",
            "Referer": "https://www.swguancha.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
            "deviceType": "1",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\""
        }
        url = "https://app.swguancha.com/client/v1/article/client/page"
        data = {
            "queryType": 3,
            "current": i,
            "size": 20
        }
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(url, headers=headers, data=data)
        js_code = f.read()
        js = execjs.compile(js_code)
        call = js.call('ff', response.text)
        t = {
            "data":response.text
        }
        call2 = js.call('getData', t)

        print(call2)
