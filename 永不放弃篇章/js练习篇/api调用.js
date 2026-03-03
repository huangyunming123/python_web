var json_str = '{"name":"zs"}'

var json_obj = JSON.parse(json_str)

console.log(typeof json_obj);
console.log(json_obj.name);


var json_data = JSON.stringify(json_obj)

console.log(json_data);
console.log(typeof json_data);


//   aa.apply(this,array) ==  this.aa(array)

//  aa.call(this,b,c) == this.aa(b,c)