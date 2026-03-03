
const {VM,VMScript} = require('vm2')

var script = new VMScript('var a = 1; a-1')

var vm = new VM()

console.log(vm.run(script))