import execjs
import requests
import json

#    遇到异步的 需要在异步回调方法 寻找第一个返回 方法
for i in range(1, 2):
    with open('企查查获取请求头.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
        js = execjs.compile(js_code)
        data =  {"searchKey": "京东", "pageIndex": i, "pageSize": 20}
        key = js.call('getKey', data, '/api/search/searchMulti')
        value = js.call('getValue', data, '/api/search/searchMulti')
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "content-type": "application/json",
            key: value,
            "origin": "https://www.qcc.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://www.qcc.com/web/search?key=%E4%BA%AC%E4%B8%9C&p=2",
            "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
            "x-pid": "5e8f2dde6ce30b8c133e416ec9f41ef9",
            "x-requested-with": "XMLHttpRequest"
        }
        cookies = {
            "qcc_did": "1dc3419e-39e0-4ed8-ad1e-fa98f8cb3788",
            "UM_distinctid": "1958e9388ef1dc-0a6793a0049e9a-1d525636-13c680-1958e9388f01278",
            "QCCSESSID": "2654d6878b418b079d0831c869",
            "tfstk": "gK4tO2MuX6dtuvztt5SHnKoR_YC3WMVZsRPWoxDMcJeLN7JiccXZHkebLcD_kS8xGSwV_xfNx5PZuq6lErQu_5Jq22vGKq1bOqcvKoXPm5PZuBlTF7y4_IEfOO3sl-gIAjGmlETsh6dIsvTsGFGXd6HEdC9jfcGBOfl6fqgbhW1KgvMjlcwbOU4cHvOsnEEkSvWcNMwplEaK6cs31vTjTyhtXYN_nETXNfntF5MdENWuKmetXyb9UfEQwJlT3a8Z5mE_VVaAeN3Qak2s9-6JDvZ87rnuWTKrCPk4eVZddF3j7bFxqkfX2vqbTynLWgAqTPVb7005zdM0x7UxMrWVJ8F_Bui75dIrcz4RW7voejx196K20cGeoAXo-FEmokGKE1Qv0noFTExTo3t20DIE9Yfnln-qY65..",
            "CNZZDATA1254842228": "1166227559-1725385215-%7C1750730683",
            "acw_tc": "0a472f8117507377596175268e007d0ef2b4472cab97ae7a322043548057fc"
        }
        url = "https://www.qcc.com/api/search/searchMulti"

        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(url, headers=headers, cookies=cookies, data=data)

        print(response.text)
        print(response.json())
