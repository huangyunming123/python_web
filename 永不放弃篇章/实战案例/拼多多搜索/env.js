delete Buffer

window = global;

// 拼多多检测Buffer关键字
// if (typeof Buffer !== 'undefined') {
//     delete Buffer;
// }

/* 代理脚本 */
function get_envs(proxy_array) {
    for (let i = 0; i < proxy_array.length; i++) {
        handler = `{
            get: function(target, property, receiver) {
                   console.log('方法：get','    对象：${proxy_array[i]}','    属性：',property,'    属性类型：',typeof property,'    属性值类型：',typeof target[property]);
                   return target[property];
            },
            set: function(target, property, value, receiver){
                    console.log('方法：set','    对象：${proxy_array[i]}','    属性：',property,'    属性类型：',typeof property,'    属性值类型：',typeof target[property]);
                    return Reflect.set(...arguments);
            }
        }`;
        eval(`
            try {
                ${proxy_array[i]};
                ${proxy_array[i]} = new Proxy(${proxy_array[i]}, ${handler});
            } catch (e) {
                ${proxy_array[i]} = {};
                ${proxy_array[i]} = new Proxy(${proxy_array[i]}, ${handler});
            }
        `);
    }
}

/* 补环境 */
document = {
    cookie: '_nano_fp=Xpm8X5Uol0dJl0dal9_P1F4JlwcYeCS7snCzCyvz',
    addEventListener: function () {}
}
screen = {
    availHeight: 1019,
    availWidth: 1707
}
navigator = {
    webdriver: false,
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}
history = {
    back: function () {}
}
location = {
    href: 'https://pinduoduo.com/home/boyshirt/'
}

/* 代理检测 */
get_envs(['window', 'document', 'navigator', 'screen', 'history', 'location'])