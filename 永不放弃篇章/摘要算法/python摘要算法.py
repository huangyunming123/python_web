import hashlib
import hmac


def md5(data):
    md5 = hashlib.md5()
    md5.update(data.encode())
    return md5.hexdigest()


print('md5加密 = ' + md5('hello 我是32位加密'))


def hmac_md5(data):
    # 需要传递字节数据
    key = '12345'.encode()
    content = data.encode()
    hmac_md5 = hmac.new(key, content, digestmod='md5')
    return hmac_md5.hexdigest()


print('hmac_md5散列加密 = ' + hmac_md5('hello 我是32位加密 随着算法变动'))


def sha1(data):
    sha1 = hashlib.sha1()
    sha1.update(data.encode())
    return sha1.hexdigest()


print('sha1加密 = ' + sha1('hello 我是40位加密'))
