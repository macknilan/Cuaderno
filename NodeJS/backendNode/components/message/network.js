// ARCHIVO DE RUTAS DEL COMPONENTE DE MESSAGE
const express = require('express');
const multer = require('multer');

const router = express.Router();
// SE IMPORTA response.js PARA RESPUESTAS UNIFICADAS
const response = require('../../network/response');
const controller = require('./controller');

// SE INSTANCIA MULTER PARA DECLARAR DONDE SE GUARDA EL ARCHIVO CUANDO SE HACE POST
const upload = multer({
    dest: 'public/files/',
});

// PARA USAR ROUTER EN LAS PETICIONES
router.get('/', function(req, res) {
    // SE IMPORTAN DEL CONTROLADOR controller.js EL MODULO getMessages PARA TRAER LA LISTA DE MENSAJES
    // BUSCAR POR EL VALOR DE user CON QUERY EN EL REQUEST
    // QUE SE PASA POR LA URL Y SE ALAMACENA EN filterMessage Y SI NO Y SI NO SE ENCUENTRA SE MANDA NULL
    // http://localhost:3000/message?user=NOMBREUSUARIO
    // const filterMessage = req.query.user || null;
    const filterMessage = req.query.chat || null;
    /* console.log(req.query.user) */
    controller.getMessages(filterMessage)
    .then((messageList) => {
        response.success(req, res, messageList, 200)
    })
    .catch(e => {
        response.error(req, res, 'An Unexpected Error Occured', 500, 'e')
    })
});

// SE AÑADE COMO MIDDLEWARE DE EXPRESS. SE LE DICE QUE SOLO ES UN ARCHIVO Y SE LLAMA file
router.post('/', upload.single('file'), function(req, res) {
  // SE IMPORTAN DEL CONTROLADOR controller.js EL MODULO addMessages PARA AÑADIR MENSAJE
  // SE LE MANDA JSON POR CON VALORES DE USER Y MESSAGE CON POSTMAN
  controller.addMessage(req.body.chat, req.body.user, req.body.message, req.file)
  .then((fullMessage) => {
    response.success(req, res, fullMessage, 201)
  })
  .catch(e => {
    console.log(e)
    response.error(req, res, 'Información invalida', 400, 'Error en el controlador')
  });
});

// RUTA PARA ACTUALIZAR MENSAJE RECIBE id EN LA URL
router.patch('/:id', function (req, res) {
    // EN req.params.id ES DONDE ESTA LA DATA SOLICITADA EN TODO LA INFO DE REQUEST
    controller.updateMessage(req.params.id, req.body.message)
    .then((data) => {
        response.success(req, res, data, 200);
    })
    .catch(e => {
        response.error(req, res, 'Error interno', 500, e)
    })
})

router.delete('/:id', function(req, res) {
    controller.deleteMessage(req.params.id)
    .then(() => {
        response.success(req, res, `Mensaje ${req.params.id} eliminado`, 200);
    })
    .catch(e => {
        response.error(req, res, 'Error interno', 500, e);
    })
})

module.exports = router;