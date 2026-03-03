import subprocess

import requests

# 异步请求需要通过sub来访问

# capture_output 允许控制台输出   text 输出方式为文本
# res = subprocess.run(['node', 'TestMethod.js'], capture_output=True, text=True, encoding='utf-8')
# print(res)
# print(res.stdout)


# 带参数访问    其实就是直接运行 整个 js  并不是运行某个方法
res = subprocess.run(['node', 'TestMethod.js','11','22'], capture_output=True, text=True, encoding='utf-8')
print(res)
print(res.stdout)

# 直接通过访问 接口方式获取异步结果
# getRes = requests.get('http://127.0.0.1:8000/async')
# print(getRes.text)