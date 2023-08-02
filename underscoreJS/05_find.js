var _ = require('underscore');

var even = _.find([1,2,5,7,9],function(num){
    return num%2 == 0;
});

console.log(even)