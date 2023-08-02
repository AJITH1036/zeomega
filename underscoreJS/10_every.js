var _ = require('underscore')


var res = _.every([2,4],function(num){
    return num % 2 == 0;
})

// return true if all values passes the condition
console.log(res)