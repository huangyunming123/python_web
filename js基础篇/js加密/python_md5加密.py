import hashlib


def get_md5():
    md_5 = hashlib.md5()
    update = md_5.update('python'.encode())
    # 获取md5 数据
    print(md_5.hexdigest())
get_md5()