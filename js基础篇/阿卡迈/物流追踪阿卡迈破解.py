import requests


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Google Chrome\";v=\"144\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}
cookies = {
    "cookieDisclaimer": "seen",
    "ak_bmsc": "317C05E69F4C50810CDB7B44BF63425C~000000000000000000000000000000~YAAQZtzdPLMfGSacAQAAcR90Kx4DnywxoY1S/xtxegCblAMVNLfqQMDC8R9L4CiWKmBuSt35dcx92qR6Vqy1MajbNoH4w4uFVb/Q6QH1k9/FIAZAaxqmbsdqOws7Oo4LLtIsqscb477kxA4PBdba8cQGqihyF40ZsUkGBe5M6hce2cxM3/jmCCwAzAgzU47wp5KItqyVM0C4Eq3LYxvhO/8xQmn7Im+N0P5UTHpRulg4wNgDRxyotcKjd4Rjoii6ut9OLZArWdBFimSQLggQJHsv8xUaWcPW2VYMxEKH+CDD3xLZmwdLJNYeLeFpgeM/c6iVJ2r6A/L8BYGStWSKQPCg1kBA4ejCE9a+MHkXaFfEKIUpk+OaX6QQPyrz+Pc3QIdt6ovrmFeg",
    "tracking-id": "1232343",
    "OptanonAlertBoxClosed": "2026-02-05T01:39:24.256Z",
    "OnetrustActiveGroups": "%2CC0001%2CC0002%2CC0003%2CC0004%2C",
    "OptanonConsent": "isGpcEnabled=0&datestamp=Thu+Feb+05+2026+09%3A39%3A24+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202411.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=17f14561-d337-424d-9e97-f33753978b98&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1",
    "s_ccst": "{%22ecid%22:true%2C%22aa%22:true%2C%22target%22:true}",
    "AMCVS_9D88879D5579828F7F000101%40AdobeOrg": "1",
    "AMCV_9D88879D5579828F7F000101%40AdobeOrg": "179643557%7CMCIDTS%7C20490%7CMCMID%7C04120748905440280812568583963652759079%7CMCAAMLH-1770860365%7C11%7CMCAAMB-1770860365%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1770262765s%7CNONE%7CvVersion%7C5.5.0",
    "s_cc": "true",
    "at_check": "true",
    "mbox": "session#93c044d20d4846009b6f09013b5d5ab0#1770257427|PC#93c044d20d4846009b6f09013b5d5ab0.38_0#1833500367",
    "s_sq": "%5B%5BB%5D%5D",
    "_abck": "FEB9F6C3C6FEE8F70E735DC6FBE4C2BA~0~YAAQZtzdPGQgGSacAQAAkWd0Kw+co/cSsfZnM6Rm3Z22aqQ5aB4n32abAk/FZs//zaywepE5Ncn3do3dMKKaJPLVjhS2ywL/U2uS2CLsU/ggCGMO93Vi/Cz+h/ZhImFk5Sp4Bgb6Jh9yQS4RypfRYX6AZ1NrWLObeJUFx1GloOOAdQWHp6S1aqgsHeaR7DPJx0iRgl+CYh7aUwl/hOkbMZENUjKVHteiQNZfDPKmwQOgkXb0Q9jCRSbpOR2oH23O9c8aVc2hjDAqd8Z9HvX61zho4bpTNLQBwmtWIsMRqTI3hB05D/dF7QeskWe6n8QUNwdndzjR1uJiKm/zkxLWsNZ6ADSQ/WN4xAx9QKv/39OnBJz/0C0rGBZACcVWNVyU312Kzftyx2S2V6plqedm5MY5bB8A3pXO2ZAoYDO+EKm5HrFplfNPUJSNISHC0IgRF07yT2qqaZPKvtwYCkEDGMxUmSGTDQlsaCA20DGdFgX2hjKwdhDm0UGGG7ZLS9MZBdnlJ77mLHMiAw3B55xXzKFNRYeD0Ns1E63avCnZGllsOLFoQ7TLfR+gJJrgpcHnYDjivYDWcWetZE1MHITnpn2/VA2NuMW4Zd18hhYsGc7cIbber9mUrE/L56bLOl8J11MQVorf/hxGfKxMSB0kpfIOd8x3NhEbHST+wemrfmfZJyqdVVrx8YCYRyT6mPJijSTWTkCmUwrk6K3pq32lLkXxDnohvKBuDVqIdk/DB+ZvEI6p0wJCmr49U4u47zBevhObv59PFm04iGPbeY2yFzz/RAt3msbTTCp+yN5vNHPx+VGGK6HjNYc6X1kCsYLv6mTTcy4Mzua6zWkEAbwEw8Hq5KhwYCgA1yOBTdkPgImL2xjQnRtCxVQox2DnsukETTAccnNefx+t8VtJBQ4LwiyJbd9wZbhUqndUwBeiPPHpGzL1uekswY8=~-1~-1~-1~AAQAAAAF%2f%2f%2f%2f%2f6LcNQIayLmwXw6FpVSmkCIP+3lK5IiFhAq7car5OllZnGGKL%2fD0SHkqYQUHjlDi78Xr03apzAGkSp0qCpqRCCARkHopzvDeXQJX~-1",
    "bm_sz": "C296C84DF4733D0AD931B70F961FCB31~YAAQZtzdPGYgGSacAQAAkWd0Kx4KeLVdAXLeLWQ2VMTipp5dqyw9E1mN8B5tYAUQzQoIfhXU1xFQmdDxtcJj4hPX2QLhCWmxZiX/Dgf6YDoyBNCM/6UoFHGd+G5z7GwOkDrRc88iDQ3ue1uHNkVFUWH+uv+0gx1i+Dan5DeHh34VXfmeqOQeJq2vbVXaDkZGicvgWcOqT4ES0xsmJ0aM6P7L8IvhJXe+A9u4m+JkLdwPgNrc86rEU0Rqby4Rgy+MCUpGlgZIX+BIlySOwT7fAEw12BRqecG/VAG2xRur5kqGTU4AceZ8w/4/VoCz3aQ1nJRXUiXTrEbJMbpjmRheEOmwoEpJJ12EzhnNORaEbuHmTyrnd02meHN0r8HGi9Dkv71mqFcZesT3sGDKmt5Npyu3tQqxcOlz35LNZ71RWJjpf6Egxlc=~4601395~3420724",
    "bm_sv": "04E1BC863160696AE4DCFBA0562A90D0~YAAQZtzdPGcgGSacAQAAyWd0Kx6VWURRWJov9qrrMnMvrTq8046xsymwYJZRbRYogCIR3FwMXMCSYaf8blDo/q5Nv7yheNvXZW/tvP0D7ANKOoFLD47buLSb0NTg6ZyWkP8690PqojhcWU2LMIk6ZIlNZx6qjzng0WhLIXMJp65e60U2vf6aXvFn8T7P1SMO3V34w2OjtUp4jMKmMLQafklcMiH5oWgMf1Asliwbrdd/rknuGAM50+zsOiCq~1",
    "da_sid": "EAB7C0668E3DAED72BFFAA13A87D0C7B88.0|4|0|3",
    "da_lid": "D984F3559A7DEA4CBEAEBB99EA7F46703B|0|0|0",
    "da_intState": "",
    "kampyle_userid": "f6da-9317-82fb-7556-d144-d0af-d825-b406",
    "kampyleUserSession": "1770255579253",
    "kampyleUserSessionsCount": "1",
    "kampyleUserPercentile": "15.471110323100657",
    "kampyleSessionPageCounter": "1"
}
url = "https://www.dhl.com/cn-zh/home/tracking.html"
params = {
    "submit": "1",
    "tracking-id": "1232343"
}
# response = requests.get(url, headers=headers, cookies=cookies, params=params)

response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)