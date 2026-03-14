import execjs

js_data = '''

function aa(t1,t2){
return t1+t2
}
'''
js = execjs.compile(js_data)
# res = js.call('aa')
# print(res)

js_eval = js.eval('aa(21)')
print(js_eval)

call_res = js.call('aa', [312, 313])
print(call_res)

js_code = ''
with open('../js基础篇/js/demo1.js', encoding='utf-8') as f:
    js_code = f.read()
    aaMethod = execjs.compile(js_code)
    call = aaMethod.call('aa', 1,2)
    print(call)
print(js_code)
