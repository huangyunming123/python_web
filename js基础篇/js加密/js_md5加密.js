var crypt = require(' crypto-js')

function get_md5() {
    var text = '/api/search/searchmultipathString{"searchkey":"小米","pageindex":2,"pagesize":20}bd15501ba20f28103269ccde25c00d73'
    var secret = '"iLAgiklLN8QiklLN8QrLi4giLAgiklLN8QiklLN8QrLi4g"'
    // console.log(crypt.MD5(text))
    // console.log(crypt.MD5(text).toString())
    console.log(crypt.HmacMD5(text, secret).toString());
    console.log(crypt.HmacSHA1(text, secret).toString());
    console.log(crypt.HmacSHA256(text, secret).toString());
    console.log(crypt.HmacSHA512(text, secret).toString());

}

get_md5()