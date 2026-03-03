var CryptoJS = require('crypto-js')
var { ParamsSign } = require('./source')

// 使用解构赋值 var { ParamsSign } = require('./source') 直接导  文件大的时候用
  window.PSignCom = new ParamsSign({
            appId: "fb5df",
            preRequest: !1,
            onSign: function(e) {
                0 != e.code && oA.postDraData(704, "ParamsSign签名不可用", "ParamsSign", "code != 0", "", "")
            },
            onRequestTokenRemotely: function(e) {
                e.code,
                e.message
            },
            onRequestToken: function(e) {
                e.code,
                e.message
            }
        });
// console.log(window.PSignCom)
// console.log("-------------------------------------")


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
// console.log(paramsH5sign)
// console.log("-------------------------------------")
var result = window.PSignCom._$sdnmd(paramsH5sign);
console.log(result)
