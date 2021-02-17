const express = require('express');
const bodyParser = require('body-parser');
const swaggerUi = require('swagger-ui-express');

const config = require('../config.js');
const user = require('./components/user/network');
const auth = require('./components/auth/network');
const erros = require('../network/errors') // SE IMPORTAN LOS ERRORES

const app = express();
// SE INSTALA BODY-PARSER EN LA APP
app.use(bodyParser.json());

// SE IMPORTA EL ARCHIVO JSON DE SWAGGER
const swaggerDoc = require('./swagger.json');

// ROUTER HACIA LOS COMPONENTES
app.use('/api/user', user);
app.use('/api/auth', auth);
// SE INSTALA LE LA APP EN LA DIRECCION /api-docs
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDoc));
// ES IMPORTANTE QUE SEA EL ULTIMO PARA QUE SE CARGUE AL FINAL
app.use(erros);

app.listen(config.api.port, () => {
    console.log('Api escuchando en el puerto ', config.api.port);
});