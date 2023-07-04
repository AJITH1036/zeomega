var app = angular.module('grocApp',[]);

app.controller('grocList',function($scope){
    
    $scope.groceries = [
                            {item:'Apple'},
                            {item:'Orange'},
                            {item:'Banana'},
                            {item:'Grapes'}, ];
   
});

app.controller('developer',function($scope){
    $scope.name = "Ajith";
});

app.directive('grocList',function(){
    return {
        restrict:"E",
        templateUrl:"views/grocList.html"
    }
});


