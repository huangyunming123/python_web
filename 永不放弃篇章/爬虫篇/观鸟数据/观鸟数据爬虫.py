import execjs
import requests

for i in range(1, 5):
    with open('观鸟数据.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
        js = execjs.compile(js_code)
        # options = {
        #     "data": 'page=2&limit=20'
        # }
        # params = options['data']
        # print(params)
        req = '{"limit":"20","page":"%s"}'
        params = req % i
        res = js.call('getData', params)
        print(res)
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://www.birdreport.cn",
            "Pragma": "no-cache",
            "Referer": "https://www.birdreport.cn/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
            "requestId": res['requestId'],
            "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sign": res['sign'],
            "timestamp": str(res['timestamp'])
        }
        url = "https://api.birdreport.cn/front/activity/search"
        data = res['data']
        response = requests.post(url, headers=headers, data=data)
        print(response.text)
        print("---------------")
        print(response.json()["data"])
        res = js.call('parseData', response.json())
        print(res)

# {'timestamp': 1752053459000, 'requestId': 'f2a20541a45eba4c26a89b6a2348f4b3', 'sign': '3f49760b90275857befed31efaad02e4', 'data': 'bs5a9gfUuD3bvqsSnYYXq6FBM/vTH5VzkFxjiavwxl5GOszBetO3hlyH55jBiJGXOukDCzMjoRHwqug+JHeV8CKuiUq8OIO6yAGapHTqCa2qVTZy/SF68u8NaSJSl+TzP+Mz6NRq9pgmQXRDhnT90m66l9ke1GmtVJCt4nw+cVU='}
