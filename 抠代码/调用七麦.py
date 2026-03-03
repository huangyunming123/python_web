import execjs
import requests

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://www.qimai.cn",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}
cookies = {
    "gr_user_id": "7b7c792d-80c9-4eb7-8641-8a889d4bd9fe",
    "AUTHKEY": "E5hrcO4r2wtvUXS9sjPzP6SUtnX6D%2FyYbupsTTE8PBxIeimOlzSEgkk5ck%2Fh1TDMKQh%2Bfp1ZMeajlgSRtlcWFTT88scE3x8tqOHu%2BCxWZuMZ3S4K4Lf%2Flg%3D%3D",
    "ada35577182650f1_gr_last_sent_cs1": "qm21146805033",
    "qm_check": "A1sdRUIQChtxen8pI0dAOQkKWVIeEHh+c3QgRioNDBgWFWVXXl1VRl0XXEcpCAkWUBd/AhUQYVYWFgILER8TUFMSZlxCR1EKCE5KVFsZXVJRWxsKFghJVktYVElWBRVP",
    "USERINFO": "JCszJABoCSPkMO7%2BcMOdOXJ9cnMDOv7iyaC3zgu7D4fHmmuOV8rjoTRo6PGzUuuMGt825dp9jsGiHGJndCDleuB0FKPy4Un1%2BF5ihkUen4zd14IIRlfuSZHHYb6Qs3M1DDXljoJ5pgr%2BTFTdqX%2B3nwylGZOSMNR1",
    "PHPSESSID": "16qveit8uisqls55ccnqc9ff9m",
    "synct": "1718164780.339",
    "tgw_l7_route": "1ed618a657fde25bb053596f222bc44a",
    "ada35577182650f1_gr_session_id": "b3a919f3-f1d5-476f-bbf6-f5a4b6a1d900",
    "ada35577182650f1_gr_last_sent_sid_with_cs1": "b3a919f3-f1d5-476f-bbf6-f5a4b6a1d900",
    "ada35577182650f1_gr_cs1": "qm21146805033",
    "ada35577182650f1_gr_session_id_sent_vst": "b3a919f3-f1d5-476f-bbf6-f5a4b6a1d900"
}
url = "https://api.qimai.cn/rank/offline"
params = {
    "date": "2024-06-12_2024-06-12",
    "country": "cn",
    "genre": "36",
    "option": "4",
    "status": "3",
    "sdate": "2024-06-12",
    "edate": "2024-06-12"
}
# response = requests.get(url, headers=headers, cookies=cookies, params=params)
#
# print(response.text)
# print(response)

with open("./七麦.js")  as f:
    js_code = f.read()

js = execjs.compile(js_code)

analysis = js.call('main', list(params.values()))

params['analysis'] = analysis
print(analysis)
response = requests.get(url, headers=headers, params=params)
print(response.text)
print(response)