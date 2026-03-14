require('./1.browser_envs')
require('./2.mod_1')
require('./3.mod_2')
require('./4.pdd_loader')



function get_anti_content() {
    // 调度fbeZ模块
    window.loader('fbeZ');

    // 执行fbeZ模块的ue方法
    return window.ue();
}


console.log(get_anti_content());
// 导出函数
// module.exports = {
//     get_h5st: get_anti_content
// };