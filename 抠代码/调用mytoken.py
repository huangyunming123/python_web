import execjs
import requests

headers = {
    "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    "Referer": "https://mytokencap.com/",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "sec-ch-ua-platform": "\"macOS\""
}
url = "https://api.mytokenapi.com/ticker/index"
with open('./mytoken.js') as f:
    js_code =f.read()
    js = execjs.compile(js_code)
    data = js.call('getMD5')
params = {
    "language": "en_US",
    "timestamp": data[0],
    "code": data[1],
    "platform": "web_pc",
    "v": "0.1.0",
    "legal_currency": "USD",
    "international": "1"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)