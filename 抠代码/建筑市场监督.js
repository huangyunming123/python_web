var crypt = require('crypto-js')


function getData(t) {
    let key = crypt.enc.Hex.parse(t)
    let n = crypt.enc.Base64.stringify(key)
    let m = crypt.enc.Utf8.parse("0123456789ABCDEF");
    let f = crypt.enc.Utf8.parse("Dt8j9wGw%6HbxfFn");
    let a = crypt.AES.decrypt(n, f, {
        iv: m,
        mode: crypt.mode.CBC,
        padding: crypt.pad.Pkcs7
    })
    let r = a.toString(crypt.enc.Utf8);
    return r;
}




// throw new Error('Malformed UTF-8 data');
// 	                报错这个的话 秘钥不对