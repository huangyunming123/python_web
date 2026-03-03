import asyncio

import requests
import websockets









headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://jzsc.mohurd.gov.cn/data/company?complexname=",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "accessToken;": "",
    "sec-ch-ua": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "timeout": "30000",
    "v": "231012"
}
cookies = {
    "Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c": "1769479629",
    "Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c": "1769479629",
    "HMACCOUNT": "F9080EB0E616319B"
}
url = "https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list"






async def echo(websocket):
    # 使用WebSocket在客户端和服务器之间建立全双工双向连接后，就可以在连接打开时调用send()方法。
    for i in range(0,3):
        params = {
            "pg": "{}".format(i),
            "pgsz": "15",
            "total": "0"
        }
        message = requests.get(url, headers=headers, cookies=cookies, params=params)
        # 发送数据
        await websocket.send(message.text)
    return True


async def recv_msg(websocket):
    while 1:
        # 接收数据
        recv_text = await websocket.recv()
        print(recv_text)


async def main_logic(websocket, path):
    await echo(websocket)
    await recv_msg(websocket)



'''
    websocket 启动
'''
start_server = websockets.serve(main_logic, '127.0.0.1', 8080)
loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
# 创建了一个连接对象之后，需要不断监听返回的数据，则调用 run_forever 方法，要保持长连接即可
loop.run_forever()






