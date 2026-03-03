# 如果报错编码问题  需要在最开始引入下面文件
# import subprocess
# from functools import partial
# subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")


import execjs
import requests


for i in range(0, 1):
    headers = {
        "Accept": "text/plain, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://www.endata.com.cn",
        "Pragma": "no-cache",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\""
    }
    url = "https://www.endata.com.cn/API/GetData.ashx"
    data = {
        "startTime": "2024-04-03",
        "MethodName": "BoxOffice_GetMonthTime"
    }
    with open('艺恩解密.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
        js = execjs.compile(js_code)
        response = requests.post(url, headers=headers, data=data)
        print(type (response.text))
        res = js.call('getData', response.text)
        print(res)
