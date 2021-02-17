// import * as Sentry from '@sentry/node';
// or using CommonJS
const Sentry = require("@sentry/node");
const Boom = require("@hapi/boom");
const { config } = require("../../config");
const isRequestAjaxOrApi = require("../../utils/isRequestAjaxOrApi");
//
Sentry.init({
  dsn: `https://${config.sentryDns}@o408997.ingest.sentry.io/${config.sentryId}`,
});

// CUANDO CAUSE ERROR SE LE MUESTRA EL STACK DEL ERROR
function withErrorStack(err, stack) {
  if (config.dev) {
    return { ...err, stack }; // Object.assign({}, err, stack)
  }
}

// MIDDLEWARE PARA HACER LOG DE LOS ERRORES
function logErrors(err, req, res, next) {
  Sentry.captureException(err); // AGREGAMOS EL CAPTURADOR DE ERRORES DE Sentry
  console.log(err.stack);
  next(err); // SE LLAMA AL RPOXIMO MIDDLEWARE PASANDO LE EL ERROR CON EL CALLBACK next
}

// SI EL ERROR NO ESTA WRAPEADO CON BOOM ENTONCES QUE LO HAGA
function wrapErrors(err, req, res, next) {
  // INDICATES THIS IS A Boom OBJECT INSTANCE
  if (!err.isBoom) {
    next(Boom.badImplementation(err)); // RETURNS A 500 INTERNAL SERVER ERROR ERROR WHERE
  }

  next(err);
}

// MANEJADOR DE ERRORES DEL CLIENTE
// statusCode THE HTTP STATUS CODE (typically 4xx or 5xx)
// payload THE FORMATTED OBJECT USED AS THE RESPONSE payload(CARGA UTIL) (stringified)
function clientErrorHandler(err, req, res, next) {
  const {
    output: { statusCode, payload },
  } = err;

  // catch errors for AJAX request or if an error ocurrs while streaming
  if (isRequestAjaxOrApi(req) || res.headersSent) {
    // ENVIA EL X-Requested-With= XMLHttpRequest EN CABECERAS CON POSTMAN PARA VERIVICAR EL ERROR
    res.status(statusCode).json(withErrorStack(payload, err.stack)); // REGRESA EL MENSAJE DEL ERROR EN FORMATO JSON PARA QUE SE MUESTRE EN LA API
  } else {
    next(err);
  }
}
// MIDDLEWARE POR DEFECTO
function errorHandler(err, req, res, next) {
  const {
    output: { statusCode, payload },
  } = err;

  // SI NO TIENE UN ERROR SE ESPECIFICA QUE SEA ERROR 500
  res.status(statusCode);
  // SE IMPRIME UNA PAGINA DE ERROR CON EL ERROR COMO PARAMETRO
  res.render("error", withErrorStack(payload, err.stack));
}

module.exports = {
  logErrors,
  wrapErrors,
  clientErrorHandler,
  errorHandler,
};
