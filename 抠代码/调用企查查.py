import execjs
import requests
import json


class Qcc():
    def __init__(self):
        self.url = "https://www.qcc.com/api/search/searchMulti"
        self.headers = {
            "3501dec9e3ec7404295c": "04c57fa43c54f5a1ffe29cba1eb0c5824905c3699914274593882bb3e357d07b965cdf4ddf72b4a8c6600d17ede4c1667370de7b30ba3d119b68585dc43ee3b2",
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9",
            "content-type": "application/json",
            "origin": "https://www.qcc.com",
            "priority": "u=1, i",
            "referer": "https://www.qcc.com/web/search?key=%E5%B0%8F%E7%B1%B3&p=2",
            "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "x-pid": "7743ba6db63e7eaef0f934f33e1f6f26",
            "x-requested-with": "XMLHttpRequest"
        }
        self.cookies = {
            "qcc_did": "7039ac87-a836-4d45-89a1-90e1df509ccf",
            "UM_distinctid": "18f22e2e4cd1d3-0fb05b5a21aa2b-1b525637-1fa400-18f22e2e4ce977",
            "QCCSESSID": "d06e14229c4cca9a4d883961e3",
            "acw_tc": "2f624a6417204208360535675e5b394889d563af737dda3014f2fc090d9ff9",
            "tfstk": "fZ9Z6dZRQtYBp4Rc8w6VzMr2DO6OQT3S3K_fmnxcfNbgCRaDTnTvCs0OCK8eqUoAhO9s3IW9dCwf5VB2mU6qP4MSFhKOBt0SPcIjmQWcmx_moD3Q5tBmP21wEQndHU6FU3G2xDSf0lqMos43KwIgotbGiyVhqwbcntYc-kjfjPb0IGV3xUtBjn2FV1mu7iHI9AAR_axEw-22681NrhbUn4vFbNbkjwy03NCucnKDoqyfEQLe3_YS3JB64BXhbBo0tNfysFspuYyGSp-MIN9iRR_MBHAWhem0nZRHZ_Okj2NFYBx6L69oz-59tFdRgKgIeOOWVKCkIAzRR_I2zOAE-R8l4TaAxCXMHCz0g1jdYaiExm0JRGVty4euMSCheM7SfGN0izh3h5Jl-SFA6wSFPcjl.",
            "CNZZDATA1254842228": "1890872787-1714277246-https%253A%252F%252Fwww.baidu.com%252F%7C1720421616"
        }
        self.data = {
            "searchKey": "小米",
            "pageIndex": 1,
            "pageSize": 100
        }


with open("./企查查.js")  as f:
    js_code = f.read()
    execjs
import requests
import json


class Qcc():
    def __init__(self):
        self.url = "https://www.qcc.com/api/search/searchMulti"
        self.headers = {
            "3501dec9e3ec7404295c": "04c57fa43c54f5a1ffe29cba1eb0c5824905c3699914274593882bb3e357d07b965cdf4ddf72b4a8c6600d17ede4c1667370de7b30ba3d119b68585dc43ee3b2",
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9",
            "content-type": "application/json",
            "origin": "https://www.qcc.com",
            "priority": "u=1, i",
            "referer": "https://www.qcc.com/web/search?key=%E5%B0%8F%E7%B1%B3&p=2",
            "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "x-pid": "7743ba6db63e7eaef0f934f33e1f6f26",
            "x-requested-with": "XMLHttpRequest"
        }
        self.cookies = {
            "qcc_did": "7039ac87-a836-4d45-89a1-90e1df509ccf",
            "UM_distinctid": "18f22e2e4cd1d3-0fb05b5a21aa2b-1b525637-1fa400-18f22e2e4ce977",
            "QCCSESSID": "d06e14229c4cca9a4d883961e3",
            "acw_tc": "2f624a6417204208360535675e5b394889d563af737dda3014f2fc090d9ff9",
            "tfstk": "fZ9Z6dZRQtYBp4Rc8w6VzMr2DO6OQT3S3K_fmnxcfNbgCRaDTnTvCs0OCK8eqUoAhO9s3IW9dCwf5VB2mU6qP4MSFhKOBt0SPcIjmQWcmx_moD3Q5tBmP21wEQndHU6FU3G2xDSf0lqMos43KwIgotbGiyVhqwbcntYc-kjfjPb0IGV3xUtBjn2FV1mu7iHI9AAR_axEw-22681NrhbUn4vFbNbkjwy03NCucnKDoqyfEQLe3_YS3JB64BXhbBo0tNfysFspuYyGSp-MIN9iRR_MBHAWhem0nZRHZ_Okj2NFYBx6L69oz-59tFdRgKgIeOOWVKCkIAzRR_I2zOAE-R8l4TaAxCXMHCz0g1jdYaiExm0JRGVty4euMSCheM7SfGN0izh3h5Jl-SFA6wSFPcjl.",
            "CNZZDATA1254842228": "1890872787-1714277246-https%253A%252F%252Fwww.baidu.com%252F%7C1720421616"
        }
        self.data = {
            "searchKey": "小米",
            "pageIndex": 1,
            "pageSize": 100
        }

    def request_data(self):
        with open("./企查查.js")  as f:
            js_code = f.read()

        js = execjs.compile(js_code)

        header_key = js.call('main')
        k1 = header_key[0]
        v1 = header_key[1]
        self.headers[k1] = v1
        data = json.dumps(self.data, separators=(',', ':'))
        response = requests.post(self.url, headers=self.headers, cookies=self.cookies, data=data)
        print(response.text)


if __name__ == '__main__':
    qcc = Qcc();
    qcc.request_data()
