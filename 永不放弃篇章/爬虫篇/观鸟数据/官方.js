var CryptoJS = require('crypto-js')
window = this
var JSEncrypt = require('jsencrypt')


function getUuid() {
    var s = [];
    var a = "0123456789abcdef";
    for (var i = 0; i < 32; i++) {
        s[i] = a.substr(Math.floor(Math.random() * 0x10), 1)
    }
    s[14] = "4";
    s[19] = a.substr((s[19] & 0x3) | 0x8, 1);
    s[8] = s[13] = s[18] = s[23];
    var b = s.join("");
    return b
}

beforeSend = function (key) {
    var paramPublicKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCvxXa98E1uWXnBzXkS2yHUfnBM6n3PCwLdfIox03T91joBvjtoDqiQ5x3tTOfpHs3LtiqMMEafls6b0YWtgB1dse1W5m+FpeusVkCOkQxB4SZDH6tuerIknnmB/Hsq5wgEkIvO5Pff9biig6AyoAkdWpSek/1/B7zYIepYY0lxKQIDAQAB";
    var encrypt = new JSEncrypt();
    encrypt.setPublicKey(paramPublicKey);
    var c = Date.parse(new Date());
    var d = getUuid();
    var e = key;
    b = encrypt.encrypt(e);
    // console.log(b)
    var f = CryptoJS.MD5(e + d + c).toString();

    return {
        "timestamp": c,
        'requestId': d,
        'sign': f,
        'data': b
    }
}

decode = function (a) {
    var key = "C8EB5514AF5ADDB94B2207B08C66601C";
    var iv = "55DD79C6F04E1A67"
    var b = CryptoJS.enc.Utf8.parse(key);
    var c = CryptoJS.enc.Utf8.parse(iv);
    var d = CryptoJS.AES.decrypt(a, b, {
        iv: c,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return d.toString(CryptoJS.enc.Utf8)
}


console.log(beforeSend('{"limit":"20","page":"1"}'));



