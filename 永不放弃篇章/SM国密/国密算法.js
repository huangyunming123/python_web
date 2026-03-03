// 终端输入     npm install sm-crypto --save
//  sm2 椭圆加密  非对称

//
// SM1	对称（分组）加密算法	芯片	分组长度、密钥长度均为 128 比特
// SM2	非对称（基于椭圆曲线 ECC）加密算法	数据加密	ECC 椭圆曲线密码机制 256 位，相比 RSA 处理速度快，消耗更少
// SM3	散列（hash）函数算法	完整性校验	安全性及效率与 SHA-256 相当，压缩函数更复杂
// SM4	对称（分组）加密算法	数据加密和局域网产品	分组长度、密钥长度均为 128 比特，计算轮数多
// SM7	对称（分组）加密算法	非接触式 IC 卡	分组长度、密钥长度均为 128 比特
// SM9	标识加密算法（IBE）	端对端离线安全通讯	加密强度等同于 3072 位密钥的 RSA 加密算法
// ZUC	对称（序列）加密算法	移动通信 4G 网络	流密码

sm2 =  require('sm-crypto').sm2

var generateKeyPairHex = sm2.generateKeyPairHex();

var privateKey = generateKeyPairHex.privateKey;
var publicKey = generateKeyPairHex.publicKey;

console.log(sm2.doEncrypt("123456", publicKey));

console.log(sm2.doDecrypt(sm2.doEncrypt("123456", publicKey), privateKey));