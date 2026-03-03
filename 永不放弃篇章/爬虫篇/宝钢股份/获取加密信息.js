const cryptoJS = require('crypto-js');
const express = require("express");

function l(e) {
    for (var n = [], t = Array.of("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"), a = 0; a < e; a++) {
        var c = Math.floor(10 * Math.random());
        n[a] = t[c]
    }
    return n.join("")
}

function s() {
    return parseInt((new Date).getTime() / 1e3)
}

function getHeader(data) {
    e = {
        "data":data,
        "headers": {},
        "method": "post",
        "baseURL": "https://cmsauth.baowugroup.com",
        "url": "/v1/web/api/content/list?domainId=12",
    }
        var n = l(10)
              , t = s()
              , a = cryptoJS.MD5(JSON.stringify(e.data ? e.data : "")).toString()
              , c = ""
              , o = "0/56f5cff3cad14853a44782c2c689ab2a"
              , i = "13ade1de1eff43ffb821735f352a4148";
    e.headers["x-user"] = o
    e.headers["x-nonce"] = n
    e.headers["x-date"] = t
    e.headers["Content-Md5"] = a
     c = "".concat(e.method.toUpperCase(), "\n").concat(e.url.replace(e.baseURL, ""), "\nx-user:").concat(o, "\nx-nonce:").concat(n, "\nx-date:").concat(t, "\nContent-Md5:").concat(a, "\n");
    var u = cryptoJS.HmacSHA1(c, i).toString().toUpperCase();
    e.headers["x-signature"] = u
    return e
}

 data = {
            "pageNo": 1,
            "pageSize": 12,
            "condition": {
                "nodeId": 436
            }
        }
console.log( cryptoJS.MD5(JSON.stringify(data ? data : "")).toString())

// console.log(getHeader());

// const app = express();
//
// app.use(express.json())
// app.post('/post', (req, res) => {
//     console.log(req.body)
//     console.log(getHeader(req.body));
//     res.send(getHeader(req.body))
// })
// app.listen(3000, () => {
//     console.log('Example app listening on port 3000!')
// })