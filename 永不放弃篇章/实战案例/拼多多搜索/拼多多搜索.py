import requests


headers = {
    "Accept": "application/json, text/javascript",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Origin": "https://pinduoduo.com",
    "Pragma": "no-cache",
    "Referer": "https://pinduoduo.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not:A-Brand\";v=\"99\", \"Google Chrome\";v=\"145\", \"Chromium\";v=\"145\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
url = "https://apiv2.pinduoduo.com/api/gindex/tf/query_tf_goods_info"
params = {
    "tf_id": "TFRQ0v00000Y_13396",
    "page": "1",
    "size": "39",
    "anti_content": "0aqAfa5e-wCE0_adXNSt_USOOG7GN5X_xMn2xti3QamJEqN8spiiXxZMl_mJftXyBfi2SOoiKXl0WqqlpxU0_8n5_jXGToXGmYXG9Ynp6Tnqmjnq4qnpXxX9VSmPVkcJIorHptqHK4KSOT8hxSqfxuw8ypQTg60nqg3XLNUhq50zHgqIxTywogSSl9WI24VEBCTDjCkDLLKbsVTUfXkMKIUMv-ZDjKHI-uHK10Vrw6ZLLl5UfleMkICMK1mMkRKbfaw26tCSTMT722d4g3X_xqtVBKKYPCSxGzPX6vnx5XPNXSq5D0P4E-QX00xX8wlG7AnqqmhxQdqqdSyIoIIPsIF_HeO56QjWga3AEg292h9Ea0kZMBSJ"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)