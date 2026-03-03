let xhr = new XMLHttpRequest();   //浏览器的对象 需要写在浏览器上
xhr.open()  //创建一个请求对象

xhr.setRequestHeader() // 设置请求头

xhr.send()  //发生请求

xhr.onreadystatechange = function () {console.log(xhr.response)} //  监听 readyState 属性


