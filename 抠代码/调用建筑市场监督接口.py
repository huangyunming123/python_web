import execjs
import requests

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Referer": "https://jzsc.mohurd.gov.cn/data/company",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "accessToken;": "",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "timeout": "30000",
    "v": "231012"
}
cookies = {
    "Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c": "1721290221",
    "Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c": "1721290221",
    "HMACCOUNT": "A46F6E1800558626"
}
url = "https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list"
params = {
    "pg": "1",
    "pgsz": "15",
    "total": "450"
}
for i in range(1, 10):
    params = {
        "pg": i,
        "pgsz": "15",
        "total": "0"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    print(i)
    with open("./建筑市场监督.js")  as f:
        js_code = f.read()

    js = execjs.compile(js_code)

    response = js.call('getData', response.text)

    print(response)

    # py 调用js的时候可能会报错 可能是编码问题

