var crypt = require('crypto-js')


function getMD5() {
    var r = Date.now().toString()
    var e = crypt.MD5((r + "9527" + r.substr(0, 6)))
    return [r,e.toString()];
}

console.log(getMD5());

