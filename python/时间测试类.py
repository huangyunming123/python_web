from datetime import datetime
from typing import Iterable

# 获取当前日期和时间
now = datetime.now()
print(now)  # 输出格式：2025-08-15 15:30:45.123456

# 格式化输出
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 输出格式：2025-08-15 15:30:45

# 只获取日期
today = datetime.now().date()
print(today)  # 输出格式：2025-08-15

# 只获取时间
current_time = datetime.now().time()
print(current_time)  #

# try:
#     a = 10 / 0
# except :
#     print("除数不能为零")
#     raise Exception("除数不能为零")
# finally:
#     print("无论是否发生异常，都会执行的代码")

# list = [12,32,3]
# print(isinstance(list, Iterable))
#
# iter__ = list.__iter__()
# print(iter__)

range_ = [i for i in range(5)]
print(range_)

in_range_ = (i for i in range(5))
print(in_range_)

print(isinstance(in_range_, Iterable))
print(isinstance(range_, Iterable))
list = [1,2,3]
arr = (1,2,3)
print(isinstance(list, Iterable))
print(isinstance(arr, Iterable))

iterator = iter(list)
print(isinstance(iterator, Iterable))

