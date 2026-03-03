# python 加密需要用  install  gmssl

# 没有自动生成 公钥私钥

# privateKey: 'cda5142173c6fb40529c4f0e33a5c0b6e68a55558305c6fef01f4e24eae08eae',
# publicKey: '046dc4bae432b48fd3dc79499589190a6e2d3f8bb2c643287322b8e8000c729157a47ae511bd437ff7db135f3382f209ab46a9ea2164b4594fbde134196ad98c38'

# from gmssl import sm2
#
# privateKey = '3c1ee6ef74e698ec2c967f4b8db3376d6696779ea372ed64df7912d94e7bc9f9',
# publicKey = '04573dab3f40a285a2e77f4465ed54c40f72d2e17f5b0f13151c4ed8e58ee2694062e16fc7c0e0db478f876be8038b6b08592596f5b6104b8d59cd00ebc3a1ebf1'
#
# # 带加密数据 和加密后的都是 byte 类型
# sm_crypt2 = sm2.CryptSM2(public_key=publicKey, private_key=privateKey)
#
# data = b"this is python"
#
# enc = sm_crypt2.encrypt(data)
# dec = sm_crypt2.decrypt(enc)
#
# print('enc = ', enc.hex())
# print('dec = ', dec)
