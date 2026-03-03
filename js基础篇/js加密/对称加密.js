var crypt = require('crypto-js')

function enc() {

    let key = crypt.enc.Utf8.parse('12345678')
    let iv = crypt.enc.Utf8.parse('12345678')
    let data = crypt.enc.Utf8.parse('python')
    // let key = '12345678'
    // let iv = '12345678'
    // let data = 'python'
    let aa = crypt.AES.encrypt(data, key,
        {
            iv: iv,
            mode: crypt.mode.CBC,
            padding: crypt.pad.Pkcs7 //补位操作
        })
    return aa.toString();
}

function dec(data) {
    let key = crypt.enc.Utf8.parse('12345678')
    let iv = crypt.enc.Utf8.parse('12345678')
    aa = crypt.AES.decrypt(data, key,
        {
            iv: iv,
            mode: crypt.mode.CBC,
            padding: crypt.pad.Pkcs7 //补位操作
        })
    return aa.toString(crypt.enc.Utf8);
}

console.log(enc());
console.log(dec(enc()))
