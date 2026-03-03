from datetime import datetime

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