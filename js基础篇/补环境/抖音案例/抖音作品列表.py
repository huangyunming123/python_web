import json

import requests

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://www.douyin.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.douyin.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "bd-tt-error-code": "0",
    "content-encoding": "br",
    "content-type": "application/json",
    "vary": "Accept-Encoding",
    "uifid": "9e5c45806baed1121aef2e4ebdb50ae0783a7b9267143d29acaade7dde1bacd527b03a068a9abdb7833ae78af98d5b7b1a6dcfae23bc2e22a1e29b89a4771c8d672279a54a7b1986b5628f6af005121a444c6628e9c2f3f3a0b4fedec9d5a2e3c52e1ce4b3b733e6154bb4a45cec893a1752dc278450a5e023b52c54590762453af552ce3a185ddcab973f136395d0a8fe242b780cdd73439975f7b459b226a9dfb7283a61810ddad08b0df53c75e2ba132ea68f2f03e6e400cb53a3c4878389",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
cookies = {
    "ttwid": "1%7CAQoguTP6gkkfX-4NL5d_RCF6Eda7v2PrL6H74cXREBc%7C1726736428%7C299651b4a8701d405409762681563542cbe8487357678df969c99548e182eb40",
    "UIFID_TEMP": "9e5c45806baed1121aef2e4ebdb50ae0783a7b9267143d29acaade7dde1bacd5d631dbf879422468b41ca734fd38b29055c81decabb0009d62ce42a759a2d17b4ecbbab4bd9a815f83858d98e4813c4f",
    "hevc_supported": "true",
    "bd_ticket_guard_client_web_domain": "2",
    "UIFID": "9e5c45806baed1121aef2e4ebdb50ae0783a7b9267143d29acaade7dde1bacd527b03a068a9abdb7833ae78af98d5b7b1a6dcfae23bc2e22a1e29b89a4771c8d672279a54a7b1986b5628f6af005121a444c6628e9c2f3f3a0b4fedec9d5a2e3c52e1ce4b3b733e6154bb4a45cec893a1752dc278450a5e023b52c54590762453af552ce3a185ddcab973f136395d0a8fe242b780cdd73439975f7b459b226a9dfb7283a61810ddad08b0df53c75e2ba132ea68f2f03e6e400cb53a3c4878389",
    "passport_assist_user": "CjwwBkqlNh_1aCmzwYSg2GMK_eKyTEW81YtER6DZYzSakMo0QwUU6xGUJq9VCZZpuE7Dg_fobXyKPWnCuugaSgo88OpPU2xfeSe55zxfg6jMWL4R-ze2EXvjo_-WWaROmRmqER4xcHqBxOFWJXKZ8TdZDnYtQunLbDvgbH9PEMb13Q0Yia_WVCABIgEDJyHz1w%3D%3D",
    "n_mh": "q2GsTtuMRTSCPgIYrhMiSsItf39_v7VemUMfqNX2w6E",
    "uid_tt": "35a27da0f8a9220804e0d0f3fecc7ca1",
    "uid_tt_ss": "35a27da0f8a9220804e0d0f3fecc7ca1",
    "sid_tt": "dc02d5f1172cb684c00a1798c36e06d8",
    "sessionid": "dc02d5f1172cb684c00a1798c36e06d8",
    "sessionid_ss": "dc02d5f1172cb684c00a1798c36e06d8",
    "is_staff_user": "false",
    "SelfTabRedDotControl": "%5B%5D",
    "store-region": "cn-bj",
    "store-region-src": "uid",
    "passport_csrf_token": "54c3c3a088c9f2161228926ef592f658",
    "passport_csrf_token_default": "54c3c3a088c9f2161228926ef592f658",
    "volume_info": "%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.032%7D",
    "sid_guard": "dc02d5f1172cb684c00a1798c36e06d8%7C1734939352%7C5184000%7CFri%2C+21-Feb-2025+07%3A35%3A52+GMT",
    "sid_ucp_v1": "1.0.0-KGRmNGQ1M2JhNDE5NmM2MWE2YWM4ZjA0YTdhMDAwMzIzZGYxZmNiM2MKGQj0kdTX2wIQ2KWkuwYY7zEgDDgGQPQHSAQaAmxmIiBkYzAyZDVmMTE3MmNiNjg0YzAwYTE3OThjMzZlMDZkOA",
    "ssid_ucp_v1": "1.0.0-KGRmNGQ1M2JhNDE5NmM2MWE2YWM4ZjA0YTdhMDAwMzIzZGYxZmNiM2MKGQj0kdTX2wIQ2KWkuwYY7zEgDDgGQPQHSAQaAmxmIiBkYzAyZDVmMTE3MmNiNjg0YzAwYTE3OThjMzZlMDZkOA",
    "is_dash_user": "1",
    "__security_mc_1_s_sdk_crypt_sdk": "8d1f4dad-4c86-8a32",
    "__security_mc_1_s_sdk_cert_key": "0195a182-419d-9cd2",
    "__security_mc_1_s_sdk_sign_data_key_web_protect": "e7c59749-4377-ae36",
    "strategyABtestKey": "%221736844400.831%22",
    "biz_trace_id": "b5da7b9a",
    "stream_player_status_params": "%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22",
    "stream_recommend_feed_params": "%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1440%2C%5C%22screen_height%5C%22%3A900%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A200%7D%22",
    "FOLLOW_NUMBER_YELLOW_POINT_INFO": "%22MS4wLjABAAAAk_4QS-crr1_ysHXvfHakXSFSJtordbjr9vE2ClzDYZk%2F1736870400000%2F0%2F1736845704440%2F0%22",
    "download_guide": "%223%2F20250114%2F0%22",
    "IsDouyinActive": "true",
    "home_can_add_dy_2_desktop": "%221%22",
    "FOLLOW_LIVE_POINT_INFO": "%22MS4wLjABAAAAk_4QS-crr1_ysHXvfHakXSFSJtordbjr9vE2ClzDYZk%2F1736870400000%2F0%2F1736850845634%2F0%22",
    "bd_ticket_guard_client_data": "eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTGMzQUVsclkvZmtIMSt5VnVyMG9DazZxTk1kK1hLODNOL2ZTRWNjVmhCelc4TkNOV21rTG9ncFg2anZtOVpkRGhUS1R0elorTEZBcit3bGxsYUxzRHc9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D",
    "publish_badge_show_info": "%220%2C0%2C0%2C1736850850397%22",
    "odin_tt": "e4fc14ed58c3b260f14795ab79c7a18760b6db2af3ed3e5a3345f01bbbd37167f428a491971874276e2678c4308db9d3697f367a5477ac4a1d82d3f35c2eae71"
}
url = "https://www-hj.douyin.com/aweme/v1/web/aweme/post/"
params = {

    "device_platform": "webapp",
    "aid": "6383",
    "channel": "channel_pc_web",
    "sec_user_id": "MS4wLjABAAAAYHFE1u4tgq29T8DQjiSaSWM77Ojh9HjOty66v8ISPjk",
    "max_cursor": "1710073014000",
    "locate_query": "false",
    "show_live_replay_strategy": "1",
    "need_time_list": "0",
    "time_list_query": "0",
    "whale_cut_token": "",
    "cut_version": "1",
    "count": "18",
    "publish_video_strategy_type": "2",
    "from_user_page": "1",
    "update_version_code": "170400",
    "pc_client_type": "1",
    "pc_libra_divert": "Mac",
    "version_code": "290100",
    "version_name": "29.1.0",
    "cookie_enabled": "true",
    "screen_width": "1440",
    "screen_height": "900",
    "browser_language": "zh-CN",
    "browser_platform": "MacIntel",
    "browser_name": "Chrome",
    "browser_version": "131.0.0.0",
    "browser_online": "true",
    "engine_name": "Blink",
    "engine_version": "131.0.0.0",
    "os_name": "Mac OS",
    "os_version": "10.15.7",
    "cpu_core_num": "8",
    "device_memory": "8",
    "platform": "PC",
    "downlink": "10",
    "effective_type": "4g",
    "round_trip_time": "200",
    "webid": "7416276412318402099",
    "uifid": "9e5c45806baed1121aef2e4ebdb50ae0783a7b9267143d29acaade7dde1bacd527b03a068a9abdb7833ae78af98d5b7b1a6dcfae23bc2e22a1e29b89a4771c8d672279a54a7b1986b5628f6af005121a444c6628e9c2f3f3a0b4fedec9d5a2e3c52e1ce4b3b733e6154bb4a45cec893a1752dc278450a5e023b52c54590762453af552ce3a185ddcab973f136395d0a8fe242b780cdd73439975f7b459b226a9dfb7283a61810ddad08b0df53c75e2ba132ea68f2f03e6e400cb53a3c4878389",
    "msToken": "jMke-iT3JHV-yzZxO7VL7uMhMUeisEqEsio9FEzP-9LbPsZWMmUVLmM3AqfuVETMdSFMXp0253QEGT1uoTR8xtJodww0T8iinIL8Q3V7mvyWVBAgvfwOn6VVEYENZ9SHepBWs8QdnX_RC-AkbQ1M2QXjCxGyNKXyDD3tB-G-j9xtQ5xNvFQ=",
    "a_bogus": "YfUnkwWLmxAVcdMtuCT0e31lUUg/NPSy8pTxStdPtOzMGh0bDmPmgxSpJxLA5o78qSpTwH5HixllbVdcOsXzZe9kFmkvSKtWkt59Ihmo0qwXbMvsEqfme0vzow0K8cTLaA9tils5As0r1dOlIr5sAddaC5FH-mRpRrMRdZYyyEWgfW8kho3wO9DpN6kT0ecX",
    "verifyFp": "verify_m3ph70u0_7v2IoMH6_IPIz_4n2h_9rSk_Mh7UYmPWMjdh",
    "fp": "verify_m3ph70u0_7v2IoMH6_IPIz_4n2h_9rSk_Mh7UYmPWMjdh"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
# 数据太长了 导致打印出现问题
# print(response.status_code)
# print('\n')
# print(response.text)
# print(response)
# print(json.loads(response.text))
# print(json.loads(response.text)['aweme_list'])
print(json.loads(response.text)['aweme_list'][0])