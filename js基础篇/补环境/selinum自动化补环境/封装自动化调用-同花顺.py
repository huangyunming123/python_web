import os

from flask import Flask
from selenium import webdriver

pro_dir = os.path.dirname(os.path.abspath(__file__))

def get_cookie():
    # 设置屋头浏览器
    op = webdriver.ChromeOptions()
    op.add_argument("--headless")
    driver = webdriver.Chrome(options=op)
    file_path = os.path.join(pro_dir, "自动化补环境-同花顺.html")
    print(file_path)
    file_url = f"file://{file_path}"
    driver.get(file_url)
    return driver
    # res = driver.execute_script("return window.aaa()")
    # print('cookies = ', res)
    # input("输入任意结束")

app = Flask(__name__)
cookie = get_cookie()

@app.route('/get_cookie')
def getCookie():
    res = cookie.execute_script('return window.aaa()')
    return res

if __name__ == '__main__':
    app.run()
