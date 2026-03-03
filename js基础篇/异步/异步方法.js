function getAsyncData(){
    return new Promise(function(resolve, reject){
        resolve(1)
        reject(2)
    })
}

function aa(data){
    console.log(data)
}
function bb(data){
    console.log(data)
}

getAsyncData().then(aa,bb)