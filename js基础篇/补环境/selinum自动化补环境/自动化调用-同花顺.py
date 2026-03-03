import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

pro_dir = os.path.dirname(os.path.abspath(__file__))
print(pro_dir)


def get_cookie():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # 使用file://协议加载本地文件
    # 这个文件就是把加密模块直接复制过来的
    file_path = os.path.join(pro_dir, "自动化补环境-同花顺.html")
    print(file_path)
    file_url = f"file://{file_path}"
    driver.get(file_url)
    res = driver.execute_script("return window.aaa()")
    print('cookies = ', res)
    # input("输入任意结束")


get_cookie()
