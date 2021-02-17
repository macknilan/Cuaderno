// FUNCION PARA EXPORTAR UN MIDDLEWARE
const auth = require('../../../auth');

module.exports = function checkAuth(action) { // action QUE SE QUIERE EJECUTAR
    function middleware(req, res, next) {
        switch(action) {
            case 'update':
                const owner = req.body.id; 
                // EL USUSARIO QUE GENERA TOKEN ES EL QUE QUEREMOS VERIFICAR
                auth.check.own(req, owner);
                next();
                break;
            case 'follow':
                auth.check.logged(req);
                next();
                break;
            default:
                next();
        }
    }

    return middleware;
}
