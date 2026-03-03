/**
 * npm install axios -s  当前项目 局部 下载 如果是全局 -g  容易找不到宝
 */

axios = require('axios');

axios.interceptors.request.use(function (config) {
    console.log("拦截成功")
    config.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    return config;
}, function (error) {
    console.log("拦截失败")
    return Promise.reject(error);
})

//响应拦截器  服务器过来的数据可能是密文 会写在这里
axios.interceptors.response.use(function (response) {
    console.log("响应成功")
    return response;
}, function (error) {
    console.log("响应失败")
    return Promise.reject(error);
})

axios.get('https://www.baidu.com').then(function (res) {
    console.log(res.data)
})