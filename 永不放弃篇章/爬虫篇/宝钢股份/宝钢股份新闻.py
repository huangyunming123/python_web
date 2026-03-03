import execjs
import requests
import json

for i in range(0, 10):
    with open('获取加密信息.js', 'r', encoding='utf-8') as f:
        data = {
            "pageNo": i,
            "pageSize": 12,
            "condition": {
                "nodeId": 436
            }
        }
        # res = requests.post(url = 'http://localhost:3000/post', json=data)
        # getHeader = res.json().get('headers')
        print('--------------------')
        js_code = f.read()
        js = execjs.compile(js_code)
        res = js.call('getHeader',data)
        getHeader = res.get('headers')
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Md5":getHeader["Content-Md5"],
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": "https://www.baosteel.com",
            "Pragma": "no-cache",
            "Referer": "https://www.baosteel.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "x-date": str(getHeader["x-date"]),
            "x-nonce": getHeader["x-nonce"],
            "x-signature": getHeader["x-signature"],
            "x-user": getHeader["x-user"]
        }
        url = "https://cmsauth.baowugroup.com/v1/web/api/content/list"
        params = {
            "domainId": "12"
        }
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(url, headers=headers, params=params, data=data)
        # print(response.text)
        print(response.json())
