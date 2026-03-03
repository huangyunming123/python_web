function aaa(args) {
    console.log('导包demo',args)
    return args
}

module.exports = {
    bbb: aaa
}