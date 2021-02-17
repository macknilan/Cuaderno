const express = require('express');
const app = express();
const server = require('http').Server(app);
// DEFINIR EL MODULO BODY-PARSER
const bodyParser = require('body-parser');
// SE IMPORTA SOCKET
const socket = require('./socket')
const db = require ('./db');
db('mongodb+srv://db_usr_rodolfo____________________________________________/test');
// DEFINIR EL ROUTRE DE EXPRES
// const router = express.Router();
// const router = require('./components/message/network');
const router = require('./network/routes');
// SE IMPORTA response.js PARA RESPUESTAS UNIFICADAS
// const response = require('./network/response');

// NOTA: EN EL ORDEN EN QUE SE DEFINEN SE TIENEN QUE AÑADIR

// AÑADIR A LA APLICACIÓN EL BODY-PARSER
// RETORNA UN MIDDLEWARE QUE PARSEA JSON Y SOLO OBSERVA LAS PETICIONES EN CONDE EL Cnten-Type SEA IGUAL AL TIPO DE OPCIPON
app.use(bodyParser.json());
// PARA RECIBIR DATA COMO x-www-form-urlencoded
app.use(bodyParser.urlencoded({extended: false}));
// AÑADIR A LA APLICACIÓN EL ROUTER
// app.use(router);
// SE INICIALIZA SOCKET CON SU PROPUEDAD CONNECT Y SE E PASA EL SERVIDOR HTTP
socket.connect(server);
// AÑADIR A LA APLICACIÓN A ROUTES Y PASARLE EL SERVIDOR A ROUTES
router(app);
// SE AÑADE A LA APLICACIÓN estatic DE express PARA SERVIR ARCHIVOS ESTATICOS
app.use('/app', express.static('public'));

/*app.use('/', function(req, res) {
    res.send('Hola');
});*/

server.listen(3000, function() {
    console.log('La aplicación esta escuchando en http://localhost:3000');
    // nodemon server.js
})
