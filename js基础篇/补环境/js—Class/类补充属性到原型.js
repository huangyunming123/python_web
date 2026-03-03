class Person {

    constructor(name) {
        console.log('子集')
        this.name = name;
    }

    dance() {
        console.log('跳舞')
    }

}


class Student extends Person {
    constructor(name, score, sex) {
        super(name);
        this.sex = sex
        this.score = score
    }

    sing(){
        console.log('唱歌')
    }
}

// student  = new Student('zs',100)
// student.dance()
// console.log(student.name);


// [[prototypo]] 对象的隐式原型 stu调用

//Student.protoType  显式原型


// 原型 就是父类       类的隐式就是对象的显式原型

//直接补   有时候 遇到原型检测就不好了
navigator = {
    userAgent: '123123'
}
console.log(Object.getOwnPropertyDescriptor(navigator, 'userAgent'))

//需要补到原型里  不然有时候出现原型检测无法通过  隐式原型
navigator = {}
navigator.__proto__.userAgent = '123123'
console.log(navigator.userAgent)
console.log(Object.getOwnPropertyDescriptor(navigator, 'userAgent'))


//补到显式原型
var Navigator = function () {}
Navigator.prototype = {'userAgent': 12121}
var navigator =new  Navigator()
console.log(navigator.userAgent)
console.log(Object.getOwnPropertyDescriptor(navigator, 'userAgent'))