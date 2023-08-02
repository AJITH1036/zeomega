var _ = require('underscore');

var num = [1,2,3,4,5]

var obj = {
'one':1,
'two':2,
'three':3
}

_.map(num,function(num){
    console.log(num * 5)
})
_.map(obj,function(a , key){
    console.log(a * 3)
})