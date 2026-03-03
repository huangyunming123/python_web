# subprocess  请求 js 异步消息
import subprocess

# 只能获取打印的结果
sign = subprocess.run(['node', 'scrape-center.js', str(1 * 10)], capture_output=True, text=True, encoding='utf-8')
# 打印控制台结果 去掉前后空格
print(sign.stdout.strip())