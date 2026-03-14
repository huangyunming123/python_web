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
window =global

window = global;
window.window = window.top = window.self = window;
window.requestAnimationFrame = function requestAnimationFrame() {
};
window.requestIdleCallback = function requestIdleCallback() {
};
window.DeviceOrientationEvent = function DeviceOrientationEvent() {
};
window.DeviceMotionEvent = function DeviceMotionEvent() {
};

function XMLHttpRequest() {
}

XMLHttpRequest.prototype.open = function () {
};
XMLHttpRequest.prototype.send = function () {
};
XMLHttpRequest.prototype.setRequestHeader = function () {
};
XMLHttpRequest.prototype.addEventListener = function () {
};
window.XMLHttpRequest = XMLHttpRequest;
window.chrome = {};
window.xsecappid = 'xhs-pc-web';
window.loadts = new Date().toString();
window.addEventListener = function addEventListener() {
};
window.MouseEvent = function MouseEvent() {
};

// Object.setPrototypeOf(window, Window.prototype);


function Document() {
}

function Element() {
}


Element.prototype.getAttribute = function getAttribute() {
};

Element.prototype.removeChild = function removeChild() {
};

function HTMLElement() {
    Element.call(this);
}


HTMLElement.prototype = Object.create(Element.prototype);
HTMLElement.prototype.constructor = HTMLElement;

window.HTMLElement = HTMLElement;

function HTMLHtmlElement() {
    HTMLElement.call(this);
}

HTMLHtmlElement.prototype = Object.create(HTMLElement.prototype);
HTMLHtmlElement.prototype.constructor = HTMLHtmlElement;


function HTMLCollection() {
}

// 添加一个基本的 iterator 方法
HTMLCollection.prototype[Symbol.iterator] = function () {
    return [].values(); // 返回一个空数组的迭代器
};


Document.prototype.documentElement = new HTMLHtmlElement();
Document.prototype.getElementsByTagName = function getElementsByTagName(tagName) {
    if (tagName === '*') {
        return [
            {"tagName": "html"},
            {"tagName": "head"},
            {"tagName": "script"},
            {"tagName": "meta"},
            {"tagName": "link"},
            {"tagName": "style"},
            {"tagName": "title"},
            {"tagName": "body"},
            {"tagName": "div"},
            {"tagName": "svg"},
            {"tagName": "defs"},
            {"tagName": "clippath"},
            {"tagName": "rect"},
            {"tagName": "path"},
            {"tagName": "symbol"},
            {"tagName": "circle"},
            {"tagName": "g"},
            {"tagName": "header"},
            {"tagName": "a"},
            {"tagName": "img"},
            {"tagName": "input"},
            {"tagName": "use"},
            {"tagName": "button"},
            {"tagName": "span"},
            {"tagName": "ul"},
            {"tagName": "li"},
            {"tagName": "picture"},
            {"tagName": "i"},
            {"tagName": "p"},
            {"tagName": "section"},
            {"tagName": "iframe"}
        ]
    }
    console.log(`对象 => Document.prototype.getElementsByTagName, 获取元素: ${tagName}`)
};
Document.prototype.addEventListener = function addEventListener() {
};

function HTMLAllCollection() {
    this.length = 1181;
}

function HTMLBodyElement() {
    HTMLElement.call(this);
}


HTMLBodyElement.prototype = Object.create(HTMLElement.prototype);
HTMLBodyElement.prototype.constructor = HTMLBodyElement;
Document.prototype.all = new HTMLAllCollection();
Document.prototype.body = new HTMLBodyElement();
Document.prototype.cookie = '';


function HTMLDocument() {
}

Object.setPrototypeOf(HTMLDocument.prototype, Document.prototype);
document = new HTMLDocument();

Document.prototype.querySelector = function querySelector(selector) {
    if (selector === 'body' || selector === '*') {
        return document.body;
    }
    return null;
};

window.document = document;
window.HTMLDocument = HTMLDocument;


function Navigator() {
}

Navigator.prototype.appCodeName = "Mozilla";
Navigator.prototype.appName = "Netscape";
Navigator.prototype.language = "zh-CN";
Navigator.prototype.languages = [
    "zh-CN",
    "zh",
    "en"
];
Navigator.prototype.platform = "MacIntel";
Navigator.prototype.product = "Gecko";
Navigator.prototype.productSub = "20030107";

function PermissionStatus() {
    this.state = "denied";
    this.then = function then() {
    };
}

function Permissions() {
}

Permissions.prototype.query = function query() {
    // console.log("对象 => navigator.permissions.query " + "调用方法: query", arguments[0])
    return Promise.resolve(new PermissionStatus())
};
Navigator.prototype.permissions = new Permissions();
Navigator.prototype.userAgent = "";
Navigator.prototype.vendor = "Google Inc.";
Navigator.prototype.webdriver = false;
navigator = new Navigator();
// navigator = watch(navigator, "navigator");
window.navigator = navigator;
window.Navigator = Navigator;


function Storage() {
}

sessionStorage = new Storage();
// sessionStorage = watch(sessionStorage, "sessionStorage");
window.sessionStorage = sessionStorage;


localStorage = new Storage();
// localStorage = watch(localStorage, "localStorage");
window.localStorage = localStorage;
window.Storage = Storage;


function Location() {
}

Location.prototype = {
    "ancestorOrigins": {},
    "href": "https://bf5b000000001001945f?xsec_token=AB3TbsCqzVXoWzLIZU5EZiXQBkisr5haqXi5iXIV2NtO0=&xsec_source=pc_note",
    "origin": "https:shu.com",
    "protocol": "https:",
    "host": "www..com",
    "hostname": "www.xiaohongshu.com",
    "port": "",
    "pathname": "/user/00000001001945f",
    "search": "?xsec_token=AB3TbsCqzVXoWzLIZU5EZiXQBkisr5haqXi5iXIV2NtO0=&xsec_source=pc_note",
    "hash": ""
};
location = new Location();
// location = watch(location, "location");
window.location = location;
window.Location = Location;


function History() {
}

history = new History();
// history = watch(history, "history");
window.history = history;
window.History = History;


function Screen() {
}

screen = new Screen();
// screen = watch(screen, "screen");
window.screen = screen;
window.Screen = Screen;


/* 代理检测 */
get_envs(['window', 'document', 'navigator', 'screen', 'history', 'location'])