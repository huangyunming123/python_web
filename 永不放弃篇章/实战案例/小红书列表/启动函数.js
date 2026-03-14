const fs = require('fs');
const express = require('express');
const app = express();
//
// //打印的就是要的值
const {getRes} = require('./main.js');
//

app.use(express.json());
app.post('/xhs/data', (req, res) => {
    const a = req['body']['data'];
    let b = req['body']['encrypt_url'];
    console.log(a,b)
       // const result = get_h5st();
    // console.log('接收到数据:', result);
    var resData = getRes(a,b)
    res.json({status: 'success', result: resData});
});


const PORT = 5233;
app.listen(PORT, () => {
    console.log(`服务已启动: 端口为 ${PORT} ...`);
});
