import execjs
import requests

for i in range(0,2):
    with open('建筑市场解密.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
        js = execjs.compile(js_code)
        params = {
            "pg": i,
            "pgsz": "15",
            "total": "0"
        }

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://jzsc.mohurd.gov.cn/data/company",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
            "accessToken;": "",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "timeout": "30000",
            "v": "231012"
        }
        cookies = {
            "Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c": "1750905629",
            "Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c": "1750905629",
            "HMACCOUNT": "5BAC04C46223486D"
        }
        url = "https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list"
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        res = js.call('b', response.text)
        print(res)