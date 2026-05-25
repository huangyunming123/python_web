# 生成器测试

def gen():
    int_value = 0
    while True:
        aaa = yield int_value
        int_value += 1
        print(aaa,"-----")

g = gen()
print(next(g))

print(g.send("hello"))

print(next(g))

