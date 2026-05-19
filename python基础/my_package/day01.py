# import re
#
# text = "折扣 20%"
# mo = re.search(r"(\d+)%", text)
# if mo:
#     discount = float(mo.group(1)) / 100
#
#

import re
# 海象运算符   mo 变量不需要单独声明了
text = "折扣 20%"
if mo := re.search(r"(\d+)%", text):
    discount = float(mo.group(1)) / 100

print(mo)
