const fs = require('fs');
const express = require('express');
const app = express();
//
// //打印的就是要的值
const {get_h5st} = require('./5.main.js');
//

app.use(express.json());
app.get('/api/data', (req, res) => {
       const result = get_h5st();
    console.log('接收到数据:', result);
    res.json({status: 'success', result: result});
});


const PORT = 5211;
app.listen(PORT, () => {
    console.log(`服务已启动: 端口为 ${PORT} ...`);
});
