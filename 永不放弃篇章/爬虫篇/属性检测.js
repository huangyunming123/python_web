/**
 * Object.defineProperty(obj, prop, descriptor)，它的作用就是直接在一个对象上定义一个新属性，或者修改一个对象的现有属性，接收的三个参数含义如下：
 *
 *
 *
 * @type {{age: string}}
 */
user = {
      age: '123'
  }
  aa = user.age
  Object.defineProperty(user, "age", {
      get: function () {
          return aa
      },
      set: function (newVal) {
          console.log("这个人来设置值了！！");
          aa = newVal
      }
  }
  )
console.log(user.age)
user.age = '23342'
console.log(user.age)