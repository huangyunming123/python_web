var CryptoJS = require('crypto-js')
require('./source')
var params = {
    "enc": "utf-8",
    "area": "1_72_55652_0",
    "page": 4,
    "mode": null,
    "concise": false,
    "new_interval": true,
    "s": 70
}

const time = new Date().getTime()

const paramsH5sign = {
    appid: 'search-pc-java',
    functionId: "pc_search_searchWare",
    client: 'pc',
    clientVersion: '1.0.0',
    t: time,
}

if (params) {
    paramsH5sign['body'] = CryptoJS.SHA256(JSON.stringify(params))
}
console.log(paramsH5sign)

 window.PSign.sign(paramsH5sign)