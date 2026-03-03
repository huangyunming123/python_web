function getAsyncData(){
    return new Promise(function(resolve, reject){
        resolve(1)
        reject(2)
    })
}

function aa(data){
    console.log(data)
}
function bb(data){
    console.log(data)
}

getAsyncData().then(aa,bb)

/**
 * 异步方法的回调有6个方法 3个大类
 * 0 2 4 为  请求拦截器   发送请求   响应拦截器这三个成功回调  1 3 5 为  请求拦截器   响应拦截器   错误拦截器  这三个失败回调
 *如果是n.then() 这个 优先考虑拦截器 去第一个请求拦截器中找
 *
 * 解密代码 一般都是在响应拦截器
 */

// Object(u.a)(e) 方法  u.a 是方法 e是入参 