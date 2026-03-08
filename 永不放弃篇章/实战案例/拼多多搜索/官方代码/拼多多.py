import time
import requests
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

headers = {
    "Accept": "application/json, text/javascript",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Origin": "https://pinduoduo.com",
    "Pragma": "no-cache",
    "Referer": "https://pinduoduo.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://apiv2.pinduoduo.com/api/gindex/tf/query_tf_goods_info"
anti_content = execjs.compile(open('./5.main.js', 'r', encoding='utf-8').read()).call('get_anti_content')
print(anti_content)
params = {
    "tf_id": "TFRQ0v00000Y_13396",
    "page": 1,
    "size": "39",
    "anti_content": anti_content
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)
