document = {
    createElement:function () {}
}
console.log(Object.getOwnPropertyDescriptor(document,'createElement'))
//document.__proto__ 观察  得知 createEnlement 方法是 document  继承  HTMLDocument  继承 Document 而得到

//所以第一步 创建的是Document
Document = function () {}
//Object.defineProperty 给对象定义新属性
Object.defineProperty(Document.prototype,'createElement',{
    value:function () {

    },
    writable:true,
    enumerable:true,
    configurable:true
})

HTMLDocument1 = function(){}
// 讲一个指定对象的原型（内部的隐式原型属性） 设置为另一个对象
// 这行代码将 HTMLDocument1.prototype 的隐式原型设置为 Document.prototype，这意味着 HTMLDocument1 的实例将继承 Document 的属性和方法。
Object.setPrototypeOf(HTMLDocument1.prototype,Document.prototype)


htmldocument = new HTMLDocument1()
console.log(Object.getOwnPropertyDescriptor(htmldocument,'createElement'))
//在他的父级里
// htmldocument.__proto__ 指向 HTMLDocument1.prototype。
// htmldocument.__proto__.__proto__ 指向 Document.prototype。
console.log(Object.getOwnPropertyDescriptor(htmldocument.__proto__.__proto__,'createElement'))
console.log(
    '----------------'
)


// document.createElement.toString();

document = {
    createElement:function () {}
}
document.createElement.toString();
// 遇到toString 检测的时候 就用下面的方式  重新给toString  赋值

// document.createElement().toString = function(){
//     return 'function createElement(){native code }'
// }

