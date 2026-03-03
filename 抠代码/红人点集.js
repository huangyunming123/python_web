var crypt = require('crypto-js')

req = {
    "no": "dy00022",
    "data": {
        "days": 1,
        "rankType": 5,
        "liveDay": "2024-06-16"
    }
}

function get_sign(n) {
    let e = (new Date).getTime()
    let data = "param=" + n + "&timestamp=" + e + "&tenant=1&salt=" + "kbn%&)@<?FGkfs8sdf4Vg1*+;`kf5ndl$";
    console.log(SHA256Data(data))
    return {sign: SHA256Data(data), time_Data: e}
}

function SHA256Data(data) {
    return crypt.SHA256(data).toString();
}
