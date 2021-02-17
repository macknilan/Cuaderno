// ARCHIVO DE RUTAS DEL COMPONENTE DE MESSAGE
const express = require('express');
const router = express.Router();
// SE IMPORTA response.js PARA RESPUESTAS UNIFICADAS
const response = require('../../network/response');
const controller = require('./controller');

router.get('/', function(req, res) {
    controller.getUser()
    .then((data) => {
            response.success(req, res, data, 201)
    })
    .catch(err => {
        console.log(err);
        response.error(req, res, 'An Unexpected Error Occurred', 500, err)
    })
});

router.post('/', function(req, res) {
  // SE IMPORTAN DEL CONTROLADOR controller.js EL MODULO addMessages PARA AÑADIR MENSAJE
  // SE LE MANDA JSON POR CON VALORES DE USER Y MESSAGE CON POSTMAN
  controller.addUser(req.body.name)
  .then((data) => {
    response.success(req, res, data, 201)
  })
  .catch(err => {
    console.log(err)
    response.error(req, res, 'Internal error', 400, err);
  });
});


module.exports = router;