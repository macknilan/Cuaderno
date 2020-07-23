
exports.success = function(req, res, message, status) {
    res.status(status || 200).send({
        error: '',
        message: message
    });
}

// SE LE MANDA DE ESTA FORMA
// response.error(req, res, 'Error inesperado', 500, 'Es una simulación de errores')
exports.error = function(req, res, error, status, details) {
    // response.error(`[response error] ${details}`)
    res.status(status || 500).send({
        error: error,
        message: ''
    });
}