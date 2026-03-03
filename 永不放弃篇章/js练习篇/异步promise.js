// pending  fulfilled  reject

function test() {
    console.log("test")
    return 123;
}

function simplePromise() {
    let promise = new Promise(function (successRes, faildRes) {
            //逻辑代码
            var flag = true
            if (flag) {
                successRes(test)
            } else {
                faildRes('这里放失败操作的代码')
            }
        }
    );
    return promise;
}

var obj = simplePromise()
obj.then(function (res) {
    console.log("success")
    console.log(res())

}).catch(function (error) {
    console.log("error")
    console.log(error)
})
