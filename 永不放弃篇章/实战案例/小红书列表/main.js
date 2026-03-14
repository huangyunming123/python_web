require('./brower_envs')
require('./source_code_1')

const {b64Encode, encodeUtf8} = require('./source_code_3.js')

var crypt = require('crypto-js')


e = '/api/sns/web/v1/homefeed'
r = {
    "cursor_score": "",
    "num": 31,
    "refresh_type": 1,
    "note_index": 26,
    "unread_begin_note_id": "",
    "unread_end_note_id": "",
    "unread_note_count": 0,
    "category": "homefeed_recommend",
    "search_key": "",
    "need_num": 6,
    "image_formats": [
        "jpg",
        "webp",
        "avif"
    ],
    "need_filter_image": false
}
// var a = window.toString
//     , f = e;
// "[object Object]" === a.call(r) || "[object Array]" === a.call(r) || (void 0 === r ? "undefined" : (0,
//     m._)(r)) === "object" && null !== r ? f += JSON.stringify(r) : "string" == typeof r && (f += r);
// // var c = h.Pu([f].join(""))
// //     , s = h.Pu(e)
// c = crypt.MD5([f].join("")).toString()
// s= crypt.MD5(e).toString()
// res = window.mnsv2(f, c, s)
// console.log(res)
//
// l = {
//     "x0": "4.3.1",
//     "x1": "xhs-pc-web",
//     "x2": "Mac OS",
//     "x3": res,
//     "x4": "object"
// }
// l = {
//     x0: u.i8,
//     x1: "xhs-pc-web",
//     x2: window[u.mj] || "PC",
//     x3: d,
//     x4: r ? void 0 === r ? "undefined" : (0,
//         m._)(r) : ""
// };

// "XYS_" + (0,
//            h.xE)((0,
//            h.lz)(JSON.stringify(l)))

function getRes(e, r) {
    var a = window.toString
        , f = e;
    "[object Object]" === a.call(r) || "[object Array]" === a.call(r) || (void 0 === r ? "undefined" : (0,
        m._)(r)) === "object" && null !== r ? f += JSON.stringify(r) : "string" == typeof r && (f += r);
// var c = h.Pu([f].join(""))
//     , s = h.Pu(e)
    c = crypt.MD5([f].join("")).toString()
    s = crypt.MD5(e).toString()
    res = window.mnsv2(f, c, s)
    l = {
        "x0": "4.3.1",
        "x1": "xhs-pc-web",
        "x2": "Mac OS",
        "x3": res,
        "x4": "object"
    }
    var result = "XYS_" + b64Encode(encodeUtf8(JSON.stringify(f)))
    console.log('getRes result:', result)
    return result
}


module.exports = {
    getRes: getRes
};
