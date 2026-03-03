#pip install curl-cffi
from curl_cffi import requests

# 跟床头的request 一样可以请求接口 但是对有指纹验证的浏览器（有浏览器版本要求的） 则需要用这个
res = requests.get('https://www.baidu.com',impersonate='chrome110')
print(res)


'''
创建一个 Session 对象，用于管理 HTTP 会话。Session 可以保持 Cookie、连接池等状态，适合需要多次请求的场景。
get = session.get
'''
session = requests.Session()
get = session.get('https://www.baidu.com')
