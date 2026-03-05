import time

from curl_cffi import requests

import subprocess

# # 只能获取打印的结果
# sign = subprocess.run(['node', './京东搜索.js', str(1 * 10)], capture_output=True, text=True, encoding='utf-8')
# # 打印控制台结果 去掉前后空格
# print(sign.stdout.strip())

response = requests.post("localhost:5987/api/data")
json = response.json()
print(json['result']['t'])
print(json['result']['h5st'])

#
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://search.jd.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8",
    "sec-ch-ua": "\"Not:A-Brand\";v=\"99\", \"Google Chrome\";v=\"145\", \"Chromium\";v=\"145\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
    "x-referer-page": "https://search.jd.com/Search",
    "x-rp-client": "h5_1.0.0"
}
cookies = {
    "shshshfpa": "bf814928-4d47-3d39-72c3-c71e5e0a964e-1767667464",
    "shshshfpx": "bf814928-4d47-3d39-72c3-c71e5e0a964e-1767667464",
    "__jdu": "1767667462971872144113",
    "jcap_dvzw_fp": "CVXIwfbPF9EeGv33b7NIxgDFtWqxAAahd6Pe8SmbgoIKxnXovR1mWodEBnJOiNhu9TZVQrZDgaG1cPMzo-KfB_Pc2O8=",
    "pin": "jd_qFoHEezsbjPm",
    "_tp": "g%2FlAHanZikcNsLkwAdmCqA%3D%3D",
    "_pst": "jd_qFoHEezsbjPm",
    "TrackID": "1v4b6HYYRd1tY4tl_MlLCvdYqjOUfESH08--yEYvCqGs-N_BsVTqd-5dDd7XLIxqOSEyffeZhuzGHyah6OUvHPBttMu7xDtmOxaOrb2IFva-gM9AlqbIaNvzBMMi2AetY",
    "light_key": "AASBKE7rOxgWQziEhC_QY6ya2bYXyOtrVRWinvi6g4Ph0Mj-ACZk9h0LhWQ4DYuTRQbf93z8",
    "pinId": "8c1DpHryJNlfHPmPCbKQMw",
    "unick": "%E9%BB%840617",
    "unpl": "JF8EAMxvNSttW00HVhxQE0JAH18GW1QASB5WaGBRAV1bSAFXEgYfGxV7XlVdWhRKFR9uZxRXXFNIXQ4eASsSEXtdVV9fD0oeBm5vNWRcNks6BHUCGhMQTFxVWl8AQxQzbGc1VW1YTVMDHAUdFxdIVVJeVA5IFwZqZwVWbVl7VA0fMhsTEUtaVV9ZCkMfAF9XAFRcWU5SBxoFEiIRe19VX1gITB8KamY1FjOO-frRpYPMvbac8vkTXQ5MEQRoYQBTXlBNVAwdARsXFUtdVm5cOEg",
    "__jdv": "181111935|lianmeng__10__www.baidu.com|t_1003608409_|tuiguang|27bb6c9aae3c48928d66ed122dc85584|1772368122901",
    "areaId": "1",
    "mba_muid": "1767667462971872144113",
    "x-rp-evtoken": "mGW9U4qbzsaBdCMe70m9pF7nFPcDDVRBIIEbXB8N62jLc0dbEQbH4Aug57L4B3XbGyCDCUrvE-fPZ51FlkZGtg%3D%3D",
    "__jdc": "143920055",
    "thor": "783F39E74905076D93152B596A9E40875CD0C7E3BE13D8C33F18F1522F29AE951BC6977B3F78AD468263525AF466BF980875B66B54A3AD95A6FCAD8F5F0F10247929F76D9DDAE3B68B8115957F29CD4806D26A5BF7590754732C1AF8C7D0597DCFF8115CC9BDD26FB654D0DE1A978C9792BEEF7632427A79183894B603B50837201AB18031A1090285D2B182F581923DCC7900AB8A1D192B7733EFA822DD421A",
    "cid": "9",
    "ipLoc-djd": "1-72-55652-0",
    "3AB9D23F7A4B3CSS": "jdd032DNDILBCMYBBMIRCRK5LV7Q7VUXZ2EH3FVZ74CDQBTKIHFAP7GIQV2H4KSEOB55JX3KZWWIOF5DITP2KLCJ4NRWXLUAAAAM4WKX3EOAAAAAACUYH4VKCXRX3OUX",
    "shshshfpb": "BApXWlyWnsflAd-c4vwDTjcAKrmnlzCeUBiUnc0tr9xJ1PdZfQpfwnTLOiTHpMYxDft1PiqjnsawxcO5k7aoO7I0sYlGzqUZQaQg",
    "3AB9D23F7A4B3C9B": "2DNDILBCMYBBMIRCRK5LV7Q7VUXZ2EH3FVZ74CDQBTKIHFAP7GIQV2H4KSEOB55JX3KZWWIOF5DITP2KLCJ4NRWXLU",
    "flash": "3_Zjr7JfwKmUa4TUS-uRNBvXnStcVyEforAsC-0ov-1aXFmEapPN0btb3QAvTMJhLKdYyJFFgkblLOte9i4lom2fbZ6rRfaEgcnwl4FwqZfEcLPYhIQqpdgqNOz6aVRx698tqI39Wbva6HdVEUa4piA9lHxNGN30tfKNjaAUpToRaCmrGBiaQR",
    "__jda": "143920055.1767667462971872144113.1767667462.1772527437.1772587742.24",
    "__jdb": "143920055.1.1767667462971872144113|24.1772587742"
}
url = "https://api.m.jd.com/api"
params = {
    "appid": "search-pc-java",
    "t": [
        str(json['result']['t'])
    ],
    "client": "pc",
    "clientVersion": "1.0.0",
    "cthr": "1",
    "uuid": "1767667462971872144113",
    "loginType": "3",
    "keyword": "手机",
    "functionId": "pc_search_searchWare",
    "body": "\\{\"enc\":\"utf-8\",\"area\":\"1_72_55652_0\",\"page\":5,\"mode\":null,\"concise\":false,\"new_interval\":true,\"s\":92\\}",
    "x-api-eid-token": "jdd032DNDILBCMYBBMIRCRK5LV7Q7VUXZ2EH3FVZ74CDQBTKIHFAP7GIQV2H4KSEOB55JX3KZWWIOF5DITP2KLCJ4NRWXLUAAAAM4WKX3EOAAAAAACUYH4VKCXRX3OUX",
    "h5st": json['result']['h5st']
}
response = requests.get(url, headers=headers, cookies=cookies, params=params,impersonate='chrome110')

print(response.text)
print(response)