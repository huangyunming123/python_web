import hashlib


def sha_data(aa):
    # sha1 = hashlib.sha1()
    # sha1.update(aa.encode())
    # print(sha1.hexdigest())

    sha1 = hashlib.sha512()
    sha1.update(aa.encode())
    print(sha1.hexdigest())

sha_data('python')
print(len('ecc579811643b170cbd88fd0d0e323d1e1acc7cef8f73483a70abea01a89afa8015295f617f27447ba05e928e47a0b3a46dc79e72f99d1333856e23eeff97d8b'))


