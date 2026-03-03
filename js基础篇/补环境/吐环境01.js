//类似于代理 hook  执行目标属性的时候会执行代理方法

var aa = {
    "name": "baichuan",
    "age": 18
}


var aa = new Proxy(aa,
    {
        get: function (target, propertiesKey, receiver) {
            //本身对象
            //访问属性
            //代理对象
            // console.log(target, "|", propertiesKey, "|", receiver, "|", 'get')

            template = Reflect.get(target, propertiesKey, receiver)
            console.log(`get 对象${target}--》get属性${propertiesKey},get值${template}`)
            return template;
        },
        set: function (target, privateKey, value, receiver) {
            res = Reflect.set(target, privateKey, value, receiver)
            // console.log(target, privateKey, value, receiver, 'set')
            console.log("set :" , target,privateKey,target[privateKey])
            console.log("value:",value," receiver:",receiver)
            return res
        }
    })
//
// console.log(aa['name']);
aa.name = 'zzz'
// console.log(aa.name);
