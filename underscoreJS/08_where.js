var _ = require('underscore')

var list = [{ year: 1918,
    newsroom: 'The New York Times',
    reason:'For its public service in publishing in full so many official reports documents and speeches by European statesmen relating to the progress and conduct of the war.' }
]

 var res =  _.where(list,{year:1918})

 console.log(res)