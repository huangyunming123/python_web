import json

from curl_cffi import requests
#
#

url = "https://api.m.jd.com/api"

jd_params = {
    "enc": "utf-8",
    "pvid": "ecd79c13d7dd458ab8293861ceb70f6a",
    "area": "1_72_55653_0",
    "page": 1,
    "new_interval": True,
    "s": 49
}

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://search.jd.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://search.jd.com/Search?keyword=sa&enc=utf-8",
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
    "TrackID": "1v4b6HYYRd1tY4tl_MlLCvdYqjOUfESH08--yEYvCqGs-N_BsVTqd-5dDd7XLIxqOSEyffeZhuzGHyah6OUvHPBttMu7xDtmOxaOrb2IFva-gM9AlqbIaNvzBMMi2AetY",
    "unpl": "JF8EAMxvNSttW00HVhxQE0JAH18GW1QASB5WaGBRAV1bSAFXEgYfGxV7XlVdWhRKFR9uZxRXXFNIXQ4eASsSEXtdVV9fD0oeBm5vNWRcNks6BHUCGhMQTFxVWl8AQxQzbGc1VW1YTVMDHAUdFxdIVVJeVA5IFwZqZwVWbVl7VA0fMhsTEUtaVV9ZCkMfAF9XAFRcWU5SBxoFEiIRe19VX1gITB8KamY1FjOO-frRpYPMvbac8vkTXQ5MEQRoYQBTXlBNVAwdARsXFUtdVm5cOEg",
    "__jdv": "181111935|lianmeng__10__www.baidu.com|t_1003608409_|tuiguang|27bb6c9aae3c48928d66ed122dc85584|1772368122901",
    "areaId": "1",
    "mba_muid": "1767667462971872144113",
    "x-rp-evtoken": "mGW9U4qbzsaBdCMe70m9pF7nFPcDDVRBIIEbXB8N62jLc0dbEQbH4Aug57L4B3XbGyCDCUrvE-fPZ51FlkZGtg%3D%3D",
    "cid": "9",
    "ipLoc-djd": "1-72-55652-0",
    "logintype": "qq",
    "npin": "a18895685732",
    "wlfstk_smdl": "2opn7wgxiphg5i2ju0o13qyo5wbggn7i",
    "smb_track": "683895034F334A3C82126B63E00EF137",
    "thor": "783F39E74905076D93152B596A9E40875CD0C7E3BE13D8C33F18F1522F29AE95FB8389DAD7E1885B38187A19C08C6783792D25C4E55D5DEF9AF217B63EBFBA5E981AC4F550F3D0C2D02C81EB1718998F38E896D9C8238C68969A32C65598665BC4341994CA202C3D2A624D5495265239858CC80658F2ED2A3555DB06308FAFB7728A46D2B50145E8B829F7B1750156DBFBE0A1868AC1B51FA15A8A31051D9CA1",
    "light_key": "AASBKE7rOxgWQziEhC_QY6yaooTGIKqpGdHeoEF8dnPiopfbwEBED55jspukaGF4R2wt3lIv",
    "pinId": "8c1DpHryJNlfHPmPCbKQMw",
    "pin": "jd_qFoHEezsbjPm",
    "unick": "%E9%BB%840617",
    "ceshi3.com": "201",
    "_tp": "g%2FlAHanZikcNsLkwAdmCqA%3D%3D",
    "_pst": "jd_qFoHEezsbjPm",
    "__jdc": "143920055",
    "flash": "3_NHugYWM_PkkqyRXbA6HLk-0DsKswHZ03-MHzythSyoKqcFcUmYqmGtuP_cUOyRcWfF0-0J-ytDa_o-vrfOjSapJmyWfBmHAdKX9d9OKIjofinEA8ZD5wY5GD7DRXkmUA0uYm1DEx8oHpyg7_cu2Te8F-YAEmTxO1xLsdaWId_hLNcIgRDWE6",
    "__jda": "143920055.1767667462971872144113.1767667462.1772702572.1772762534.29",
    "__jdb": "143920055.2.1767667462971872144113|29.1772762534",
    "3AB9D23F7A4B3CSS": "jdd032DNDILBCMYBBMIRCRK5LV7Q7VUXZ2EH3FVZ74CDQBTKIHFAP7GIQV2H4KSEOB55JX3KZWWIOF5DITP2KLCJ4NRWXLUAAAAM4YDQZGDIAAAAADQUSIJ4RTYFJO4X",
    "_gia_d": "1",
    "shshshfpb": "BApXW9gLpw_lAd-c4vwDTjcAKrmnlzCeUBiUnc0tu9xJ1PdZfQpfwnTLOiTHpMYxDft1PiqjnsawxcO5k7aoO7I0sYlGzqfT9BF0",
    "cn": "33",
    "3AB9D23F7A4B3C9B": "2DNDILBCMYBBMIRCRK5LV7Q7VUXZ2EH3FVZ74CDQBTKIHFAP7GIQV2H4KSEOB55JX3KZWWIOF5DITP2KLCJ4NRWXLU",
    "sdtoken": "AAbEsBpEIOVjqTAKCQtvQu17efRvGdhgd_w86O7skwsP4je0B-zw37X1RkJzr37NHfsnDZ5ThbzgQLQ7kpM_16m3D_04BKUob-SBUbTy8YcHf_ysKh6_Zx25pdqXbWXs1Eq0jgChU2_815pfzHktkxxI9CwQyMrm8YAiGiKHm1A"
}


res = requests.post("localhost:8888/api/data")

h5st_info = res.json()["result"]
params = {
    "appid": "search-pc-java",
    "t": [
        h5st_info["t"]
    ],
    "client": "pc",
    "clientVersion": "1.0.0",
    "uuid": "1767667462971872144113",
    "keyword": "口红",  # 可以换成其他的商品关键字
    "functionId": "pc_search_getShopAndWare",
    "loginType": "3",
    "body": jd_params,  # 接口请求的body为明文
    "x-api-eid-token": "jdd032DNDILBCMYBBMIRCRK5LV7Q7VUXZ2EH3FVZ74CDQBTKIHFAP7GIQV2H4KSEOB55JX3KZWWIOF5DITP2KLCJ4NRWXLUAAAAM4YDQZGDIAAAAADQUSIJ4RTYFJO4X",
    "h5st": h5st_info["h5st"]
}
# dumps = json.dumps(params)
# print(dumps)
response = requests.get(url, headers=headers, cookies=cookies, params=params,impersonate='chrome110')

print(response.text)
print(response)