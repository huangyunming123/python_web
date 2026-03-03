from curl_cffi import requests


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://search.jd.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Google Chrome\";v=\"144\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
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
    "thor": "783F39E74905076D93152B596A9E40875CD0C7E3BE13D8C33F18F1522F29AE951BC6977B3F78AD468263525AF466BF98DF1065AE1C757735F5E5A3A441ECB563C4D2A7E39A7552E3B9468492597158F3B380DFB4EC754DDD54301F46FF3BD2AA8FA7CB1E12E30107C0E63474C1C303B0D3755A951CAD9F91E493BF3DE0DBCA22F2A00C0E1FD890BE714E0C86151B778304E1DC45B7D353B21B7AF2C6343369D0",
    "3AB9D23F7A4B3CSS": "jdd032DNDILBCMYBBMIRCRK5LV7Q7VUXZ2EH3FVZ74CDQBTKIHFAP7GIQV2H4KSEOB55JX3KZWWIOF5DITP2KLCJ4NRWXLUAAAAM4VSX7VOQAAAAADOFCWYLWIW3O34X",
    "cid": "9",
    "3AB9D23F7A4B3C9B": "2DNDILBCMYBBMIRCRK5LV7Q7VUXZ2EH3FVZ74CDQBTKIHFAP7GIQV2H4KSEOB55JX3KZWWIOF5DITP2KLCJ4NRWXLU",
    "ipLoc-djd": "1-72-55652-0",
    "shshshfpb": "BApXW47S4r_lAd-c4vwDTjcAKrmnlzCeUBiUnc0tq9xJ1PdZfQpfwnTLOiTHpMYxDft1PiqjnsawxcO5k7aoO7I0sYlGzqRFOKuA",
    "__jdc": "143920055",
    "flash": "3_Bn0v2AIOFDiDPbVss_4Fosradh6PrsXsXZGFXrzyoAwsLosB3ijXrPcnerMBH1SQaXG9NF1S5WgJf_ZhLXqIQG03S39eK7bEY1Xw3ppYcuFEvhTqzWPQSdebLPtIgvQoQ0-FxgPMFAi5cG_AM265g5rFM-0UKqHAsFKoWco017IkLJ2KlBiS",
    "__jda": "143920055.1767667462971872144113.1767667462.1772423737.1772432250.19",
    "__jdb": "143920055.1.1767667462971872144113|19.1772432250",
    "sdtoken": "AAbEsBpEIOVjqTAKCQtvQu17f_84aMksRcCG2dzhfUXvTHXJ3GNyfCPqu-EltxZ8-34_CLKq0TwjGtlWeneEOLY4MtCSrkxCw7A67dQ-2MVBHNlmF9G2rBbCr9P-2EW5mtQOchYjeXPEZjVBqMne6FC1iBazaWRTBdwGFhjaz5U"
}
url = "https://api.m.jd.com/api"
params = {
    "appid": "search-pc-java",
    "t": [
        "1772432294697",
        "1772432294699"
    ],
    "client": "pc",
    "clientVersion": "1.0.0",
    "cthr": "1",
    "uuid": "1767667462971872144113",
    "loginType": "3",
    "functionId": "pctradesoa_mixer",
    "body": "\\{\"lim\":12,\"p\":202002,\"ec\":\"utf-8\",\"uuid\":\"1767667462971872144113\",\"lid\":\"1\",\"ck\":\"pinId,lighting,pin,ipLocation,atw,aview\",\"page\":\"1\",\"c1\":\"\",\"c2\":\"\",\"c3\":\"\",\"brand\":\"\"\\}",
    "x-api-eid-token": "jdd032DNDILBCMYBBMIRCRK5LV7Q7VUXZ2EH3FVZ74CDQBTKIHFAP7GIQV2H4KSEOB55JX3KZWWIOF5DITP2KLCJ4NRWXLUAAAAM4VSX7VOQAAAAADOFCWYLWIW3O34X",
    "h5st": "20260302141817698;im6tawzwg3033q35;f06cc;tk03w9ea91ba018n1vkuJNPq6nOmxX4zDwHD6YNT9RWzcZ1gHMCDpHL96Il4k-_MOVLs7rmyLWrR3lW9gc-l7AxhDn3C;234dfb6ccebf466e23e43ec9e6b425793000e0c8788ab3a1fcb7b89bcc1fbc38;5.2;1772432294698;fZRCXZPUudqVuhuV6E6DqcbErtLH-h-T-h6I-hfZXxfTB5_ZzUrJ-hfZXx-ZAILTsBeTtJLTqZ_VAQOTq9_JrV_J-IOVrZbTAI_ItZ_ZB5_ZxIdG6YLIqYfZB5hW-JrV7ILJq9_Vu9eV_M_JsdbVrRrJsdbTwJ7VqZ7Up9eU-h-T-VKJroLJ_YfZB5hW-dOW-h-T-ROE-YfZB5hW-9_WvpPUrkMI187ICMeH-h-T-J6ZBh-f1ZvEwA8LM4sErN6V38tF-h-T-trG9oLJvYfZB5hW-xLItoLP_cLO-h-T-JbF-hfZXxPCBh-fvh-T-dOVsY7ZBhfZB5hWtdeZnZfVwN6J-hfZBh-f1BOWB5_ZvdOE-YfZBhfZXx-ZM07J6UMW5YePqU6ZB5_Z0kbIzc7F-hfZBh-f1heZnZfTsY7ZBhfZB5hWxh-T-FOE-YfZBhfZXxvVvh-T-JOE-YfZBhfZXxfVB5_ZsN6J-hfZBh-f1heZnZfUsY7ZBhfZB5hWsFeZnZvVsY7ZBhfZB5hW-J_WwpfV-h-T-dOE-YfZBhfZXxfVB5_Z2E6ZBhfZB5hWsh-T-VaG-hfZBh-f1heZnZfG-hfZBh-f1heZnZfIqYfZBhfZX1aZnZfIzMbEpM7ZBh-f1taZB5BZ0g8H-U6D8MdPyINFCQ7H-h-T-ZeF-hfZBh-fmg-T-haF-hfZXx-ZqlMUwlcVwhfLBVsOBVLJUgfG8Q6GYgvT5UqGtoLH_cLO-h-T-dLEuYfZB5xD;20a1bb43ec3be974894b2a92885df756f5d705a7cc06fcf89d7acf1e0cf4a6e0;gRaW989Gy8bE_oLE7w-Gy8rFvM7MtoLI4wrJ1R6G88bG_wPD9k7J1RLHxgKJ"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params,impersonate="chrome110",)

print(response.text)
print(response)