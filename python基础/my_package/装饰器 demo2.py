"""
函数 make_power(n) 返回一个新函数，该新函数接收参数 x，返回 x 的 n 次方。
"""
def make_power(n):
    def power(x):
        return x ** n
    return power


power = make_power(2)

print(power(3))