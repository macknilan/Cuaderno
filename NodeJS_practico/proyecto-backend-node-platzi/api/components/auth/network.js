const express = require('express');

const response = require('../../../network/response');
const Controller = require('./index') /* index.js DEL COMPONENTE USER */
const router = express.Router();


router.post('/login', function(req, res, next) {
    Controller.login(req.body.username, req.body.password)
    .then(token => {
        response.success(req, res, token, 200)
    })
    .catch(next);
    /* .catch(err => {
        response.error(req, res, 'Información invalida', 400)
    }) */
})


module.exports = router;