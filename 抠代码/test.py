import execjs

# 生成对应的js运行环境
node = execjs.get()
print(node)
with open('../js基础篇/js/demo1.js', encoding='utf-8') as f:
    js_code = f.read()

# 创建js环境
js = execjs.compile(js_code)

# 两种调用js的方法

# res = js.call('aa', 123)
# print(res)

res = js.eval('getData(123)')
print(res)

'''
pyExcelJS 是一个在python 上执行js 的库  底层是对js 运行环境的封装
pip install pyexecjs 



'''