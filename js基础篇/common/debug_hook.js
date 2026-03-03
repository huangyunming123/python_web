(function () {
        var _parse = JSON.parse;
        JSON.parse = function (ps) {
            console.log('被hook了')
            debugger
            return _parse(ps)
        }
    }
)();
//hook cookie
(function () {
    cookie_data = document.cookie;
    Object.defineProperty(document, 'cookie',
        {
            set: function (val) {
                if (val.indexOf('v') != -1) {
                    debugger
                }
                cookie_data = val
            },
            get: function () {
                return cookie_data
            }
        })
})()

    // hook  xhr请求
    (function () {
        var open = window.XMLHttpRequest.prototype.open;
        window.XMLHttpRequest.prototype.open = function (method, url, async) {
            if (url.indexOf('analysis') != -1) {
                debugger
            }
            return open.apply(this, arguments)
        }
    })()
    //  XHR.open() 构建请求  XHR.send()发送请求  ajax的底层
    (function () {
        var open = window.XMLHttpRequest.prototype.open;
        window.XMLHttpRequest.prototype.open = function (method, url, async) {
            if (url.indexOf("analysis") != -1) {
                debugger;
            }
            return open.apply(this, arguments);
        };
    })()