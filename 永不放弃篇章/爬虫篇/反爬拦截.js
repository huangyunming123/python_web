/**
 * 遇到无限debugger 用这个
 *
 * 需要再事先运行
 *
 */

var _constructor = constructor;
Function.prototype.constructor = function(s) {
    if (s == "debugger") {
        console.log(s);
        return null;
    }
    return _constructor(s);
}
