// https://www.hanghangcha.com/hhcreport
/**
 * 需要进行登录后才能看
 * 这个网站返回结果被加密了
 *
 * 所以关键操作是JSON.parse()
 *
 *搜索关键字 所以 就用到了 hook  技术   hook  类似于 aop  在你操作的前后进行增强操作
 */

(function() {
      var _parse = JSON.parse;
      JSON.parse = function(ps) {
          console.log("Hook JSON.parse ——> ", ps);
          debugger;
          return _parse(ps);  // 不改变原有的执行逻辑
      }
  })();

/**
 * 当然也可以用传统的  xhr 来做
 *
 * u.a.ajax(m).done  类似于 ajax 回调 success
 *
 * send 走几步 注意观察就行
 */
