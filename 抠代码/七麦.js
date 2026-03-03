// 控制台输入 copy(a) 就能实现复制

function main(aa) {
// let aa = ['2024-06-11_2024-06-11', 'cn', '36', '4', '3', '2024-06-11', '2024-06-11']
    let a = aa['sort']()['join']('')
// a = i[jt](a)
    a = v(a)
    var r = +new Date() - 181 - 1661224081041
    a = (a += "@#" + "/rank/offline"["replace"]("https://api.qimai.cn", "")) + ("@#" + r) + ("@#" + 3)

    e = cv(oz(a, "xyz517cda96efgh"))
    url = "/rank/offline"
    url += (-1 != url["indexOf"]("?") ? "&" : "?") + "analysis" + "=" + encodeURIComponent(e)
    console.log(url)
    return url;
}


function v(t) {
    t = encodeURIComponent(t)["replace"](/%([0-9A-F]{2})/g, function (n, t) {
        return o("0x" + t)
    });
    return btoa(t)
}

function o(n) {
    t = "",
        ['66', '72', '6f', '6d', '43', '68', '61', '72', '43', '6f', '64', '65'].forEach(function (n) {
            t += unescape("%u00" + n)
        });
    var t, e = t;
    return String[e](n)
}

function cv(t) {
    t = encodeURIComponent(t)["replace"](/%([0-9A-F]{2})/g, function (n, t) {
        return o("0x" + t)
    });
    return btoa(t)
}

function oz(n, t) {
    // t = t || u();
    for (var e = (n = n["split"](""))["length"], r = t["length"], a = "charCodeAt", i = 0; i < e; i++)
        n[i] = o1(n[i]["charCodeAt"](0) ^ t[(i + 10) % 15]["charCodeAt"](0));
    return n["join"]("")
}

function o1(n) {
    t = "",
        [
            "66",
            "72",
            "6f",
            "6d",
            "43",
            "68",
            "61",
            "72",
            "43",
            "6f",
            "64",
            "65"
        ].forEach(function (n) {
            t += unescape("%u00" + n)
        });
    var t, e = t;
    return String[e](n)
}
