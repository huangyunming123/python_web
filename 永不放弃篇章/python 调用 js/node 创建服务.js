const express = require('express')

const app = express();
app.get('/user', (req, res) => {
    res.send('Hello World')
})

app.get('/async', (req, res) => {
    asyncFunc().then(data => {
        res.send(data)
    })
})
app.listen(8000, () => {
    console.log('web 服务创建成功！')
});


function asyncFunc() {
    // return new Promise((resolve, reject) => {
    //     resolve('异步数据测试')
    //
    // })
    //
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('异步结果')
        }, 1000);
    })


}