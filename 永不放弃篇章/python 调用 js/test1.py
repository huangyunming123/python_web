import execjs

with open('TestMethod.js', 'r',encoding='utf-8') as f:
    js_code = f.read()
    js = execjs.compile(js_code)
    res = js.call('run_add_array',[1,2,3])
    print(res)

# python 无法调用 js 的异步函数    
with open('TestMethod.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
    js = execjs.compile(js_code)
    res = js.call('async')
    print(res)

