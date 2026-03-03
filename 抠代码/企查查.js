let crypt = require('crypto-js')


function getI() {
    // let text = '/api/search/searchmulti{"searchkey":"小米","pageindex":1,"pagesize":20}'
    // let secret = 'iLAgiklLN8QiklLN8QrLi4giLAgiklLN8QiklLN8QrLi4g'
    // let s = crypt.HmacSHA512(text, secret).toString().toLowerCase();
    // console.log(s)
    // console.log(s.substr(8, 20));
    var arguments = [
        "/api/search/searchmulti",
        {
            "searchKey": "小米",
            "pageIndex": 1,
            "pageSize": 100
        }
    ]
    let e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
        , t = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
        , n = JSON.stringify(e).toLowerCase();
    console.log(getI_child(arguments))
    let secret = getI_child(arguments)
    let i = crypt.HmacSHA512(t + n, secret).toString().toLowerCase().substr(8, 20)
    console.log(i)
    // return
    // o.default(t + n, getI_child(t)).toLowerCase().substr(8, 20)
    return i;

}


function getJ() {
    // let text = '/api/search/searchmulti{"searchkey":"小米","pageindex":1,"pagesize":20}'
    // let secret = 'iLAgiklLN8QiklLN8QrLi4giLAgiklLN8QiklLN8QrLi4g'
    // let s = crypt.HmacSHA512(text, secret).toString().toLowerCase();
    // console.log(s)
    // console.log(s.substr(8, 20));
    let t = '/api/search/searchmulti';
    let data = {
        "searchKey": "小米",
        "pageIndex": 1,
        "pageSize": 100
    };
    let tid = 'bd15501ba20f28103269ccde25c00d73';
    let j = getJ_Child([t, data, tid])
    console.log(j)
    return j;
}


function getI_child(data) {
    let codesArr = {
        "n": 20,
        "codes": {
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
    }
    var res = "";
    for (let e = (data.length > 0 && void 0 !== data[0] ? data[0] : "/").toLowerCase(), t = e + e, n = "", i = 0; i < t.length; ++i) {
        let a = t[i].charCodeAt() % codesArr.n;
        res += codesArr.codes[a]
    }
    return res
}

function getJ_Child(args) {
    let e = args.length > 1 && void 0 !== args[1] ? args[1] : {}
        , t = args.length > 2 && void 0 !== args[2] ? args[2] : ""
        , n = (args.length > 0 && void 0 !== args[0] ? args[0] : "/").toLowerCase()
        , i = JSON.stringify(e).toLowerCase();
    let secret = getI_child([n]);
    console.log(secret)
    return crypt.HmacSHA512(n + "pathString" + i + t, secret).toString()
}

function main() {
    let key = getI()
    console.log("------------")
    let value = getJ()
    console.log([key,value])
    return [key, value]
}
