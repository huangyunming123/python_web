// hook 方法
//解密用这个
(function() {
      var _parse = JSON.parse;
      JSON.parse = function(ps) {
          console.log("Hook JSON.parse ——> ", ps);
          debugger;
          return _parse(ps);  // 不改变原有的执行逻辑
      }
  })();

//加密调这个
(function() {
   var _parse = JSON.stringify;
      JSON.stringify = function(ps) {
          console.log("Hook JSON.stringify ——> ", ps);
          debugger;
          return _parse(ps);  // 不改变原有的执行逻辑
      }
  })();



//hook 属性
user = {
      age: '123'
  }
  aa = user.age
  Object.defineProperty(user, "age", {
      get: function () {
          return aa
      },

      set: function (newVal) {
          console.log("这个人来设置值了！！");
          aa = newVal
      }
  })
  console.log(user.age)
  user.age = '23342'
  console.log(user.age)

//hook cookies
(function () {
      cookieTemp = document.cookie;
      Object.defineProperty(document, 'cookie', {
          set: function (val) {
              if (val.indexOf('v') != -1) {
                  debugger;
              }
              console.log('Hook捕获到cookie设置->', val);
              cookieTemp = val;
          },
          get: function () {
              return cookieTemp;
          },
      });
  })();

//hook  XHR中的请求
// 如果是正数 表示存在里面
  // 如果是-1 表示不在里面

  (function () {
      var open = window.XMLHttpRequest.prototype.open;
      window.XMLHttpRequest.prototype.open = function (method, url, async) {
          if (url.indexOf("analysis") != -1) {
              debugger;
          }
          return open.apply(this, arguments);
      };
  })();

  //hook 拦截器
// npm install axios
axios = require('axios')
//设置请求拦截器
axios.interceptors.request.use(function (config) {
    console.log('请求拦截器 成功')
    config.headers['sign'] = 'lili'
    return config;
}, function (error) {
    console.log('请求拦截器 失败')
    return Promise.reject(error);
});

//设置响应拦截器
axios.interceptors.response.use(function (response) {
    console.log('响应拦截器 成功')
    console.log('调解密函数进行解密数据')
    //return response;
    return response.data; //修改响应数据
}, function (error) {
    console.log('响应拦截器 失败')
    return Promise.reject(error);
});

//发送请求
axios.get('http://httpbin.org/get').then(res=>console.log(res))