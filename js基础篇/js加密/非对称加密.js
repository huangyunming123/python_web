let node_rsa = require('node-rsa')

window = this
//用这个包会报错 需要加上window = this
let JSEncrypt = require('jsencrypt')
//设置秘钥长度
let key = new node_rsa({b: 512})

let publicKey = key.exportKey('pkcs8-public')
let privateKey = key.exportKey('pkcs8-private')
console.log(publicKey)
console.log(privateKey)


function et(params) {
    let key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsgDq4OqxuEisnk2F0EJFmw4xKa5IrcqEYHvqxPs2CHEg2kolhfWA2SjNuGAHxyDDE5MLtOvzuXjBx/5YJtc9zj2xR/0moesS+Vi/xtG1tkVaTCba+TV+Y5C61iyr3FGqr+KOD4/XECu0Xky1W9ZmmaFADmZi7+6gO9wjgVpU9aLcBcw/loHOeJrCqjp7pA98hRJRY+MML8MK15mnC4ebooOva+mJlstW6t/1lghR8WNV8cocxgcHHuXBxgns2MlACQbSdJ8c6Z3RQeRZBzyjfey6JCCfbEKouVrWIUuPphBL3OANfgp0B+QG31bapvePTfXU48TYK0M5kE+8LgbbWQIDAQAB';
    let jsencrypt = new JSEncrypt();
    jsencrypt['setPublicKey'](key);
    let _0x4bd6d3 = jsencrypt['encrypt'](params);
    return _0x4bd6d3;
}

function t2() {
    let key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQComqoAyvbCqO1EGsADwfNTWFQIUbm8CLdeb9TgjGLcz95mAo204SqTYdSEUxFsOnPfROOTxhkhfjbRxBV4/xjS06Y+kkUdiMGFtABIxRQHQIh0LrVvEZQs4NrixxcPI+b1bpE0gO/GAFSNWm9ejhZGj7UnqiHphnSJAVQNz2lgowIDAQAB';
    let jsencrypt = new JSEncrypt();
    jsencrypt['setPublicKey'](key);
    let _0x4bd6d3 = jsencrypt['encrypt']("321321321");
    return _0x4bd6d3;
}

// console.log(et("321321321"));

console.log(t2())