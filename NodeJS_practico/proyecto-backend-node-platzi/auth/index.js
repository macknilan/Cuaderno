// SE IMPORTA LA LIBRERIA
const jwt = require('jsonwebtoken');
// SE IMPOTA ARCHIVO DE CONFIGURACION PARA TRAER SECRETO
const config = require('../config');
// SE IMPORTA LA VARIABLE GOBLAN DEL ARCHIVO cinfig.js
const secret = config.jwt.secret;
// SE IMPORTA ERRORS DE UTILS
const error = require('../utils/erros');

// FUNCION PARA GENERAR/FIRMAR EL TOKEN CON AYUDA DE JWT
function sign(data) {
    return jwt.sign(data, secret);
}
// VALIDAR QUE EL TOKEN QUE OBTENIDO ES VALIDO
function verify(token) {
    return jwt.verify(token, secret)
}

const check = {
    own: function(req, owner) {
        const decoded = decodeHeader(req); // FUNCION PARA DECODIFICAR EL TOKEN
        console.log(decoded);
        // SE COMPRUEBA SI ES, O NO PROPIO
        if (decoded.id !== owner) {
            throw error( 'No puedes hacer esto', 401);
            // throw new Error('No puedes hacer esto');
        }
    },
    logged: function(req, owner) {
        const decoded = decodeHeader(req);
    },
}
// FUNCION PARA SACAR EL TOKEN DESDE LA CABECERA
function getToken(auth) {
    // Bearer <token>
    if (!auth) {
        //throw new Error('No viene token');
        throw error( 'No vienen token', 401);
    }
    // SI EL FORMATO DEL TOKEN NO ES CORRECTO
    if (auth.indexOf('Bearer ') === -1) {
        // throw new Error('Formato invalido');
        throw error( 'Formato invalido', 401);
    }
    // SE OBTIENEN EL TOKEN
    let token = auth.replace('Bearer ', '');
    return token;
}

function decodeHeader(req) {
    const authorization = req.headers.authorization || '';
    const token = getToken(authorization); // FUNCION PARA SACAR EL TOKEN DESDE LA CABECERA
    const decoded = verify(token); // VALIDAR QUE EL TOKEN QUE OBTENIDO ES VALIDO
    req.user = decoded;
    return decoded;
}

module.exports = {
    sign,
    check,
};
