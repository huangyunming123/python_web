"""class Deco:
    def __call__(self,func):
        def inner():
            print("类装饰器")
            func()
        return inner

@Deco()
def test():
    print("运行")
"""

class MyDecorator:
    # 1. 初始化：接收装饰器参数（无参可省略）
    def __init__(self):
        print("创建装饰器实例---执行 run 之前就已经执行了1")

    # 2. 核心：拦截被装饰函数
    def __call__(self, func):
        print("拦截被装饰函数---执行 run 之前就已经执行了2")
        def wrapper(*args, **kwargs):
            # 执行前逻辑
            print("类装饰器前置逻辑")
            res = func(*args, **kwargs)
            # 执行后逻辑
            print("类装饰器后置逻辑")
            return res
        print("返回被装饰函数---执行 run 之前就已经执行了3")
        return wrapper

@MyDecorator()
def run(xxx):
    print("执行",xxx)

