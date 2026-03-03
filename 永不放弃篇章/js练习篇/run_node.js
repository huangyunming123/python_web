function test() {
    console.log(arguments)
}

// 创建数组

let array = new Array(1,2,3,'4');

let newVar = [1,2,3,"4"];
console.log(array)
console.log(newVar)


test(1, 2, 3)

!function () {
    console.log("自执行函数1")
}();

(function () {
    console.log("自执行函数2")
})()


var inner_func;

!function () {
    function _inner_func() {
        console.log("这是内部函数")
    }
    inner_func = _inner_func;
}();
inner_func();
// ======================format  数据方式

const name = 'zs';
const age = 118;
console.log(`my name is  ${name}  age is ${age}`)

// 定时器

function run_test(){
    console.log('定时测试')
}

//执行一次
// setTimeout(run_test,3000)
//周期执行
var handler = setInterval(run_test,1000)

clearInterval(handler)