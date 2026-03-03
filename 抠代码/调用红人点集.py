import json

import execjs
import requests


class HRDJ():
    def __init__(self):
        self.url = "https://ucp.hrdjyun.com:60359/api/dy"
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": "https://www.hh1024.com",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\""
        }
        self.data = {
            "param": "{\"no\":\"dy0002\",\"data\":{\"days\":1,\"rankType\":5,\"liveDay\":\"2024-06-28\"}}",
            "sign": "a37a5ae544d8cc5d548e406aeb064e45ee76895793a70ae0df7c93ac1bf6e97a",
            "tenant": "1",
            "timestamp": 1719816494294,
            "token": "FrWKAvpXdX8lx5RlQgCZIWnjg5f6kCbj"
        }
        self.js = execjs.compile(open("红人点集.js", encoding='utf-8').read())

    def request_data(self):
        param_ = self.data['param']
        sign = self.js.call('get_sign', param_)
        self.data['sign'] = sign['sign']
        self.data['timestamp'] = sign['time_Data']
        res = requests.post(self.url, headers=self.headers, json=self.data)
        print(res.text)

    def main(self):
        self.request_data()


if __name__ == '__main__':
    req = HRDJ()
    req.main()
# js 转换 json 跟 python 转换 会存在差异 --> python 会多一个空格 大致加密的时候不一致 所以 转换的时候需要在同一语言进行
