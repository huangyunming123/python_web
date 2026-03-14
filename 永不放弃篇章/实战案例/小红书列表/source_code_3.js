f = [
    "Z",
    "m",
    "s",
    "e",
    "r",
    "b",
    "B",
    "o",
    "H",
    "Q",
    "t",
    "N",
    "P",
    "+",
    "w",
    "O",
    "c",
    "z",
    "a",
    "/",
    "L",
    "p",
    "n",
    "g",
    "G",
    "8",
    "y",
    "J",
    "q",
    "4",
    "2",
    "K",
    "W",
    "Y",
    "j",
    "0",
    "D",
    "S",
    "f",
    "d",
    "i",
    "k",
    "x",
    "3",
    "V",
    "T",
    "1",
    "6",
    "I",
    "l",
    "U",
    "A",
    "F",
    "M",
    "9",
    "7",
    "h",
    "E",
    "C",
    "v",
    "u",
    "R",
    "X",
    "5"
]

function b64Encode(e) {
    for (var r, a = e.length, c = a % 3, s = [], d = 16383, u = 0, l = a - c; u < l; u += d)
        s.push(encodeChunk(e, u, u + d > l ? l : u + d));
    return 1 === c ? (r = e[a - 1],
        s.push(f[r >> 2] + f[r << 4 & 63] + "==")) : 2 === c && (r = (e[a - 2] << 8) + e[a - 1],
        s.push(f[r >> 10] + f[r >> 4 & 63] + f[r << 2 & 63] + "=")),
        s.join("")
}


function tripletToBase64(e) {
    return f[e >> 18 & 63] + f[e >> 12 & 63] + f[e >> 6 & 63] + f[63 & e]
}

function encodeChunk(e, r, a) {
    for (var f, c = [], s = r; s < a; s += 3)
        f = (e[s] << 16 & 0xff0000) + (e[s + 1] << 8 & 65280) + (255 & e[s + 2]),
            c.push(tripletToBase64(f));
    return c.join("")
}

function encodeUtf8(e) {
    for (var r = encodeURIComponent(e), a = [], f = 0; f < r.length; f++) {
        var c = r.charAt(f);
        if ("%" === c) {
            var s = parseInt(r.charAt(f + 1) + r.charAt(f + 2), 16);
            a.push(s),
                f += 2
        } else
            a.push(c.charCodeAt(0))
    }
    return a
}

// 函数导出
module.exports = {b64Encode: b64Encode, encodeUtf8: encodeUtf8}
