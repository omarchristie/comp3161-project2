var app = angular.module("MealPlanner",['ngRoute','ui.bootstrap']);

angular.module('MealPlanner').factory('Service',['$http','$q',function($http,$q){
    return{
        getUsers : function(){
            var deferred = $q.defer();
            $http.get('/users')
            .success(function(data){
                deferred.resolve(data);
            })
            .error(function(err){
                deferred.reject(err);
            });
            return deferred.promise;
        },
        getRecipes : function(){
            var deferred = $q.defer();
            $http.get('/recipes')
            .success(function(data){
                deferred.resolve(data);
            })
            .error(function(err){
                deferred.reject(err);
            });
            return deferred.promise;
        },
        getIngredients : function(){
            var deferred = $q.defer();
            $http.get('/ingredients')
            .success(function(data){
                deferred.resolve(data);
            })
            .error(function(err){
                deferred.reject(err);
            });
            return deferred.promise;
        },
        getMeasurements : function(){
            var deferred = $q.defer();
            $http.get('/measurements')
            .success(function(data){
                deferred.resolve(data);
            })
            .error(function(err){
                deferred.reject(err);
            });
            return deferred.promise;
        },
        getRestrictions : function(){
            var deferred = $q.defer();
            $http.get('/restrictions')
            .success(function(data){
                deferred.resolve(data);
            })
            .error(function(err){
                deferred.reject(err);
            });
            return deferred.promise;
        },
        getmealplanmeals : function(mtype){
            var deferred = $q.defer();
            $http.get('/getmealplanrecipes/' + mtype)
            .success(function(data){
                console.log("rad");
                console.log(data);
                deferred.resolve(data);
            })
            .error(function(err){
                deferred.reject(err);
            });
            return deferred.promise;
        }
        
    }
}]);

angular.module('MealPlanner').controller('IngredientCtrl',['$scope','Service',function($scope,Service){
    // Service.getIngredients().then(function(ingredients){
    //     $scope.ingredients = ingredients;
    // });
    // console.log($scope.ingredients);
    Service.getMeasurements().then(function(measurements){
        console.log(measurements);
        $scope.measurements = measurements;
    });

    $scope.fields = [{'id':'field1'}]
    $scope.addNewField = function(){
        var newField = $scope.fields.length+1;
        $scope.fields.push({'id':'field'+newField});
    };
    $scope.removelastField = function(){
        var selectField = $scope.fields.length-1;
        $scope.fields.splice(selectField);
    };
}]);

angular.module('MealPlanner').controller('RecipesCtrl',['$scope','Service',function($scope,Service){
    Service.getRecipes().then(function(recipes){
        $scope.recipes = recipes;
    })
}]);

angular.module('MealPlanner').controller('NewRecipeCtrl', ['$scope', 'Service', function ($scope, Service){
	Service.getMeasurements().then(function (measurements) {
		console.log(measurements);
		$scope.measurements = measurements.measurements;
	});

	Service.getIngredients().then(function (ingredients) {
		console.log(ingredients);
		$scope.ingredients = ingredients.ingredients;
	});

	$scope.ingredient= [];
    $scope.instructions = [];
    
	$scope.add_ingredient = function(){
	    var x = {
			quantity: 1,
			measurement: '',
			ingredient: ''

		};
		$scope.ingredient.push(
		   x
		);
		console.log("hi");
	};
    
    
	$scope.add_instruction = function(){
	    var x = {
			quantity: 1,
			measurement: '',
			ingredient: ''

		};
		$scope.instructions.push(
		   x
		);
		console.log("hi");
	};


}]);



angular.module('MealPlanner').controller('GenMealPlanCtrl', ['$scope', 'Service', function ($scope, Service){

	$scope.dostuff = function(){
	    Service.getmealplanmeals('Breakfast').then(function (meals) {
		$scope.breakfasts = meals.meals;
    	});
        Service.getmealplanmeals('Lunch').then(function (meals) {
    		$scope.lunches = meals.meals;
    	});
    	Service.getmealplanmeals('Dinner').then(function (meals) {
    		$scope.dinners = meals.meals;
    	});
	};

}]);

