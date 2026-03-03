import requests
import execjs
import pymongo
import json

class GuanNiao:
    def __init__(self):
        self.con = pymongo.MongoClient()
        self.db = self.con['spiders']['gn']
        self.headers = {
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
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "requestId": "5c9f03183a1f1344be38d193458abcf2",
            "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sign": "306f3cde26bca82cd0fb52a9efb95f64",
            "timestamp": "1733819569000"
        }
        self.url = "https://api.birdreport.cn/front/activity/search"
        self.data = '{"limit":"20","page":"%s"}'
        with open('官方.js', 'r', encoding='utf-8') as f:
            js_code = f.read()
        self.js = execjs.compile(js_code)

    def get_data(self, page):
        da = self.data % page
        res = self.js.call('beforeSend', da)
        print(res)
        self.headers['sign'] = res['sign']
        self.headers['timestamp'] = str(res['timestamp'])
        self.headers['requestId'] = res['requestId']
        response = requests.post(self.url, headers=self.headers, data=res['data'])
        return response.json()

    def parse_data(self, response):
        result = self.js.call('decode', response['data'])
        for i in json.loads(result):
            # print(i)
            item = {}
            item['address'] = i['address']
            item['id'] = i['id']
            item['username'] = i['username']
            item['endTime'] = i['endTime']
            self.save_data(item)

    def save_data(self, item):
        print(item)
        # self.db.insert_one(item)

    def main(self):
        for i in range(1, 2):
            res = self.get_data(i)
            print(res)
            self.parse_data(res)


if __name__ == '__main__':
    gn = GuanNiao()
    gn.main()