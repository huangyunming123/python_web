import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

'''
https://www.cnblogs.com/mt-loading/p/18530462
解决 谷歌浏览器版本太高  webdriver 版本找不到
'''

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(r'http://localhost:63344/python_web/js%E5%9F%BA%E7%A1%80%E7%AF%87/%E8%A1%A5%E7%8E%AF%E5%A2%83/%E8%87%AA%E5%8A%A8%E5%8C%96%E8%A1%A5%E7%8E%AF%E5%A2%83/test.html?_ijt=2o5h5jnpm4oqrcbibhpjn180ap')
# driver.get('jetbrains://pycharm/navigate/reference?project=python_web&path=js基础篇/补环境/自动化补环境/qqq.html')
# time.sleep(25)
print(driver.execute_script('return window.aaa()'))