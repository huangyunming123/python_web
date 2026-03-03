// // js原型
//
// [[Prototype]]   ----  __proto__
//
//
// 分为
//     类的原型（显示原型  .prototype） 跟 实例的原型（隐式原型 .proto ）
//
// Student.prototype === student.__proto__  return true  说明 隐式调用不到的时候会去显示里面找

// navigator = {
//
//     "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
//
// }
//
// console.log(Object.getOwnPropertyDescriptor(navigator,"userAgent"))

//补原型
//补属性

// useragent 其实是 Navigator 的属性
//直接在原型里补
// navigator = {}
// navigator.__proto__.userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36";
// //输出的是undifine 因为在隐式原型里
// console.log(Object.getOwnPropertyDescriptor(navigator,"userAgent"))
// //但是还能调用到
// console.log(navigator.userAgent)

//补充道显示原型中
// let Navigator = function Navigator() {}
// Navigator.prototype = { "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
// let navigator = new Navigator();
// console.log(navigator.userAgent)
// console.log(Object.getOwnPropertyDescriptor(navigator,"userAgent"))


// 补充方法到原型上面


// document = {}
// document.createElement = function createElement() {
// }
// console.log(Object.getOwnPropertyDescriptor(document, 'createElement'))
// // createElement方法在document前两级的对象当中
// console.log(Object.getOwnPropertyDescriptor(document.__proto__.__proto__, 'createElement'));

// document extends HTMLDocument extends Document
//
// var Document = function Document() {
// }
// Document.prototype.createElement = function createElement() {}
//
//
// HTMLDocument = function HTMLDocument() {}
//
// Object.setPrototypeOf(HTMLDocument.prototype, Document.prototype)
//
// document = new HTMLDocument()
//
// console.log(Object.getOwnPropertyDescriptor(document.__proto__.__proto__,"createElement"))

// Document = function Document() {
// }
// // Object.defineProperty 直接在一个对象上定义一个新属性，或修改其现有属性，并返回此对象。
// Object.defineProperty(Document.prototype, 'createElement', {
//     configurable: true,
//     enumerable: true,
//     value: function createElement() {
//     },
//     writable: true,
// })
// HTMLDocument = function HTMLDocument() {
// }
// //可以将一个指定对象的原型（即内部的隐式原型属性）设置为另一个对象
// Object.setPrototypeOf(HTMLDocument.prototype, Document.prototype)
// document = new HTMLDocument()
// console.log(Object.getOwnPropertyDescriptor(document.__proto__.__proto__, 'createElement'));


// // prototype  相当于构造函数
// Document = function Document() {
// }
// Document.prototype.createElement = function createElement() {
// }
// HTMLDocument = function HTMLDocument() {
// }
// //可以将一个指定对象的原型（即内部的隐式原型属性）设置为另一个对象
// Object.setPrototypeOf(HTMLDocument.prototype, Document.prototype)  // 把 HTMLDocument 的原型指向了 Document的原型
//
// let document = new HTMLDocument();
// console.log(Object.getOwnPropertyDescriptor(document.__proto__.__proto__, 'createElement'));
//
// // document.__proto__: 指向 HTMLDocument.prototype，即 HTMLDocument 构造函数的原型对象
// // document.__proto__.__proto__: 指向 HTMLDocument.prototype.__proto__，即 HTMLDocument 原型对象的原型
//
//
// // --------TEST--------
// console.log(document.__proto__.__proto__  ===  Document.prototype)
// console.log(document.__proto__  ===  HTMLDocument.prototype)
// console.log(HTMLDocument.prototype === Document) //false

// toString方法 检测
Document = function Document() {
}
Document.prototype.createElement = function createElement() {
}
Document.prototype.createElement.toString = function toString() {
    return 'function createElement() { [native code] }'
}
HTMLDocument = function HTMLDocument() {
}
Object.setPrototypeOf(HTMLDocument.prototype, Document.prototype)

document = new HTMLDocument()
console.log(document.createElement.toString());
