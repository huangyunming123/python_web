import requests

# res = requests.post("http://127.0.0.1:8080/api", json={'uname': 'zzzlecc'})
# print(res.text)



print(float('1'))

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