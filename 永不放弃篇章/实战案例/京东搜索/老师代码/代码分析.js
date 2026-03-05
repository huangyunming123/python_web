require('./source_code')
var crypto_js = require('crypto-js')

const time = new Date().getTime()
const paramsH5sign = {
    appid: 'search-pc-java',
    functionId: "pc_search_searchWare",  // 固定值(操作系统的不同可能导致获取到的值不同)
    client: 'pc',
    clientVersion: '1.0.0',
    t: time,
}

var params = {
    "enc": "utf-8",
    "pvid": "ecd79c13d7dd458ab8293861ceb70f6a",
    "area": "1_72_55653_0",
    "page": 3,
    "new_interval": true,
    "s": 49
}

paramsH5sign['body'] = crypto_js.SHA256(JSON.stringify(params))
// paramsH5sign['body'] = crypto_js.SHA256(JSON.stringify(params)).toString()
// console.log(paramsH5sign)

// ParamsSign类在source_code文件中
window.PSignCom = new ParamsSign({
    appId: "fb5df",
    preRequest: !1,
    onSign: function (t) {
        0 != t.code && K.O.postDraData(704, "ParamsSign签名不可用", "ParamsSign", "code != 0", "", "")
    },
    onRequestTokenRemotely: function (t) {
        t.code,
            t.message
    },
    onRequestToken: function (t) {
        t.code,
            t.message
    }
});

var result = window.PSignCom._$sdnmd(paramsH5sign);
console.log(result);
