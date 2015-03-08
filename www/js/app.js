var movimetro = angular.module('movimetro', [
  'ngRoute',
  'movimetroControllers',
  'ui.bootstrap'
]);

movimetro.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: 'partials/bienvenida.html',
        controller: 'BienvenidaFotoController'
      }).
      when('/mi-tarjeta', {
        templateUrl: 'partials/mitarjeta.html',
        controller: 'MiTarjetaController'
      }).
      when('/mi-tarjeta/asociar', {
        templateUrl: 'partials/mitarjeta-asociar.html',
        controller: 'MiTarjetaAsociarController'
      }).
      when('/mi-tarjeta/cambiar', {
        templateUrl: 'partials/mitarjeta-cambiar.html',
        controller: 'MiTarjetaCambiarController'
      }).
      when('/mi-tarjeta/recargar', {
        templateUrl: 'partials/mitarjeta-recargar.html',
        controller: 'MiTarjetaRecargarController'
      }).
      when('/mi-tarjeta/transferir', {
        templateUrl: 'partials/mitarjeta-transferir.html',
        controller: 'MiTarjetaTransferirController'
      }).
      when('/alertas', {
        templateUrl: 'partials/alertas.html',
        controller: 'AlertasController'
      }).
      when('/servicio', {
        templateUrl: 'partials/servicio.html',
        controller: 'EstadoServicioController'
      });
      // otherwise({
      //   redirectTo: '/mi-tarjeta'
      // });
  }]);