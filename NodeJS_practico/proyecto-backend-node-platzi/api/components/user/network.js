const express = require('express');
// SE IMPORTA EL MIDDLEWARE
const secure = require('./secure');
const response = require('../../../network/response');
const Controller = require('./index') /* index.js DEL COMPONENTE USER */
const router = express.Router();

// ROUTER
router.get('/', list);
router.post('/follow/:id', secure('follow'), follow);
router.get('/:id', get);
router.post('/', upsert);
// MIDDLEWARE COMPRUEBA EN update LA PERTENENCIA DEL TOKEN
router.put('/', secure('update') , upsert);


// PETICION GET DE LISTA
function list(req, res, next) {
    Controller.list()
    .then((lista) => {
        response.success(req, res, lista, 200);
    })
    .catch(next);
    /* .catch((err) => {
        response.error(req, res, err.message, 500);
    }) */
}
// PETICION GET DE USER POR ID localhost:3000/api/user/1
function get(req, res, next) {
    Controller.get(req.params.id)
    .then((user) => {
        response.success(req, res, user, 200);
    })
    .catch(next);
    /* .catch((err) => {
        response.error(req, res, err.message, 500);
    }) */
}
// PETICION UPSERT
function upsert(req, res, next) {
    Controller.upsert(req.body)
    .then((user) => {
        response.success(req, res, user, 201);
    })
    .catch(next);
    /* .catch((err) => {
        response.error(req, res, err.message, 500);
    }) */
}
// 
function follow(req, res, next) {
    // MI USUARIO - USUARIO AL QUE QUIERO SEGUIR
    Controller.follow(req.user.id, req.params.id)
        .then(data => {
            response.success(req, res, data, 201);
        })
        .catch(next);
}

module.exports = router;