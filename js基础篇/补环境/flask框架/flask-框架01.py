# 开发框架
from flask import Flask

# 创建应用
app = Flask(__name__)


# 配置路由
@app.route("/s")
def hello():
    return 'hello world'


if __name__ == '__main__':
    # 启动
    app.run()
