var movimetroControllers = angular.module('movimetroControllers', ['ui.bootstrap']);

// movimetroControllers.controller('MiTarjetaController', ['$scope', '$http',
//   function ($scope, $http) {
//     $http.get('phones/phones.json').success(function(data) {
//       $scope.phones = data;
//     });

//     $scope.orderProp = 'age';
//   }]);

movimetroControllers.controller('MiTarjetaController', function($scope) {
  $scope.user = {
    name: window.localStorage.getItem('app-user.name'),
    email: window.localStorage.getItem('app-user.email'),
    card_number: window.localStorage.getItem('app-user.card_number'),
    current_balance: window.localStorage.getItem('app-user.current_balance')
  }

  $scope.alerts = [];

  var alerts = window.localStorage.getItem('alerts');
  window.localStorage.setItem('alerts', JSON.stringify($scope.alerts));
  if (alerts !== null){
    $scope.alerts = JSON.parse(alerts);
  }
  console.log($scope.alerts);

  $scope.closeAlert = function(index) {
    $scope.alerts.splice(index, 1);
  };

});

movimetroControllers.controller('MiTarjetaRecargarController', ['$scope', '$http',
  function ($scope, $http) {
    $scope.recharge = {};
    
    $scope.recharge_action = function(recharge){
      console.log(recharge.amount);
      console.log(recharge.credit_card_number);
      console.log(recharge.credit_card_month);
      console.log(recharge.credit_card_year);
      console.log(recharge.credit_card_code);

      $http.get('http://192.168.43.238:8000/create_charge', {
        currency: 'MXN',
        amount: recharge.amount,
        description: 'Recarga Tarjeta Metro',
        reference_id: 'recarga_metro_id_usuario'+'1',
        card: 'tok-test-visa-4242'
      }).success(function(data) {
        var current_balance = window.localStorage.getItem('app-user.current_balance');
        window.localStorage.setItem('app-user.current_balance',
          ( current_balance + amount ).toFixed(2)
        );
      });
      
    }
  }]);

movimetroControllers.controller('MiTarjetaAsociarController', function ($scope, $location) {
  $scope.user = {
    name: window.localStorage.getItem('app-user.name'),
    email: window.localStorage.getItem('app-user.email'),
    card_number: window.localStorage.getItem('app-user.card_number'),
  }

  $scope.check = function(user){
    window.localStorage.setItem('app-user.name', user.name);
    window.localStorage.setItem('app-user.email', user.email);
    window.localStorage.setItem('app-user.card_number', user.card_number);
    window.localStorage.setItem('app-user.current_balance', (50.00).toFixed(2));
    console.log('app-user saved');

    var alerts = JSON.parse(window.localStorage.getItem('alerts'));
    alerts.push({
      type: 'success',
      msg: 'Informacion Guardada!'
    });
    window.localStorage.setItem('alerts', JSON.stringify(alerts));
    $location.path("/mi-tarjeta");
  }
});

movimetroControllers.controller('MiTarjetaCambiarController', function ($scope, $location) {
  $scope.user = {
    card_number: window.localStorage.getItem('app-user.card_number'),
  }

  $scope.changeCard = function(user){
    window.localStorage.setItem('app-user.card_number', user.card_number);
    var existing_balance = window.localStorage.getItem('app-user.current_balance');
    window.localStorage.setItem('app-user.current_balance', 
      ( 10.0 + float(existing_balance) ).toFixed(2) );

    var alerts = JSON.parse(window.localStorage.getItem('alerts'));
    alerts.push({
      type: 'success',
      msg: 'Informacion Guardada!'
    });
    window.localStorage.setItem('alerts', JSON.stringify(alerts));

    $location.path("/mi-tarjeta");
  }
});

movimetroControllers.controller('AlertasController', ['$scope', '$routeParams',
  function($scope, $routeParams) {
    $scope.phoneId = $routeParams.phoneId;
  }]);

movimetroControllers.controller('EstadoServicioController', ['$scope', '$routeParams',
  function($scope, $routeParams) {
    $scope.phoneId = $routeParams.phoneId;
  }]);

movimetroControllers.controller('BienvenidaController', function ($scope) {
  $scope.navbarCollapsed = true;
});