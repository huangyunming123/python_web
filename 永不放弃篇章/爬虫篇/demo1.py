import requests


headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://item.jd.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://item.jd.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "x-referer-page": "https://item.jd.com/53651009583.html",
    "x-rp-client": "h5_1.0.0"
}
cookies = {
    "shshshfpa": "bf814928-4d47-3d39-72c3-c71e5e0a964e-1767667464",
    "shshshfpx": "bf814928-4d47-3d39-72c3-c71e5e0a964e-1767667464",
    "__jdu": "1767667462971872144113",
    "areaId": "1",
    "ipLoc-djd": "1-72-55653-0",
    "TrackID": "1ViNTvKUAhIghTWCM3NmnwuA_iREucSftRwlUOIW0Cu_btA59qFpd-0CAzNBtkfyfvOC1obgnW_PSGvi6fOToDkBil10UejPDdMdaFhucraUSHMOKlpBChLOuwvZTY-d2",
    "jsavif": "1",
    "unpl": "JF8EAMhnNSttDBkEDB9QHkBCTgkHW1oOTR4GbTBQVl8MSgAATFFMEUB7XlVdWhRKFx9ubxRUWlNOUw4eBysSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAh0VFkxaUltaC0MRA2ZhBlRYXUtUBysDKxUge21SWlQLTRQzblcEZB8MF1IDHAcaEV1LW1NYWg9NEgRsbwNUVF5IVAAeAhsQIEptVw",
    "TARGET_UNIT": "bjcenter",
    "__jdv": "76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_eca85c4cc4eb4677843fd33e0e4fbf2a|1767948421476",
    "jcap_dvzw_fp": "CVXIwfbPF9EeGv33b7NIxgDFtWqxAAahd6Pe8SmbgoIKxnXovR1mWodEBnJOiNhu9TZVQrZDgaG1cPMzo-KfB_Pc2O8=",
    "wlfstk_smdl": "zpgopptk5mnfzgotmgpx7xm6i2fnurit",
    "3AB9D23F7A4B3CSS": "jdd032DNDILBCMYBBMIRCRK5LV7Q7VUXZ2EH3FVZ74CDQBTKIHFAP7GIQV2H4KSEOB55JX3KZWWIOF5DITP2KLCJ4NRWXLUAAAAM3UHY3MKQAAAAAD7SWBU2XVI73QEX",
    "_gia_d": "1",
    "joyya": "1767948476.1767948538.25.1hzczm1",
    "thor": "783F39E74905076D93152B596A9E40875CD0C7E3BE13D8C33F18F1522F29AE957C1909B5E51EF6B2CFD2F3E988DC8D6668D465CF936CB979046FF71C23BBBE8FF5B44D20B7DCB267E8864CA260DD4A32FD441CE838E89F473FF7D203FB1F1583AD46A5D0E1380CB17B7B36EDEEAD658D2C129D7EFD4D10BCCDC2D2DC7560B8DBD1A7F77127AF5DA781AA52F0F07F7BB654F6034A7F9981B4C1F4A4522D99A2ED",
    "flash": "3_qzT_v5eg_j3WD7kNT4VwEcqMgJuZx51iu6o3Q-jpIZZWVRIBA5HNJTEe6ZMps0nz-npiQc52iGJb6l0PpHAcm3-YF5xw_KlDUHhw1u5-ZUbJp4mkvweNZT0qAF3spSO6Cv7HWRq6NZ14n8RJ6i5d8_LifY5fRDW37vAhx56kByG0Vezjr11h",
    "light_key": "AASBKE7rOxgWQziEhC_QY6yauurqaItg9aCr8KPIFwr23wOTp6jpFr9Whmu5Xda-1LaSytbv",
    "pinId": "8c1DpHryJNlfHPmPCbKQMw",
    "pin": "jd_qFoHEezsbjPm",
    "unick": "%E9%BB%840617",
    "ceshi3.com": "203",
    "_tp": "g%2FlAHanZikcNsLkwAdmCqA%3D%3D",
    "_pst": "jd_qFoHEezsbjPm",
    "3AB9D23F7A4B3C9B": "2DNDILBCMYBBMIRCRK5LV7Q7VUXZ2EH3FVZ74CDQBTKIHFAP7GIQV2H4KSEOB55JX3KZWWIOF5DITP2KLCJ4NRWXLU",
    "token": "505cf6b2b95921ca109100bb5958b816,3,982193",
    "__jda": "181111935.1767667462971872144113.1767667462.1767948389.1767948405.5",
    "__jdc": "181111935",
    "cn": "10",
    "shshshfpb": "BApXW0oP6ov5Ad-c4vwDTjcAKrmnlzCeUBiUnc0sX9xJ1PdZfQpfwnTLOiTHpMYxDft1PiqjnsawxcO5k7aoO7I0sYlGzqUulcow",
    "__jdb": "181111935.18.1767667462971872144113|5.1767948405",
    "sdtoken": "AAbEsBpEIOVjqTAKCQtvQu172vG2WPXJfqDbJD0l7P-QhWCskpcOdFmR20EHkdM5QVzvakL3dYZ9n3TsbIb6KVQEFCVEPLlJldDLZfVFTj-mMdljvfPaUadKgSDXFK3VkC89kDp2Tl-LSWtrQxsfpxvwt30EV1Uk-OCBaTDzOYGggjvXT-xoh6O7kz5PJA"
}
url = "https://api.m.jd.com/"
params = {
    "appid": "pc-item-soa",
    "functionId": "pc_detailpage_wareBusiness",
    "client": "pc",
    "clientVersion": "1.0.0",
    "t": "1767948571359",
    "body": "{\"skuId\":53651009583,\"cat\":\"670,716,42312\",\"area\":\"1_72_55653_0\",\"shopId\":\"994966\",\"venderId\":10148377,\"paramJson\":\"{\\\"platform2\\\":\\\"1\\\",\\\"colType\\\":0,\\\"specialAttrStr\\\":\\\"p0ppppppppp3ppp3ppppppppppppp\\\",\\\"skuMarkStr\\\":\\\"00\\\"}\",\"num\":\"1\",\"bbTraffic\":\"\",\"canvasType\":1,\"giftServiceIsSelected\":\"\",\"customInfoId\":\"\",\"sfTime\":\"1,0,0\"}",
    "h5st": "20260109164938090;tig366ww9dq0tdp5;fb5df;tk03wb1ab1c8518nS40QzToYh8RGMzpPKaDQrdRItl2PpzFqZylJ1r4BGJZ77nEh4xzIPOOuuFnq6zXVeGDQL4tmZqAS;7b13db11f91da2aef286a744ff891faa;5.2;1767948572090;fZRCXZfTzd_WxZfZnZPVsY7ZBh-f1ZPUxQbExdaIoFqErJuV68bE-h-T-h6I-hfZXxfTB5_ZzUrJ-hfZXx-ZAILTsBeTtJLTqZ_VAQOTq9_JrV_J-IOVrZbTAI_ItZ_ZB5_ZxIdG6YLIqYfZB5hW-JrV7ILJq9_Vu9eV_M_JsdbVrRrJsdbTwJ7VqZ7Up9eU-h-T-VKJroLJ_YfZB5hW-ZOW-h-T-ROE-YfZB5hW-F_WvpPUrkMI187ICMeH-h-T-J6ZBh-f1Z-PvZ8LqttVutNMpZfZnZPGyQ7GAY6ZBh-f1ZfG8Q6GYULJUYfZnZ-IxYfZB5hWkgfZXZ-GbYfZnZvVwN6J-hfZBh-f1VeZnZPVwN6J-hfZBh-f1ROVB5_ZxdOE-YfZBhfZXxfT0h-T-ZOVsY7ZBhfZB5hW-hcGwNdNM0NJu1rJCYfZnZPGyQ7GAY6ZBhfZB5hWxh-T-BOE-YfZBhfZXxfVB5_ZqN6J-hfZBh-f1V_VB5_ZrN6J-hfZBh-f1heZnZPUsY7ZBhfZB5hWxh-T-ROE-YfZBhfZXxfUxdeZnZvVsY7ZBhfZB5hW-9_WwpfV-h-T-dOE-YfZBhfZXxfVB5_Z2E6ZBhfZB5hWsh-T-VaG-hfZBh-f1heZnZfG-hfZBh-f1heZnZfIqYfZBhfZX1aZnZfIzMbEpM7ZBh-f1taZB5BZ0g8H-U6D8MdPyINFCQ7H-h-T-ZeF-hfZBh-fmg-T-haF-hfZXx-ZqlMUwlcVwhfLBVsOBVLJUgfG8Q6GYgvT5UqGtoLH_cLO-h-T-dLEuYfZB5xD;ee8132094fa4cac82c0e872bf06fd2db;gRaW989Gy8bE_oLE7w-Gy8rFvM7MtoLI4wrJ1R6G88bG_wPD9k7J1RLHxgKJ",
    "x-api-eid-token": "jdd032DNDILBCMYBBMIRCRK5LV7Q7VUXZ2EH3FVZ74CDQBTKIHFAP7GIQV2H4KSEOB55JX3KZWWIOF5DITP2KLCJ4NRWXLUAAAAM3UHY3MKQAAAAAD7SWBU2XVI73QEX",
    "loginType": "3",
    "scval": "53651009583",
    "uuid": "181111935.1767667462971872144113.1767667462.1767948389.1767948405.5"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)