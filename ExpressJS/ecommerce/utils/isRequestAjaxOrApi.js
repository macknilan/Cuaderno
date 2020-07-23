// REALIZAR DOS VALIDACIONES, SI EL `REQUEST` ES DE UNA LLAMADA PARA VISTA "HTML" ES UNA LLAMADA POR AJAX(API)
function isRequestAjaxOrApi(req) {
  return !req.accepts("html") || req.xhr;
}

module.exports = isRequestAjaxOrApi;
