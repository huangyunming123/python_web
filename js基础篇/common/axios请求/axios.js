var axios1 = require('axios')


axios1.interceptors.request.use(function (config) {
    console.log('这个是请求拦截器');
    config.headers['sign'] = 'sdsafsaghjk'
    return config;
})

axios1.interceptors.response.use(function (response) {
    console.log('这个是响应拦截器')
    return response;
})

axios1.get('http://httpbin.org/get').then(res=>{
    console.log(res.data)
})


// 加载html ----> 加载js -----> 触发请求接口 ---->构造请求对象 ----->请求拦截器 --->请求服务 ----> 返回数据----->响应拦截器