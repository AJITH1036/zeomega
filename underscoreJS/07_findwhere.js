var _ = require('underscore');


publicServicePulitzers = [{year: 1918, 
                          newsroom: "The New York Times",
                          reason: "For its public service in publishing in full so many official"
                          + " reports documents and speeches by European statesmen relating to the"
                          + " progress and conduct of the war."}]

var obj = _.findWhere(publicServicePulitzers, {year:1918});

console.log(obj)