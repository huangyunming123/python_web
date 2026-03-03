import hashlib
from selenium import webdriver


def hmac_data(aa):
    # sha1 = hashlib.sha1()
    # sha1.update(aa.encode())
    # print(sha1.hexdigest())

    hmac = hashlib.pbkdf2_hmac()
    hmac.update(aa.encode())
    print(hmac.hexdigest())


hmac_data('python')
print(len('1'))
