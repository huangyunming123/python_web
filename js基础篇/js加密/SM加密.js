var sm = require('sm-crypto')

aa = require('./SM_demo')
// console.log(aa.bbb(1231))

let generateKeyPairHex = sm.sm2.generateKeyPairHex();
console.log(generateKeyPairHex)
let publicKey = generateKeyPairHex.publicKey;
let privateKey = generateKeyPairHex.privateKey;

var key = sm.sm2.doEncrypt('python',publicKey)
console.log(key)
var deKey = sm.sm2.doDecrypt(key,privateKey)
console.log(deKey)

var k3 = sm.sm3('python')

console.log(k3)
