// const fs = require('fs');
const express = require('express');
const app = express();


const {get_h5st} = require('./2.代码逻辑分析与结构调整');


app.use(express.json());
app.post('/api/data', (req, res) => {
    console.log('接收到数据:', req);
    console.log('数据处理中...');
    console.log(get_h5st());
    res.json({status: 'success', result: get_h5st()});
});


const PORT = 8888;
app.listen(PORT, () => {
    console.log(`服务已启动: 端口为 ${PORT} ...`);
});
