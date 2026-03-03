# 关键包
import execjs

js_code = """
function run_func(arg){
return arg
}
"""
#1 环境检测  获取 node 环境
print(execjs.get())
#2 编译代码
compile_code = execjs.compile(js_code)
#3 方法一  call
print( compile_code.call('run_func',33))

#4 方法二  eval  带参数
print( compile_code.eval('run_func(22)'))

import time

print(int(time.time()*1000))
