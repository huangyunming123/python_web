function f() {
    console.log('end')
}

function asyncFunc() {
    return new Promise((resolve, reject) => {
        setTimeout(f, 2000)
        var async_data = 'aaa';
        console.log("1212121")
        resolve(async_data)
        console.log("333333")

    });
}

async function get_async() {
    var res = await asyncFunc();
    console.log(77777)
    console.log(res)

}

get_async()