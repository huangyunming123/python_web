/***

 npm install node-rsa --save
 require('node-rsa')
 // crypto-js   无法生成私钥 所以 用node-rsa




     密文长度   大约 有的场景
RSA  DSA ECDSA   密文长度

     88位
     172位
     344位


 new JSEncrypt() JSEncrypt 等 一般会使用 JSEncrypt库，会有 new 一个实例对象的操作
 setPublicKeysetKeysetPrivateKeygetPublicKey 等，一般实现的代码里都含有设置密钥的过程
 */

var NodeRSA = require('node-rsa')

function rsaEncrypt() {
    pubKey = new NodeRSA(publicKey, 'pkcs8-public');
    var encryptedData = pubKey.encrypt(text, 'base64');
    return encryptedData
}

function rsaDecrypt() {
    priKey = new NodeRSA(privatekey, 'pkcs8-private');
    var decryptedData = priKey.decrypt(encryptedData, 'utf8');
    return decryptedData
}

var key = new NodeRSA({b:512});                    //生成512位秘钥
var publicKey = key.exportKey('pkcs8-public');    //导出公钥
var privatekey = key.exportKey('pkcs8-private');  //导出私钥
var text = "I love Python!"

var encryptedData = rsaEncrypt()
var decryptedData = rsaDecrypt()

console.log("公钥:\n", publicKey,publicKey.length)
console.log("私钥:\n", privatekey,privatekey.length)
console.log("加密字符串: ", encryptedData)
console.log("解密字符串: ", decryptedData)