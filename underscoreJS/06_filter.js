var _ = require('underscore');

var even = _.filter([1,2,3,4,5,6,7,8,9],function(n){
    return n % 2 == 0;
})

console.log(even)