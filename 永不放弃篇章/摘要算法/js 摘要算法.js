// npm install crypto-js --save   注意需要 到当前目录下去下载
const cryptoJS = require('crypto-js');


function md5(str) {
    return cryptoJS.MD5(str).toString();
}

console.log(md5('hello  我是32位加密'));


function hmac_md5(str, key){
    return cryptoJS.HmacMD5(str, key).toString();
}

console.log(hmac_md5('hello  我是32位加密', '123'));
