// ARCHIVO DE RUTAS DEL COMPONENTE DE MESSAGE
const express = require('express');
// SE IMPORTA response.js PARA RESPUESTAS UNIFICADAS
const response = require('../../network/response');
const controller = require('./controller');
const router = express.Router();

router.post('/', function(req, res) {
    // SE RECIBE UN PARAMETRO USERS EN EL BODY
    controller.addChat(req.body.users)
    .then(data => {
        response.success(req, res, data, 201);
    })
    .catch(err => {
        response.error(req, res, 'Internal Error Ocurred', 501, err);
    });
});

// '/:userId' SE TRAE EL ID DEL USUARIO PARA TRAER TODOS LOS DEL MISMO USUARIO
router.get('/:userId', function(rew, res) {
    controller.listChat(req.params.userId)
    .then(users => {
        response.success(req, res, users, 201);
    })
    .catch(err => {
       response.error(req, res, 'Internal Error Ocurred', 501, err); 
    });
});

module.exports = router;
