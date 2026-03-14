delete Buffer
window = global;

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
    addEventListener: function () {
    },
    cookie: '_nano_fp=XpmjnpTqX0PoXpXYXT_Ua1mSOiCU5_cUVr1OVJPN',
}
screen = {
    availHeight: 1080,
    availWidth: 1920,
}
history = {
    back: function () {
    }
}
navigator = {
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54',
    webdriver: false
}
location = {
    href: 'https://pinduoduo.com/home/boyshirt/'
}

/* 代理检测 */
get_envs(['window', 'document', 'navigator', 'screen', 'history', 'location'])