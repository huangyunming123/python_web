import time
import pywasm
import requests

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://spa14.scrape.center/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
# https://spa14.scrape.center/js/Wasm.wasm
url = 'https://spa14.scrape.center/api/movie/'
runtime = pywasm.load("./TestMethod.wasm")

for page in range(1, 2):
    offset = page * 10
    sign = runtime.exec('encrypt', [offset, int(time.time())])
    print(sign)
    # params = {
    #     "limit": "10",
    #     "offset": "10",
    #     "sign": sign
    # }

    # response = requests.get(url, headers=headers, params=params)
    #
    # print(response.json())
