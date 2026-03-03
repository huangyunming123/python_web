// js异步代码在 python 运行会报错哦
const express = require('express');

const app = express();

app.get('/msg', (req, res) => {
    console.log(req.query)
    res.send('Hello World!');
});

//需要设置这个才能接到post请求参数
app.use(express.json())
app.post('/post', (req, res) => {
    console.log(req.body)
    res.send("你好,入参是" + JSON.stringify(req.body))
})


app.listen(3000, () => {
    console.log('Example app listening on port 3000!')
})

