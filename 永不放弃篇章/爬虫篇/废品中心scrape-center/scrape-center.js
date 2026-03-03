// e = this.$wasm.asm.encrypt(n, parseInt(Math.round((new Date).getTime() / 1e3).toString()));

var fs = require('fs')

var code = fs.readFileSync('TestMethod.wasm')

function getSign(page) {
    var e = WebAssembly.instantiate(code, {
        "env": {},
        "wasi_snapshot_preview1": {}
    });
    e.then(result => {
        var asm = result["instance"].exports
        // console.log(asm)
        console.log(asm.encrypt(page
            , parseInt(Math.round((new Date).getTime() / 1e3).toString())))
    }, (function (t) {
            return S("wasm streaming compile failed: " + t),
                S("falling back to ArrayBuffer instantiation"),
                i(r)
        }
    ))
}
// 接受 python 调用传递的第三个参数
getSign(process[2])
getSign(process.argv[2])
// console.log(process)