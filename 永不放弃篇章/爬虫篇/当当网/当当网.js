
const {RSAKeyPair,encryptedString} = require('./RSA')

const {setMaxDigits} = require('./BigInt')

const a= require('./BigInt')

console.log(a)
setMaxDigits(130);
var PublicExponent = "10001";
var modulus = "be44aec4d73408f6b60e6fe9e3dc55d0e1dc53a1e171e071b547e2e8e0b7da01c56e8c9bcf0521568eb111adccef4e40124b76e33e7ad75607c227af8f8e0b759c30ef283be8ab17a84b19a051df5f94c07e6e7be5f77866376322aac944f45f3ab532bb6efc70c1efa524d821d16cafb580c5a901f0defddea3692a4e68e6cd";
var key = new RSAKeyPair(PublicExponent, "", modulus);
var arg = 'admin123'
let encryptedString1 = encryptedString(key, arg);
console.log(encryptedString1)
console.log('61524a416ac10c4d1cda89edc332ded9a4f4224aff16edeb333d9bb03aa3530479d4b7922cdcf5cd15bbf57dc640b3ff131469a115a046fdbf7934b65db7937adcb05eb91b59b14cd14cb4a596cabedb77cf9ac9b48ad32d85fe46316fff9944c8e36b300f6fdcf7761de86fa3f800c81271181ee7e725e5d237d0a96c00e54b')