import requests
import json


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Authorization": "59hK4WsuV1TR8haZPHfsze2BE9m/fGCUB3P1BnPa/hjEWM066k+VTr1lmztVCjOMyb5BzesJgjobCjZCOKnb35Z7c/cbFIgo0z3KhZ4MH9vAVBoiCZIG/JWWRx3RoovJJBSTjDj7vWJLMDvMNz5Z0K9pKNZF+ENbGW5LC8Fh2XidWHZQbjbTBp5SE1MtLqMhDtmlIjPm/qGH7myzomAHCm22+i+o7TPkkJom3krg++w=",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://www.beeselect.net",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
    "applicationCode": "6",
    "businessType": "2",
    "enterpriseId": "a99b843431ae48c39cd541743417f10f",
    "platform": "0",
    "sec-ch-ua": "\"Chromium\";v=\"146\", \"Not-A.Brand\";v=\"24\", \"Google Chrome\";v=\"146\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
cookies = {
    "HWWAFSESID": "8ce3373522de5b3e61",
    "HWWAFSESTIME": "1749460621842",
    "13466786708": "400",
    "13793666298": "200",
    "MEIQIA_TRACK_ID": "2eo1SyQeBIwPPHCOM6ZAOd6ElMZ",
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%22Gsr1xqrr%22%2C%22first_id%22%3A%2219785de0d8514ac-0b07ddb9e842dc8-1c525636-1484784-19785de0d86205b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfbG9naW5faWQiOiJHc3IxeHFyciIsIiRpZGVudGl0eV9jb29raWVfaWQiOiIxOTc4NWRlMGQ4NTE0YWMtMGIwN2RkYjllODQyZGM4LTFjNTI1NjM2LTE0ODQ3ODQtMTk3ODVkZTBkODYyMDViIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22Gsr1xqrr%22%7D%2C%22%24device_id%22%3A%2219785de0d8514ac-0b07ddb9e842dc8-1c525636-1484784-19785de0d86205b%22%7D",
    "PlatVisitCount": "aFUrRm1iU2Z1N0lNSEZtTzdMWlM0WFg4dUJjL0J5dUo4M1BPYzNYaXhCTT0=",
    "ASP.NET_SessionId": "hq32csb3wghm2qmplzuc1wtq",
    "allAccount": "[{\"phone\":\"18600340733\",\"token\":\"59hK4WsuV1TR8haZPHfsze2BE9m/fGCUB3P1BnPa/hjEWM066k+VTr1lmztVCjOMyb5BzesJgjobCjZCOKnb35Z7c/cbFIgo0z3KhZ4MH9vAVBoiCZIG/JWWRx3RoovJJBSTjDj7vWJLMDvMNz5Z0K9pKNZF+ENbGW5LC8Fh2XidWHZQbjbTBp5SE1MtLqMhDtmlIjPm/qGH7myzomAHCm22+i+o7TPkkJom3krg++w=\"},{\"phone\":\"15204697356\",\"token\":\"59hK4WsuV1TR8haZPHfsze2BE9m/fGCUB3P1BnPa/hjEWM066k+VTr1lmztVCjOM62JYmMA8RhD2lh+d+myo+v++cuXXpAonnMcoxLgkG2zBOmWCS8gy7KuvZGgm27/OP+DTGb4Xw5VAMYs5ft3pjyoab6xQE/mShqP4NfUPVKxCKyQJdB6Z7wTOIjr76WS9gxK6foBVC7XP0hYkWzwfiZ/s6WWCiN5sXu9unwxm5sc=\"},{\"phone\":\"17710049039\",\"token\":\"59hK4WsuV1TR8haZPHfsze2BE9m/fGCUB3P1BnPa/hjEWM066k+VTr1lmztVCjOMwYmMC5UhITwe5H/YJI/2AtQH36dZTfq5cpiQxdNQPQkPijxQC/q/GEePsVJIAoL/tjooei4X7lwEWoAkLzEwQOjtfzOLrCLuoYSgU0YqCDtEcGvQWGlvPOhmr+YXeSGCAyaj1YKkRYK3eNmzxMkUTJ9N+8vhqHk597HlLndiSg0=\"},{\"phone\":\"13466786708\",\"token\":\"59hK4WsuV1TR8haZPHfsze2BE9m/fGCUB3P1BnPa/hjEWM066k+VTr1lmztVCjOMqkb3E0xaZiKTkW38I7qiAmfnJPk+RsS9tjDj1VcW6GPxIlU6FPy8T9Wi2wKJcdCntBgk34wPmjCtWoEFm4vnac0BF2LAX5sLkjST5NzMj9++kaR75G6T7Xz3nzksQknsua0BpPjEtBZrYmmBLJYVwWE3ELJ8ONykITBDlVjny6g=\"},{\"phone\":\"15936934685\",\"token\":\"59hK4WsuV1TR8haZPHfsze2BE9m/fGCUB3P1BnPa/hjEWM066k+VTr1lmztVCjOM6GTTGiB3lO+ohucJaGGLeStofmoz4PkztvJxpI7PLH8WDrHAL3A38ZjXS0reC9OMc5/4ZhDVhxS+TgwQpiQCsAZP3w5X6x6i6JpjRSJ2XVwHbDQdPIIH7VA4UtWBRjRqum5Of1sfcnZD8nFnIPbnMkm3UzxhjOxaBlqZSzKkf54=\"},{\"phone\":\"13793666298\",\"token\":\"59hK4WsuV1TR8haZPHfsze2BE9m/fGCUB3P1BnPa/hjEWM066k+VTr1lmztVCjOM5Mb48xAZDujfcBozb8bzvo2NLiIO6isApEVdwQBNS+xLvY+XmMf0Vhmfl3rWMbhDUJAxm0UxsBCz+gb3Oadp31RmlN7xk1aBSXSt5ZYQ1j1DJx0aVJ13wzPgEqwkUXkz3TpFONq+kySGvZeYOMGmUs/5+pOp6sPrjty0p/ucB8w=\"},{\"phone\":\"18742030191\",\"token\":\"59hK4WsuV1TR8haZPHfsze2BE9m/fGCUB3P1BnPa/hjEWM066k+VTr1lmztVCjOMQDxbWQKdp47gktDrrbBvQgOwqQpmDoxsmtF8m1X6lbnbIDaKG0VXOooziiZuBotdNlLNayB4QTy4VuCgpFxRw9H0UNTLe5i1FkYv6O9I7zgQmSGs69gx5AbHe2eaHP8weglM+XHmgak7kvMGrQomEXpvAh3Sf+LST8S3nmP90YE=\"},{\"phone\":\"15086660521\",\"token\":\"59hK4WsuV1TR8haZPHfsze2BE9m/fGCUB3P1BnPa/hjEWM066k+VTr1lmztVCjOM60HS3Zs7fxeM57iMlWitXeE0OeDpgffxZ1FvBuCQGZolj9sZbjanVcBk5QTThmFMuhiL3NnPieOX/WJXPgA/gai/pkZPg1rCPk7MwkytgaFxDbMaJ0+lTU9/BQ+Svv3Imz2frV+W7uGxvR3AnEvP27ibGaxA5qU0T48YAHa2JWI=\"},{\"phone\":\"15810572405\",\"token\":\"59hK4WsuV1TR8haZPHfsze2BE9m/fGCUB3P1BnPa/hjEWM066k+VTr1lmztVCjOMtbfyrkZ5tAtzyEdVeuQZ3YQHp249ktyzHJD4lNEMURUl4drYnLTe5+h+tA+5NTa/S5UkKSEWpIHx0veqvtnaLDa81Z04mWEev6R++nz1vOonw0NE4dFzJhk3KqL7Def4uNthfv6YBL2MWOU0PhtnFTvLWpxja2adTUAQMo+PeDs=\"}]",
    "Himall-User": "59hK4WsuV1TR8haZPHfsze2BE9m/fGCUB3P1BnPa/hjEWM066k+VTr1lmztVCjOMyb5BzesJgjobCjZCOKnb35Z7c/cbFIgo0z3KhZ4MH9vAVBoiCZIG/JWWRx3RoovJJBSTjDj7vWJLMDvMNz5Z0K9pKNZF+ENbGW5LC8Fh2XidWHZQbjbTBp5SE1MtLqMhDtmlIjPm/qGH7myzomAHCm22+i+o7TPkkJom3krg++w=",
    "113ae933-ff58-412f-890f-6314fe26e549": "8ef7940be401d7dcd825b0d1b5445c83",
    "Scmmall-Shop": "3473",
    "Scmmall-enterpriseId": "a99b843431ae48c39cd541743417f10f"
}
url = "https://www.beeselect.net/tenant/api/fc/category/resend"
data = {
    "orderIds": [
        "1713853150789635"
    ],
    "pushType": 1
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)