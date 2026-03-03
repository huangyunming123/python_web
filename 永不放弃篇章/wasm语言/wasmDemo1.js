/**
 * 如果确定是用wasm 运行 那么可以搜索关键字  WebAssembly   instantiate/instantiateStreaming
 *


 */



//js读取文件用这个
var fs = require('fs')
//本地读取不用fetch
var wasm = fs.readFileSync('wasmDemo1.wasm')

WebAssembly.instantiate(wasm, {'aa': '这个是传参'}).then(function (result) {
    console.log(result.instance.exports.add(1, 2))
})