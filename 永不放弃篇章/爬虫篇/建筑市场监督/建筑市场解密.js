// Error: Malformed UTF-8 data  一般是秘钥错误了


let crypt = require('crypto-js')

d = {
    a: crypt
}
// f = d.a.enc.Utf8.parse("jo8j9wGw%6HbxfFn")
f = d.a.enc.Utf8.parse("Dt8j9wGw%6HbxfFn");
m = d.a.enc.Utf8.parse("0123456789ABCDEF");
function b(t) {
    var e = d.a.enc.Hex.parse(t)
        , n = d.a.enc.Base64.stringify(e)
        , a = d.a.AES.decrypt(n, f, {
        iv: m,
        mode: d.a.mode.CBC,
        padding: d.a.pad.Pkcs7
    })
        , r = a.toString(d.a.enc.Utf8);
    return r.toString()
}