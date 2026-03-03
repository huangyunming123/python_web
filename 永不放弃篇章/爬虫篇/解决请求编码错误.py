import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

# 用来解决请求时候报错