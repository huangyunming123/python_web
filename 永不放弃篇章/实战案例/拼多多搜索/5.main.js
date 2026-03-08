require('./env')
require('./source1')
require('./source2')
require('./sourceTotal')


// function get_anti_content(){
//     window.loader("fbeZ")
//     res = window.ue()
//     console.log(res);
//     return res
// }

function get_anti_content() {
    window.loader('fbeZ');
    return window.ue();
}
// 导出函数
module.exports = {
    get_h5st: get_anti_content
};
