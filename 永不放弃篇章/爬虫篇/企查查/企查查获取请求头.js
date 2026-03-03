let crypt_js = require('crypto-js')


function o_default() {
    var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
        , t = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
        , n = JSON.stringify(e).toLowerCase();

    return encrypt(t + n, o1_default(t)).toLowerCase().substr(8, 20)
}

function s_default() {
    var list = ["w", "i", "n", "d", "o", "w", ".", "t", "i", "d"];
    return eval(list.join(""))

}


function o1_default() {
    for (var e = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase(), t = e + e, n = "", i = 0; i < t.length; ++i) {
        var o = t[i].charCodeAt() % 20;
        n += codes[o]
    }
    return n
}

function r_default() {
    var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
        , t = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : ""
        , n = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
        , i = JSON.stringify(e).toLowerCase();
    return encrypt(n + "pathString" + i + t,
        o1_default(n))
}


function encrypt(e, t) {
    return crypt_js.HmacSHA512(e, t).toString()
}

codes = {
    "0": "W",
    "1": "l",
    "2": "k",
    "3": "B",
    "4": "Q",
    "5": "g",
    "6": "f",
    "7": "i",
    "8": "i",
    "9": "r",
    "10": "v",
    "11": "6",
    "12": "A",
    "13": "K",
    "14": "N",
    "15": "k",
    "16": "4",
    "17": "L",
    "18": "1",
    "19": "8"
}
window = {
    'pid': '5e8f2dde6ce30b8c133e416ec9f41ef9',
    'tid': '9c3c89c47b0d71b65b5176683bbc3c89'
}


function getKey(data,t) {
    return o_default(t, data)
}

function getValue(data,t){
    return r_default(t, data, s_default())
}




// var t = '/api/search/searchmulti'
//
// data = {"searchKey": "京东", "pageIndex": 2, "pageSize": 20}
//
//
//
// var i = o_default(t, data)
//
// var u = r_default(t, data, s_default())
// console.log(i)
// console.log(u)
