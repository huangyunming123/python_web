// 我们知道在 JavaScript 中 JSON.stringify() 方法用于将JavaScript 对象或值转换为 JSON 字符串
// JSON.parse() 方法用于将一个 JSON字符串转换为JavaScript 对象，某些站点在向web 服务器传输用户名密码时，会用到这两个方法
// 首先定义了一个变量 stringify 保留原始 JSON.stringify 方法
// 然后重写 JSON.stringify 方法，遇到 JSON.stringify 方法就会执行 debugger 语句，会立即断下
// 最后将接收到的参数返回给原始的 JSON.stringify 方法进行处理，确保数据正常传输
(function() {
      // var _parse = JSON.stringify;
      var _parse = JSON.parse;
      JSON.parse = function(ps) {
          console.log("Hook JSON.parse ——> ", ps);
          debugger;
          return _parse(ps);  // 不改变原有的执行逻辑
      }
  })();

/**
 * hook   cookie 设置  键值对  是 v
 */
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

/**
 *
 * XHR 的 hook   类似捕获请求
 */
  (function () {
      var open = window.XMLHttpRequest.prototype.open;
      window.XMLHttpRequest.prototype.open = function (method, url, async) {
          if (url.indexOf("analysis") != -1) {
              debugger;
          }
          return open.apply(this, arguments);
      };
  })();

