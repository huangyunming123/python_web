"""
# 定义装饰器
def outer(func):
    def inner():
        print("执行前")
        func()   # 执行原函数
        print("执行后")
    return inner

# 使用装饰器  把 say 丢给装饰器进行代理后 此处的 say 相当于 outer 方法的返回值
@outer
def say():
    print("Hello")

# 注解等价于
# outer(say)()
"""
# 带参数的装饰器
"""def outer(func):
    def inner(a,b):
        print("开始计算")
        return func(a,b)
    return inner

# @outer
def add(x,y):
    return x+y

# print(add(1,2))
# 等同于
print(outer(add)(1, 2))
"""

def deco(func):
    print("我在装饰了")
    return func

@deco
def test():
    print("调用test")
# 运行这里直接打印：我在装饰了（定义就执行）

test() # 调用才走内部


