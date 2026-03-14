import json
import requests
# 如果报错编码问题  需要在最开始引入下面文件
# import subprocess
# from functools import partial
# subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

data = {
    "cursor_score": "",
    "num": 31,
    "refresh_type": 1,
    "note_index": 28,
    "unread_begin_note_id": "",
    "unread_end_note_id": "",
    "unread_note_count": 0,
    "category": "homefeed.food_v3",
    "search_key": "",
    "need_num": 6,
    "image_formats": [
        "jpg",
        "webp",
        "avif"
    ],
    "need_filter_image": False
}
encrypt_url = '/api/sns/web/v1/homefeed'
# json_data = json.dumps(data)
# 注意：需要在调用 JS 之前将 data 转为 Python 字典，让 execjs 自动处理
    # 先不序列化，保持为 Python 字典，让 execjs 处理
# x_s = execjs.compile(open('./main.js', 'r', encoding='utf-8').read()).call('getRes', encrypt_url, json_data)
params = {
    "data": data,
    "encrypt_url": encrypt_url
}
requests.post('http://localhost:5233/xhs/data', json=params)


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://www.xiaohongshu.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.xiaohongshu.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "x-b3-traceid": "8982d930de9a17ef",
    "x-s": x_s,
    "x-s-common": "2UQAPsHC+aIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0c1Pjh9HjIj2eHjwjQgynEDJ74AHjIj2ePjwjQhyoPTqBPT49pjHjIj2ecjwjHMN0Z1+jHVHdWMH0ijP/DEw/Z9P9zfPepA+9k6Pn4jG9pU4oG9qgcl4AGlynS6Jo8E47pYPgPMPeZIPerFPecIPsHVHdW9H0ijHjIj2eqjwjHjNsQhwsHCHDDAwoQH8B4AyfRI8FS98g+Dpd4daLP3JFSb/BMsn0pSPM87nrldzSzQ2bPAGdb7zgQB8nph8emSy9E0cgk+zSS1qgzianYt8p+1/LzN4gzaa/+NqMS6qS4HLozoqfQnPbZEp98QyaRSp9P98pSl4oSzcgmca/P78nTTL08z/sVManD9q9z18np/8db8aob7JeQl4epsPrzsagW3Lr4ryaRApdz3agYDq7YM47HFqgzkanYMGLSbP9LA/bGIa/+nprSe+9LI4gzVPDbrJg+P4fprLFTALMm7+LSb4d+kpdzt/7b7wrQM498cqBzSpr8g/FSh+bzQygL9nSm7qSmM4epQ4flY/BQdqA+l4oYQ2BpAPp87arS34nMQyFSE8nkdqMD6pMzd8/4SL7bF8aRr+7+rG7mkqBpD8pSUzozQcA8Szb87PDSb/d+/qgzVJfl/4LExpdzQ4fRSy7bFP9+y+7+nJAzdaLp/2LSizgbzwgbMagYiJdbCwB4QyFSfJ7b7yFSenS4o+A+A8BlO8p8c4A+Q4DbSPB8d8ncIyFkQy/pAPFSUz0QM4rbQyLTAynz98nTy/fpLLocFJDbO8p4c4FpQ4S+IGLrM8n8l4ApIwLTAzb87cDDAy7QQ2rLM/op749bl4UTU8nTinDbw8/b+/fLILoqEaL+wqM8PJ9p/GDSBanT6qM+U+7+nJD8kanTdqM8n4rMQygpDqgb7t7zl4b4QPAmSPMm7aLSiJ9LA4gclanSOq9kM4e+74gz1qMm7nrSeG9lQPFSUP04VyAQQ+nLl4gzeaLp/NFSbadPILoz1qbSQcLuIafp88DclaLpULrRc4rT6qgqAa/+O8gYl4b4z/epSygkDqMz/zgSQzLkSy9c6q9Tc4o+1Lo4laL+t8p+c49SQyepSpDbM/rS9+np8JURSPbmFLFSea7+nqg4n+BRTqLDAt9RQ2rkSPnlmq9SV+7PIn08Sngp74rSe/LpQc9WAqob78FShyLTQPAmSnnb+2gkja9pnpdq9agYcz/zM4AY6c0pSPnM6q7Yn49RCpd41aL+czrSbJgQOqg4o4b8FGLDAPBp/a/mApSm7GaHVHdWEH0iTP/rlP0qA+eGhwsIj2erIH0iINsQhP/rjwjQ1J7QTGnIjKc==",
    "x-t": "1765868387001",
    "x-xray-traceid": "cd92eb7cde629f450f6bfa254aabd8ae",
    "xy-direction": "59"
}
cookies = {
    "abRequestId": "5e9f5f1c-4ae7-52d4-9e20-622b3b1cdfc2",
    "a1": "1999063df05s7jo1gbcertv6qt1w61iiolvywua1s50000140400",
    "webId": "812941f19b661d1532801b3d2fc6f34a",
    "gid": "yjjj8Kqdj4lJyjjj8Kqfi17082MWVlykDSdFhyM9hKA9yv28EKy33E888y484888Wfj2qiWJ",
    "web_session": "030037afea646c0d1e8902db462e4ae80f052c",
    "webBuild": "5.0.6",
    "xsecappid": "xhs-pc-web",
    "loadts": "1765866375963",
    "websectiga": "634d3ad75ffb42a2ade2c5e1705a73c845837578aeb31ba0e442d75c648da36a"
}
url = "https://edith.xiaohongshu.com/api/sns/web/v1/homefeed"

data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)



