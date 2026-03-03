 const crypto_js = require('crypto-js')

//哈希算法加密   md5      sha     hmac
// 对称加密算法  ECB 不需要偏移量iv   CBC 需要偏移量iv（分组加密）       CFB 需要偏移量iv  OFB 需要偏移量iv  CTR 不需要偏移量iv

function des_encrypt(desKey, desIv, text) {
//加密  注意 Utf8 首字母要大写
    var key = crypto_js.enc.Utf8.parse(desKey)
    var vi = crypto_js.enc.Utf8.parse(desIv)
    var srcs = crypto_js.enc.Utf8.parse(text)

    encryted = crypto_js.AES.encrypt(srcs, key, {
        iv: vi,
        mode: crypto_js.mode.CBC,
        padding: crypto_js.pad.Pkcs7
    })

    return encryted.toString()
}

//解密
function des_de_encrypt(desKey, desIv, text) {
    var key = crypto_js.enc.Utf8.parse(desKey)
    var vi = crypto_js.enc.Utf8.parse(desIv)

    encryted = crypto_js.AES.decrypt(text, key, {
        iv: vi,
        mode: crypto_js.mode.CBC,
        padding: crypto_js.pad.Pkcs7
    })

    return encryted.toString(crypto_js.enc.Utf8)
}


console.log(des_encrypt('12345678', '12345678', 'python'));

console.log(des_de_encrypt('12345678', '12345678', 'TAYlDnSxC+U='));
