from flask import Flask, jsonify

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def driver_dd():
    option = webdriver.ChromeOptions();
    # 无痕模式
    option.add_argument('headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
    driver.get('http://localhost:63344/python_web/js%E5%9F%BA%E7%A1%80%E7%AF%87/%E8%A1%A5%E7%8E%AF%E5%A2%83/%E8%87%AA%E5%8A%A8%E5%8C%96%E8%A1%A5%E7%8E%AF%E5%A2%83/test.html?_ijt=2o5h5jnpm4oqrcbibhpjn180ap')
    return driver

dd = driver_dd()
app = Flask(__name__)

@app.route('/d')
def hello():
    return jsonify(context={'v':dd.execute_script('return window.aaa()')})


if __name__ == '__main__':
    app.run()
