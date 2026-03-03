import websocket


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("close###")


def on_open(ws):
    print("open...")


if __name__ == '__main__':
    ws_app = websocket.WebSocketApp(url='', header='',cookie='', on_message=on_message(), on_error=on_error(),
                                    on_close=on_close(), on_open=on_open())

    # 保持长连接
    ws_app.run_forever()
