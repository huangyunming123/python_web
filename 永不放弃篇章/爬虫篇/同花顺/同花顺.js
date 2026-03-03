/**
 * hook   cookie 设置  键值对  是 v
 *
 *
 * qn.update 是 cookie 加密之前的数据  setCookie  往往是加密后的
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

