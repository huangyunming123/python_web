!(function (e) {
    function n(t) {
        return e[t].call();
    }

    n(1)
})([
    function () {
        console.log("webpack打包方式1")
    },
    function () {
        console.log("webpack打包方式2")
    }
])

// 当方法中有 return e[t].call(a.exports,a,a.exports,n)

