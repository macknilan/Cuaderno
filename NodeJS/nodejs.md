
# Curso de Node.js


## 1. Conocer y comprender cómo se realizan las conexiones hacia los servidores a través de internet y sus implicaciones en el desarrollo de servidores
### 1. Bienvenida y presentación del curso
Repositorio del proyecto

:octocat: [CodingCarlos/backend-node-platzi](https://github.com/CodingCarlos/
backend-node-platzi)

### 2. Qué es Node y cómo instalarlo
**Node.js** es un entorno en tiempo de ejecución multiplataforma de código abierto para la capa del servidor basado en el lenguaje de programación ECMAScript, asíncrono y basado en el motor **V8 de Google**.

+ Muchos proyectos utilizan Node para funcionar, como:
    * [electron](https://www.electronjs.org/)
    * [PM2](https://pm2.keymetrics.io/)
    * [Babel](https://babeljs.io/)
    * [Webpack](https://github.com/webpack/webpack)

### 3. ¿Qué son y cómo se usan las peticiones HTTP?
Una petición **HTTP** es un protocolo de comunicación que permite las transferencias de información en la web.

Es el lenguaje común para todas las comunicaciones.

¿Cómo es una petición?
```
GET /index.html HTTP/1.1
Host: www.example.com
Referer: www.google.com
User-Agent: Mozilla/5.0
Connection: keep-alive
```
+ Puntos claves a tener en cuenta:
    * **Métodos**: Qué quieres hacer
    * **Estado**: Cómo ha ido la operación
    * **Cuerpo**: Lo que el servidor devuelve

**HTTP** es un protocolo que se encuentra dentro de la capa de aplicacion, dicha capa se encuentra en el **septimo nivel** del **MODELO OSI** y cuarto del modelo **TCP**.

La diferencia de **http** y **https** es que **https** pasa por un canal de encriptacion haciendo que los datos que se envían por Internet sean imposibles de entender y cuando llegan al servido estos se descifra.

Existen diferentes protocolos dentro de esta capa:
+ Protocolos:
    + **FTP** (_File Transfer Protocol_ - Protocolo de transferencia de archivos) para transferencia de archivos.
    + **DNS** (_Domain Name System_ - Sistema de nombres de dominio).
    + **DHCP** (_Dynamic Host Configuration Protocol_ - Protocolo de configuración dinámica de anfitrión).
    + **HTTP** (_HyperText Transfer Protocol_) para acceso a páginas web.
    + **HTTPS** (_Hypertext Transfer Protocol Secure_) Protocolo seguro de transferencia de hipertexto.
    + **POP** (_Post Office Protocol_) para recuperación de [correo electrónico].
    + **SMTP** (_Simple Mail Transport Protocol_) para envío de correo electrónico.
    + **SSH** (_Secure SHell_)
    + **TELNET** para acceder a equipos remotos.

| HTTP  |  Es el protocolo de comunicaciones que permite las transparencias de infoemación en la web  |
| Importancia  |  Al ser un protocolo es algo que se va a usar comúnmente(lenguaje común)     |
| ¿Cómo funciona?  | Un cliente manda una petición  (http) donde le llegará al servidor, se procesa y responde a la petición     |
|  Host  |  A donde o estoy pidiendo  |
|  Referer  |  De donde viene  |
|  User-Agent  |  Navegador  |
|  Connection  |  Que le va a pasar al enlace entre el cliente y al servidor  |

### 4. Métodos, cabeceras y estados

Métodos: el verbo que dice "lo que vamos haver" al servidor
+ Métodos HTTP:
    + **GET**: Recoger información del servidor.
    + **POST**: Añadir información al servidor.
    + **PUT**: Reemplazar información en el servidor.
    + **PATCH**: Actualizar parte de la información.
    + **DELETE**: Eliminar información del servidor.
    + **OPTIONS**: Pedir información sobre métodos (saber si podemos ejecutar alguno de los métodos anteriores).

**Las cabeceras** serán el envío al servidor de cómo queremos hacer la petición. Infomación contextual de la petición

En **GET**, **POST**, **PUT** pueden tenener esta información cache, Indicaciones, Condiciones, CORS, Cookies, 

+ Cookies: Compartir información entre peticiones
+ CORS: Cross Origin Resource Sharing: Maneja información desde fuera de nuestro servicio. `Acces-Control-Allow-Origin`
+ Accept: Define el contenido que acepta:
    + Accept
    + Accept-Charset
    + Accept-Encoding
+ Autenticación: Asegurarte que puedes pedir cosas al servidor: Authorization
+ Cache: Almacenamiento temporal: Gestionar durante cúanto tiempo la respuesta será la misma
    * cache-control
    * Expires

+ Los **estados** son números que indica el estado de la petición:
    * **2XX**: Todo ha ido bien.
        * 200:OK
        * 201:Created
    * **3XX**: La petición se ha redirigido.
        * 301: Moved permanently
        * 304:Not modified
    * **4XX**: Errores del cliente y servidor.
        * 400:Bad Request
        * 401: Unauthorized
        * 403:Forbidden
        * 404:Not Found
    * **5XX**: Ha habido un error al procesar la petición.
        * 500:Internal server error

### 5. Cuerpo y query de la petición
[HTTP Messages](https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages)

+ **Cuerpo**: Es la información de la petición, los datos del usuario que quieres añadir. Dependen de las cabeceras `Content-type` y `Content-length`
    * Content-type
        - text/html
        - text/css
        - application/javascript
        - image/jpeg
        - application/json
        - application/xml
Request
```
[POST]
http://api.com/user
-> content-type: application/json
{
    "name": "Carlos",
    "username": userCarlos
}
```
Response
En cualquier método
Un archivo html, css, js, etc
Los datos de un producto
```
[GET]
-> content-type: text/html
<html>
    <head> ... </head>
    <body> ... </body>
</html>
```
+ Query: Es información extra y compartir datos con el frontend
    - Orden en que se desean los datos que se devuelban.
    - Parámetros que quieres medir
    - NOTA: el susario verá toda la información y hay que tener cuidado que información se manda al frontend
```
youtube.com/watch?v=KJSDHSDLFKJ
#
api.com/person?orderBy=name&age25
```
+ Estructura de query
    + Añadir **?** al final de una **URL**
    + nombre=valor
    + Separados por **&**

## 2. Crear un servidor HTTP en Javascript, y comenzar a escuchar y responder peticiones desde un cliente .
### 6. Crear un servidor HTTP desde NodeJS
Para crear un server en NodeJS:

1. Instalamos,importamos y usamos una librería como express `npm i expresss` estando parado donde esta `package.json`
2. Se crea el archivo `server.js` a la misma altura que el archivo `package.json`
```js
const express = require('express');

var app = express();
// use PARA DECIRLE A EXPRESS QUE USE LAS RUTAS en este caso /(root)
app.use('/', function(req, res) {
    res.send('Hola'); // EN res(RESPONSE) EXITOSA SE REGRESA 'Hola'
});
// SE LEVANTA EL SERVIDOR EN EL PUERTO 3000
app.listen(3000);

console.log('La aplicación esta escuchando en http://localhost:3000');
// node server.js
```
Para no tener que andar bajando y subiendo el server se puede instalar una librería que se llama **nodemon**, la cual detecta cambios en el `package.json` del proyecto y hace el reload del proyecto automáticamente.
```bash
$ sudo npm i -g nodemon
```
Despues para ejecutar el archivo
```bash
$ nodemon server
```

### 7. ¿Cómo pueden venir las peticiones?
Para que funcione se puede usar **postman** se puede mandar las peticiones a cada metodo y revisar la respuesta a `http://localhost:3000`

`server.js`
```js
const express = require('express');
// DEFINIR EL ROUTRE DE EXPRES
const router = express.Router();

var app = express();
// AÑADIR A LA APLICACIÓN EL ROUTER
app.use(router);

// PARA USAR ROUTER EN LAS PETICIONES
router.get('/', function(req, res) {
    res.send('Lista de mensajes');
});

router.post('/', function(req, res) {
    res.send('Mensaje añadido');
});
/*app.use('/', function(req, res) {
    res.send('Hola');
});*/
app.listen(3000);

console.log('La aplicación esta escuchando en http://localhost:3000');
// node server.js
```

### 8. Recibir información desde el cliente: Body y Query
**Body-parser**: es una extensión que nos permite trabajar con el body de la petición de forma sencilla.
:link: [body-parser](https://expressjs.com/en/resources/middleware/body-parser.html)
```
$ npm install body-parser
```

```js
const express = require('express');
// DEFINIR EL MODULO BODY-PARSER
const bodyParser = require('body-parser');
// DEFINIR EL ROUTRE DE EXPRES
const router = express.Router();
// NOTA: EN EL ORDEN EN QUE SE DEFINEN SE TIENEN QUE AÑADIR
var app = express();
// AÑADIR A LA APLICACIÓN EL BODY-PARSER
// RETORNA UN MIDDLEWARE QUE PARSEA JSON Y SOLO OBSERVA LAS PETICIONES EN CONDE EL Cnten-Type SEA IGUAL AL TIPO DE OPCIPON
app.use(bodyParser.json());
// PARA RECIBIR DATA COMO x-www-form-urlencoded
app.use(bodyParser.urlencoded({extended: false}));
// AÑADIR A LA APLICACIÓN EL ROUTER
app.use(router);

// PARA USAR ROUTER EN LAS PETICIONES
router.get('/message', function(req, res) {
    console.log(req.body);
    res.send('Lista de mensajes');
});

router.post('/message', function(req, res) {
    console.log(req.body);
    console.log(req.query);
    res.send('Mensaje añadido ' + req.body.text + ' correctamente');
});
app.listen(3000);
console.log('La aplicación esta escuchando en http://localhost:3000');
// node server.js
```
Las respuestas en consola se deben de mostrar de la siguiente mandera cuando se le pasa el data por json y x-www-form-urlencoded
```bash
{ text: 'hola' }
```
Cuanndo se le pasa el request por `query` con postman mandar la peticion
```bash
http://localhost:3000/message?orderBy=id&AGE=15
```
La salida en consola es
```bash
{ text: 'hola' }
{ orderBy: 'id', AGE: '15' }
```

### 9. Información contextual: Leer las cabeceras

```js
router.get('/message', function(req, res) {
    console.log(req.body);
    // LEER LÑAS CABECERAS
    console.log(req.headers);
    // ESTABLECER CABESERAS PERSONALIZADAS
    res.header({
      "custom-header": "Nuestro valor personalizado",
      "Cache-Control": "public, max-age=300"
    });
    res.send('Lista de mensajes');
});
```

Con `console.log(req.headers);` se pude ver en consola que cuales con las cabeceras que manda REQUEST y con postman se pude ver de la siguiente manera y cuando se entra desde un browser se pueden observar mas datos y mas cabeceras de diferentes tipos.
```bash
{
  'user-agent': 'PostmanRuntime/7.25.0',
  accept: '*/*',
  'cache-control': 'no-cache',
  'postman-token': 'cd856f65-9078-4680-b894-ebb47933a9bd',
  host: 'localhost:3000',
  'accept-encoding': 'gzip, deflate, br',
  connection: 'keep-alive'
}
```
Y la cabecera personalizada `custom-header` en postmant se muestran las cabeceras de respuesta

### 10. Tipos de respuesta: Vacía, plana, con datos y estructurada

Se pueden enviar todo tipo de respuestas, dependiendo que se necesite.   
Con postman se manda mensaje de **POST** a la dirección `http://localhost:3000/message` y la respuesta se muestra
```js
router.post('/message', function(req, res) {
  console.log(req.body);
  console.log(req.query);
  // res.send('Mensaje añadido ' + req.body.text + ' correctamente');
  // res.send() // RESPUESTA VACIA
  // res.status(201).send(`Mensaje añadido ${req.body.text} correctamente`);
  res.status(201).send({
    error: '',
    body:'Creado correctamente'
  });
});
```

```json
{
    "error": "",
    "body": "Creado correctamente"
}
```


### 11. Respuestas coherentes
:link: [Export Module in Node.js](https://www.tutorialsteacher.com/nodejs/nodejs-module-exports)

Se crea la carpeta `network` a la misma altura de `package.json` en la cual estaran todas las partes que pertenescan a la capa de red de la aplicación.

Se crea el archivo `response.js` el cual sirve para responder desde un solo lugar de forma coherente y se evita tener muchos **endpoints**

En el archivo `server.js` se importan las respuestas
```js
// SE IMPORTA response.js PARA RESPUESTAS UNIFICADAS
const response = require('./network/response');

router.get('/message', function(req, res) {
    console.log(req.body);
    console.log(req.headers);
    res.header({
      "custom-header": "Nuestro valor personalizado",
      "Cache-Control": "public, max-age=300"
    });
    // SE IMPORTA MODULO `response` PARA ESTANDARIZAR LA FORMA DE MOSTRAR LAS RESPUESTAS
    response.success(req, res, 'Lista de mensajes', 201)
});

router.post('/message', function(req, res) {
  console.log(req.body);
  console.log(req.query);
  // SE IMPORTA MODULO `response` PARA ESTANDARIZAR LA FORMA DE MOSTRAR LAS RESPUESTAS
  response.success(req, res, 'Creado correctamente', 201)
});


```

`response.js`
```js
exports.success = function(req, res, message, status){
    res.status(status || 200).send({
        error: '',
        message: message
    });
}

exports.error = function(req, res, error, status){
    res.status(status || 500).send({
        error: error,
        message: ''
}
```


### 12. Servir archivos estáticos
Para servir archivos estaticos se crea la carpeta `public` la cual lleva ese nombre por convención y se crea en la raiz del proyecto

La ruta es solo una dirección, donde quieres que cada vez que el cliente entre a esa ruta, el servidor vaya y muestre el contenido que está en la carpeta `public`. Pero puede colocar lo que quieras.
```js
app.use('/loquequieras', express.static(`public`)
```
Entonces cada vez que el cliente vaya a `http://localhost:3000/loquequieras` verá el contenido de la carpeta public del servidor

`server.js`
```js
// SE AÑADE A LA APLICACIÓN estatic DE express PARA TRABAJAR
app.use('/app', express.static('public'));
```
Se tiene que crear dentro de static el archivo `index.html` se tienen que llamar así, si no express no lo toma en cuenta.

`index.html` para poder verlo se tiene que ser en la dirección `http://localhost:3000/app/`
```html
<html>
    <body>
        Hola, ejemplo de archivo estatico
    </body>
</html>
```
Tambien para los archivos css, se crea una carpeta `css` y para poder verlo es en la ruta `http://localhost:3000/app/css/style.css`
```css
body {
    background-color: red;
}
```

### 13. Errores: Cómo presentarlos e implicaciones en la seguridad
Se tienen que presentar la información minima requerida al usuario con respectyo al error, y no mostrar le detalles internos del error del sistema para que ocacione problemas de seguridad.

`response.js`
```js
// SE LE MANDA DE ESTA FORMA
// response.error(req, res, 'Error inesperado', 500, 'Es una simulación de errores')
exports.error = function(req, res, error, status, details) {
    response.error(`[response error] ${details}`)
    res.status(status || 500).send({
        error: error,
        message: ''
    });
}
```


## 3. Comprender y desarrollar la arquitectura básica de un backend en NodeJS, y comunicarse entre módulos
### 14. Conceptualmente: Rutas, controladores y bases de datos
**Capas**:   
1. Capa Principal: Toda la configuración de nuestro servidor
2. Capa de Red: Donde se encuentran nuestra configuración de nuestras rutas y respuestas.
3. Capa de componentes: Aquí estarán todos nuestros componentes.

![Arquitectura BackEnd con NodeJS](imgs/arquitectura_backend_nodejs.png)

### 15. Rutas y capa de red: Responsabilidades y límites

Cualquier aplicación va a tener tres puntos de responsabilidad, que deben responder a tres preguntas:

+ ¿Cómo me comunico con ella?
+ ¿Qué hace?
+ ¿Dónde y cómo se guardan los resultados?

+ La respuesta a estos tres puntos, corresponden a las tres capas que vamos a generar:
    * Capa de red(en inglés **“network”**)
    * Capa controladora(en inglés, **“controller”**)
    * Capa de almacenamiento(en inglés, **“store”**)

De esto se habla en el puntop anterior.

_La primera capa es una capa de red_, porque la conexión con la aplicación se hace a través del protocolo de comunicación en red HTTP. Es la responsable de comunicar al cliente HTTP con nuestro código del controlador.

En los primeros puntos, se ve que el protocolo HTTP construye una petición con una dirección (_route_), un verbo (_method_), unas cabeceras (_headers_) y un mensaje (_body_).

Por esto, cada uno de los componentes, tendrá un archivo `network.js` encargado de traducir la petición del cliente _HTTP_ a la acción que queremos realizar en nuestro controlador.

Así, lo que hace nuestro código (_la funcionalidad_) no está acoplado a unos requisitos de red, y puede ser reutilizado con otras fuentes de entrada (_colas MQTT, una biblioteca externa, microservicios…_).

Se crea la carpeta `components` en la raiz del proyecto dentro de ella se crea la carpeta del **componente** `message` y dentro se crea el archivo `network.js` (_QUE ACTUA COMO LA CAPA DE RED_)

Arbol de carpetas sugerido para proyectos.
```bash
├── components
│   └── message
│       └── network.js
├── css
├── network
│   ├── response.js
│   └── routes.js
├── package.json
├── package-lock.json
├── public
│   ├── index.html
│   └── style.css
└── server.js
```

`server.js`
```js
const express = require('express');
// DEFINIR EL MODULO BODY-PARSER
const bodyParser = require('body-parser');
// DEFINIR EL ROUTRE DE EXPRES
// const router = express.Router();
// const router = require('./components/message/network');
const router = require('./network/routes');
// SE IMPORTA response.js PARA RESPUESTAS UNIFICADAS
// const response = require('./network/response');

// NOTA: EN EL ORDEN EN QUE SE DEFINEN SE TIENEN QUE AÑADIR

var app = express();
// AÑADIR A LA APLICACIÓN EL BODY-PARSER
// RETORNA UN MIDDLEWARE QUE PARSEA JSON Y SOLO OBSERVA LAS PETICIONES EN CONDE EL Cnten-Type SEA IGUAL AL TIPO DE OPCIPON
app.use(bodyParser.json());
// PARA RECIBIR DATA COMO x-www-form-urlencoded
app.use(bodyParser.urlencoded({extended: false}));
// AÑADIR A LA APLICACIÓN EL ROUTER
// app.use(router);
// AÑADIR A LA APLICACIÓN A ROUTES Y PASARLE EL SERVIDOR A ROUTES
router(app);
// SE AÑADE A LA APLICACIÓN estatic DE express PARA SERVIR ARCHIVOS ESTATICOS
app.use('/app', express.static('public'));

app.listen(3000);

console.log('La aplicación esta escuchando en http://localhost:3000');
// nodemon server.js
```
`/components/message/network.js`
```js
// ARCHIVO DE RUTAS DEL COMPONENTE DE MESSAGE
const express = require('express');
const router = express.Router();
// SE IMPORTA response.js PARA RESPUESTAS UNIFICADAS
const response = require('../../network/response');

// PARA USAR ROUTER EN LAS PETICIONES
// router.get('/message', function(req, res) {
router.get('/', function(req, res) {
    console.log(req.body);
    // LEER LÑAS CABECERAS
    console.log(req.headers);
    res.header({
      "custom-header": "Nuestro valor personalizado",
      "Cache-Control": "public, max-age=300"
    });
    // res.send('Lista de mensajes');
    response.success(req, res, 'Lista de mensajes', 201)
});

// router.post('/message', function(req, res) {
router.post('/', function(req, res) {
  console.log(req.body);
  console.log(req.query);
  // res.send('Mensaje añadido ' + req.body.text + ' correctamente');
  // res.send() // RESPUESTA VACIA
  // res.status(201).send(`Mensaje añadido ${req.body.text} correctamente`);
  /*res.status(201).send({
    error: '',
    body:'Creado correctamente'
  });*/
  response.success(req, res, 'Creado correctamente', 201)
});

module.exports = router;
```
`/network/routes.js`
```js
// SERVIDOR DE RUTAS
const express = require('express');
const message = require('../components/message/network');

const routes = function(server) {
    server.use('/message', message);
}

module.exports = routes;
```

### 16. Controladores: Definiendo la lógica de negocio
NOTA: Commit `21d1467` en mi repo para ver los cambios en los archivos.

`compoments/message/network.js`
```js
// ARCHIVO DE RUTAS DEL COMPONENTE DE MESSAGE
const express = require('express');
const router = express.Router();
// SE IMPORTA response.js PARA RESPUESTAS UNIFICADAS
const response = require('../../network/response');
const controller = require('./controller');

// PARA USAR ROUTER EN LAS PETICIONES
// router.get('/message', function(req, res) {
router.get('/', function(req, res) {
    console.log(req.body);
    // LEER LAS CABECERAS
    console.log(req.headers);
    res.header({
      "custom-header": "Nuestro valor personalizado",
      "Cache-Control": "public, max-age=300"
    });
    // res.send('Lista de mensajes');
    response.success(req, res, 'Lista de mensajes', 201)
});

// router.post('/message', function(req, res) {
router.post('/', function(req, res) {
  // SE LE MANDA JSON POR CON VALORES DE USER Y MESSAGE CON POSTMAN
  controller.addMessage(req.body.user, req.body.message)
  .then((fullMessage) => {
    response.success(req, res, fullMessage, 201)
  })
  .catch(e => {
    console.log(e)
    response.error(req, res, 'Información invalida', 400, 'Error en el controlador')
  });
});

module.exports = router;
```

Se crea el archivo `components/message/controller.js` para poder manejar la "logica del negocio". Recibe la data del `network.js` de las peticiones `GET`, `POST` y se maneja la logica, en este caso se valida la rección y prueva de errores en caso de no recibir el json correctamente en `POST`
```json
{
	"user": "mack",
	"message": "mensaje"
}
```
Mensaje correcto que regresa `resolve(fullMessage)` cuando se hacen las pruebas con _Postman_
```json
{
    "error": "",
    "message": {
        "user": "mack",
        "message": "mensaje",
        "date": "2020-05-25T16:25:17.911Z"
    }
}
```

```js
function addMessage(user, message) {
    console.log(user);
    console.log(message);
    return new Promise((resolve, reject) => {
        if (!user || !message) {
            console.error('[messageController] No hay usuario o mensaje');
            return reject('Los datos son oncorrectos');
        }
        const fullMessage = {
            user: user,
            message: message,
            date: new Date(),
        }
        console.log(fullMessage);
        resolve(fullMessage);
    });
}
module.exports = {
    addMessage,
};
```


### 17. Almacenando la información en una base de datos
Separar físicamente nuestro código permite una fácil refactorización en los módulos que lo necesiten, así no afectará otros módulos.

Se creará mocks (simulación de una base de datos) para probar nuestras funciones, rutas y servidor.

Para esto se crea el archivo `store.js` en el componente `message`

`backendNode/components/message/network.js`
```js
// ARCHIVO DE RUTAS DEL COMPONENTE DE MESSAGE
const express = require('express');
const router = express.Router();
// SE IMPORTA response.js PARA RESPUESTAS UNIFICADAS
const response = require('../../network/response');
const controller = require('./controller');

// PARA USAR ROUTER EN LAS PETICIONES
router.get('/', function(req, res) {
    // SE IMPORTAN DEL CONTROLADOR controller.js EL MODULO getMessages PARA TRAER LA LISTA DE MENSAJES
    controller.getMessages()
    .then((messageList) => {
        response.success(req, res, messageList, 200)
    })
    .catch(e => {
        response.error(req, res, 'Uncexpected Error', 500, 'e')
    })
});

router.post('/', function(req, res) {
  // SE IMPORTAN DEL CONTROLADOR controller.js EL MODULO addMessages PARA AÑADIR MENSAJE
  // SE LE MANDA JSON POR CON VALORES DE USER Y MESSAGE CON POSTMAN
  controller.addMessage(req.body.user, req.body.message)
  .then((fullMessage) => {
    response.success(req, res, fullMessage, 201)
  })
  .catch(e => {
    console.log(e)
    response.error(req, res, 'Información invalida', 400, 'Error en el controlador')
  });
});

module.exports = router;
```
`/backendNode/components/message/controller.js`
```js
// SE IMPORTA STORE PARA ALMACENAR 
const store = require('./store');
// FUNCION PARA AÑADIR UN MENSAJE
function addMessage(user, message) {
    console.log(user);
    console.log(message);
    return new Promise((resolve, reject) => {
        if (!user || !message) {
            console.error('[messageController] No hay usuario o mensaje');
            return reject('Los datos son oncorrectos');
        }
        const fullMessage = {
            user: user,
            message: message,
            date: new Date(),
        }
        // SE ALMACENA EN store
        store.add(fullMessage);
        resolve(fullMessage);
    });
}
// FUNCION PARA RETORNAR MENSAJES A network.js
function getMessages() {
    return new Promise((resolve, reject) => {
        resolve(store.list());
    });
}

module.exports = {
    addMessage,
    getMessages,
};
```

`/backendNode/components/message/store.js`
```js
// EN EL ARRAY ES DONDE SE GUARDAN TODOS LOS MENSAJES
// ACTUA COMO MOCK DE LA BD
const list = [];

// FUNCION PARA AGREGAR LOS MENSAJES QUE LLEGAN EN controller.js
function addMessage(message) {
    // SE AGREGAN LOS MENSAJES NUEVOS A LA LISTA PARA DESPUES AGREGAR A LOSMENSAJES
    list.push(message);
}
// FUNCION PARA RETORNAR LA LISTA DE MENSAGES, SI ES QUE EXISTEN A controller.js
function getMessage() {
    return list;
} 

module.exports = {
    add: addMessage,
    list: getMessage,
    // get
    // update
    // delete
}
```

## 4. Utilizar una base de datos para definir, modelar, almacenar y recuperar la información de nuestra aplicación
### 18. Tipos de Bases de Datos: Relacionales y No Relacionales

**Bases de Datos Relacionales**: no es una base de datos muy flexible, pero tiene a favor su gran soporte y el enorme desarrollo en herramientas para su uso. Si necesitamos cambiar un valor de un campo debemos hacerlo con todos los campos de nuestra BD, en cambio con NoSQL o No Relacional no es así.

**Bases de Datos No Relacionales**: son de bases de datos sin una tabla fija como las que sí se encuentran en las bases de datos relacionales, lo que permite una alta escalabilidad en ellas. Además, es abierta y por lo tanto flexible a diferentes tipos de datos y no necesita tantos recursos para ejecutarse; de hecho, el hardware necesario no cuesta mucho.

![BD relacionales y no-relacionales](imgs/bd_relacinales_no_relacionales.png)

### 19. Crear y Configurar tu Base de Datos con MongoDB

MongoDB compró **mLab**.

**MongoDB Atlas** es un servicio de bases de datos como servicio que nos permite configurar nuestras bases de datos para entornos de pruebas o producción con diferentes proveedores de nube. Además de todas sus características, Atlas se destaca por ser un servicio mantenido oficialmente por el equipo que desarrolla MongoDB.

**mLab** también era un servicio de bases de datos con Mongo. Pero fue adquirido por MongoDB a inicios del 2019 para darle más fuerza a **MongoDB Atlas** y unir fuerzas con el anterior equipo de **mLab**.

:link: [MongoDB comprará mLab* y su servicio de base de datos en la nube](https://www.silicon.es/mongodb-comprara-mlab-y-su-servicio-de-base-de-datos-en-la-nube-2383965)

Usa **MongoDB Atlas** en lugar de **mLab**

Durante el curso usamos **mLab** para crear nuestra base de datos con MongoDB. Pero el servicio ya no está disponible, así que te recomendamos seguir esta clase para configurar tu base de datos con **MongoDB Atlas**:

:link: [Creación de una BD en MongoAtlas](https://platzi.com/clases/1646-backend-nodejs/22033-creacion-de-una-bd-en-mongoatlas/)

MongoDB está escrito en C++, aunque las consultas se hacen pasando objetos JSON como parámetro. Es algo bastante lógico, dado que los propios documentos se almacenan en BSON. Por ejemplo:

db.Clientes.find({Nombre:“Pedro”});
La consulta anterior buscará todos los clientes cuyo nombre sea Pedro.

MongoDB viene de serie con una consola desde la que podemos ejecutar los distintos comandos. Esta consola está construida sobre JavaScript, por lo que las consultas se realizan utilizando ese lenguaje. Además de las funciones de MongoDB, podemos utilizar muchas de las funciones propias de JavaSciprt. En la consola también podemos definir variables, funciones o utilizar bucles.

Si queremos usar nuestro lenguaje de programación favorito, existen drivers para un gran número de ellos. Hay drivers oficiales para C#, Java, Node.js, PHP, Python, Ruby, C, C++, Perl o Scala. Aunque estos drivers están soportados por MongoDB, no todos están en el mismo estado de madurez. Por ejemplo el de C es una versión alpha. Si queremos utilizar un lenguaje concreto, es mejor revisar los drivers disponibles para comprobar si son adecuados para un entorno de producción.

Nuestro código no cambiará mucho. De hecho, puede que no cambie nada. Solo debes recordar que los nombres de tus bases de datos y clusters deben ser los mismos en el servicio de Atlas y en tu código.

Entrar a al :link: [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) y registrarse en **Start Free** 

1. Crear una BD gratis en AWS
2. Cuando este creada, en el papartado de la derecha en _SECURITY/Network Acces_ se tiene que configurar una IP de la cual se tienen que tener acceso, seleccionar _Add IP Adress_ y seleccionar en el modal la op. _ALLOW ACCES FROM ANYWHARE_
3. Se tiene que configurar un usuario en en el papartado de la derecha en _SECURITY/Database Acces_

![Modal para agregar usuario en MongoDB](imgs/mongodb_create_user_modal.png)

4. Cuando ya este creada, en el papartado de la derecha en _DATA STORAGE/Clusters_ se muestra el boton de **CONNEC** en el que se muestra las diferentes formas en que se puede conectar, copiar el link de las tres posibles maneras,

5. Se tiene que crear la base de datos en **COLLECTIONS** y dar click en Add **My Own Data**  y escribir el nombre de la DB en **DATABASE NAME** y el nombre de la collección en **COLLECTION NAME** 

```
mongodb+srv://USER:<PASSWORD>@cluster0-6lojz.mongodb.net/<NAME_DATABASE>
```


### 20. MongoDB I: Almacenar y leer datos
Instalar en el proyecto :link: [mongoose elegant mongodb object modeling for node.js](https://mongoosejs.com/)
```bash
$ npm i mongoose
```
Se crea el archivo `model.js` en la carpeta del componente _message_ que se encarga del modelo

`model.js`
```js
const mongoose = require('mongoose');
// DE MONGOOSE IMPORTAMOS EL ESCHEMA
const Schema = mongoose.Schema;

// SE LE INDICA A MONGOOSE QUE CLASE DE ESCHEMA DESEAMOS PARA NUESTRO COMPONENTE
const mySchema = new Schema({
    user: String,
    message: {
        type: String,
        required: true,
    },
    date: Date,
});
// CUANDO SE TIENE EL SCHEMMA DEFINIDO, SE CREA EL MODELO EN MONGOOSE
// SE DEFINE EL NOMBRE DE LA TABLA Y EL SCHEMA
const model = mongoose.model('Message', mySchema);

module.exports = model;
```
`store.js`
```js
// EN EL ARRAY ES DONDE SE GUARDAN TODOS LOS MENSAJES
// ACTUA COMO MOCK DE LA BD
// const list = [];
// SE IMPORTA LA DB DE MONGOOSE PARA GUARDAR EN LA DB
const db = require('mongoose');
// SE IMPORTA LA SCHEMMA PARA QUE SE GUARDE EN EL MODELO ESTYABVLECIDO
const Model = require('./model');

// QUE MOONGOOSE UTILIZE LAS PROMESAS DE FORMA MAS SIMPLE(BUENA PRACTICA)
db.Promise = global.Promise;
db.connect('mongodb+srv://db_usr_rodolfo:V7bNFXijjR9iyPxo@cluster0-6lojz.mongodb.net/test', {
    useNewUrlParser: true, // PARA ELIMINAR PROBLEMAS DE CO,PATYIBILIDAD EN CSO DE EL SERVISOR SEA MÁS NUEVO O MAS ANTIGUO
    useUnifiedTopology: true, // RECOMENDACIÓN DE MOOGOOSE
});
console.log('[db] CONECTYADA CON EXITO')

// FUNCION PARA AGREGAR LOS MENSAJES QUE LLEGAN EN controller.js
function addMessage(message) {
    // SE AGREGAN LOS MENSAJES NUEVOS A LA LISTA PARA DESPUES AGREGAR A LOS MENSAJES
    // list.push(message);
    // SE INSTYANCIA LA VBUEVA CLASE DEL MODELO
    const myMessage = new Model(message);
    // SE GUARDA CON EL MODELO EXTENDIDO DE MOONGOSE
    myMessage.save();
}
// FUNCION PARA RETORNAR LA LISTA DE MENSAGES, SI ES QUE EXISTEN A controller.js
async function getMessage() {
    // return list;
    const messages = await Model.find();
    return messages;

} 

module.exports = {
    add: addMessage,
    list: getMessage,
    // get
    // update
    // delete
}
```
`controller.js`
```js
// SE IMPORTA STORE PARA ALMACENAR 
const store = require('./store');
// FUNCION PARA AÑADIR UN MENSAJE
function addMessage(user, message) {
    console.log(user);
    console.log(message);
    return new Promise((resolve, reject) => {
        if (!user || !message) {
            console.error('[messageController] No hay usuario o mensaje');
            return reject('Los datos son oncorrectos');
        }
        const fullMessage = {
            user: user,
            message: message,
            date: new Date(),
        }
        // SE ALMACENA EN store
        store.add(fullMessage);
        resolve(fullMessage);
    });
}
// FUNCION PARA RETORNAR MENSAJES A network.js
function getMessages() {
    return new Promise((resolve, reject) => {
        resolve(store.list());
    });
}

module.exports = {
    addMessage,
    getMessages,
};
```

### 21. MongoDB II: Actualizar datos

Para modificar los mensajes se tiene que crear una función en `components/message/network.js` de una ruta para modificar mensajes.

```js
// ARCHIVO DE RUTAS DEL COMPONENTE DE MESSAGE
const express = require('express');
const router = express.Router();
// SE IMPORTA response.js PARA RESPUESTAS UNIFICADAS
const response = require('../../network/response');
const controller = require('./controller');

// PARA USAR ROUTER EN LAS PETICIONES
router.get('/', function(req, res) {
    // SE IMPORTAN DEL CONTROLADOR controller.js EL MODULO getMessages PARA TRAER LA LISTA DE MENSAJES
    controller.getMessages()
    .then((messageList) => {
        response.success(req, res, messageList, 200)
    })
    .catch(e => {
        response.error(req, res, 'Uncexpected Error', 500, 'e')
    })
});

router.post('/', function(req, res) {
  // SE IMPORTAN DEL CONTROLADOR controller.js EL MODULO addMessages PARA AÑADIR MENSAJE
  // SE LE MANDA JSON POR CON VALORES DE USER Y MESSAGE CON POSTMAN
  controller.addMessage(req.body.user, req.body.message)
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
    // EN req.params.id ES DONDE ESTA LA DATA SOLICITADA
    controller.updateMessage(req.params.id, req.body.message)
    .then((data) => {
        response.success(req, res, data, 200);
    })
    .catch(e => {
        response.error(req, res, 'Error interno', 500, e)
    })
})

module.exports = router;
```
`/components/message/controller.js`
```js
// SE IMPORTA STORE PARA ALMACENAR 
const store = require('./store');
// FUNCION PARA AÑADIR UN MENSAJE
function addMessage(user, message) {
    console.log(user);
    console.log(message);
    return new Promise((resolve, reject) => {
        if (!user || !message) {
            console.error('[messageController] No hay usuario o mensaje');
            return reject('Los datos son oncorrectos');
        }
        const fullMessage = {
            user: user,
            message: message,
            date: new Date(),
        }
        // SE ALMACENA EN store
        store.add(fullMessage);
        resolve(fullMessage);
    });
}
// FUNCION PARA RETORNAR MENSAJES A network.js
function getMessages() {
    return new Promise((resolve, reject) => {
        resolve(store.list());
    });
}
// FUNCION PARA ACTUALIZAR MENSAJE QUE COINCIDA CON EL id
// FUNCION QUE RECIBE DE controller.js EL id, message PROVENIENTES DE LA BD
// SE VERIFICA QUE CONTENGA VALORES LAS VARIABLES
function updateMessage(id, message) {
    return new Promise(async (resolve, reject) => {
        if (!id || !message) {
            reject('Invalid data')
            return false;
        }
        // EN `store.js` SE CREA EL METODO updateText PARA ACTUALIZAR EL MENSAJE
         const result = await store.updateText(id, message)
         resolve(result)
    })
}

module.exports = {
    addMessage,
    getMessages,
    updateMessage,
};
```
`/components/message/store.js`
```js
// EN EL ARRAY ES DONDE SE GUARDAN TODOS LOS MENSAJES
// ACTUA COMO MOCK DE LA BD
// const list = [];
// SE IMPORTA LA DB DE MONGOOSE PARA GUARDAR EN LA DB
const db = require('mongoose');
// SE IMPORTA LA SCHEMMA PARA QUE SE GUARDE EN EL MODELO ESTYABVLECIDO
const Model = require('./model');

// QUE MOONGOOSE UTILIZE LAS PROMESAS DE FORMA MAS SIMPLE(BUENA PRACTICA)
db.Promise = global.Promise;
db.connect('mongodb+srv://db_usr_rodolfo:V7bNFXijjR9iyPxo@cluster0-6lojz.mongodb.net/test', {
    useNewUrlParser: true, // PARA ELIMINAR PROBLEMAS DE CO,PATYIBILIDAD EN CSO DE EL SERVISOR SEA MÁS NUEVO O MAS ANTIGUO
    useUnifiedTopology: true, // RECOMENDACIÓN DE MOOGOOSE
});
console.log('[db] CONECTYADA CON EXITO')

// FUNCION PARA AGREGAR LOS MENSAJES QUE LLEGAN EN controller.js
function addMessage(message) {
    // SE AGREGAN LOS MENSAJES NUEVOS A LA LISTA PARA DESPUES AGREGAR A LOS MENSAJES
    // list.push(message);
    // SE INSTYANCIA LA VBUEVA CLASE DEL MODELO
    const myMessage = new Model(message);
    // SE GUARDA CON EL MODELO EXTENDIDO DE MOONGOSE
    myMessage.save();
}
// FUNCION PARA RETORNAR LA LISTA DE MENSAGES, SI ES QUE EXISTEN A controller.js
async function getMessage() {
    // return list;
    const messages = await Model.find();
    return messages;

}

async function updateText(id, message) {
    // Model.findOne SE ENCARGA DE BUSCAR UNA COINCIDENCIA POR PARTE DE MONGOOSE EN LA BD
    // BUSCANDO POR id
    const foundMessage = await Model.findOne({
        _id: id
    });
    // EL MENSAJE QUE SE ENCUENTRA SE LE PASA EL NUEVO VALOR A LO QUE ESTA ALMACENADO
    foundMessage.message = message;
    // Y SE ESPERA QUE SE GUARDE
    const newMessage = await foundMessage.save();
    // PARA RETORNAR EL VALOR
    return newMessage;
}

module.exports = {
    add: addMessage,
    list: getMessage,
    updateText: updateText,
    // get
    // update
    // delete
}
```
Con _Postman_ se puede ahora hacer `PATCH` a `http://localhost:3000/message/5ecc40d37b70933537ffb25a` con el id del mensaje y actualizar el mensaje
```json
{
	"message": "HOLA"
}
```

### 22. MongoDB III: Consultar datos
Para filtar por por un valor en especifico se le puede pasar el valor a biscar por URL `http://localhost:3000/message?user=NOMBREUSUARIO` que se manda por _Postman_ la petición por **GET**

`/components/message/network.js`
```js
router.get('/', function(req, res) {
    // SE IMPORTAN DEL CONTROLADOR controller.js EL MODULO getMessages PARA TRAER LA LISTA DE MENSAJES
    // BUSCAR POR EL VALOR DE user CON QUERY EN EL REQUEST
    // QUE SE PASA POR LA URL Y SE ALAMACENA EN filterMessage Y SI NO Y SI NO SE ENCUENTRA SE MANDA NULL
    // http://localhost:3000/message?user=NOMBREUSUARIO
    const filterMessage = req.query.user || null;
    /* console.log(req.query.user) */
    controller.getMessages(filterMessage)
    .then((messageList) => {
        response.success(req, res, messageList, 200)
    })
    .catch(e => {
        response.error(req, res, 'Uncexpected Error', 500, 'e')
    })
});
```
`/components/message/controller.js`
```js
// FUNCION PARA RETORNAR/TRAER LOS MENSAJES VIENEN DE network.js
// CON filterUser TRAE POR PARAMETRO EL VALOR DE USUARIO QUE SE QUIERE FILTRAR
// PARA MANDARLO A store
function getMessages(filterUser) {
    return new Promise((resolve, reject) => {
        resolve(store.list(filterUser));
    });
}
```
`/components/message/store.js`
```js
// FUNCION PARA RETORNAR LA LISTA DE MENSAGES, SI ES QUE EXISTEN A controller.js
async function getMessage(filterUser) {
    // return list;
    console.log(filterUser)
    let filter = {} // SE DECLARA OBJETO FILTRO VACIO
    // SI filterUser ES DIFERENTE DE null DECLARADO EN network.js
    if (filterUser !== null) {
        filter = { user: filterUser }
    }
    const messages = await Model.find(filter);
    return messages;
}
```


### 23. MongoDB IV: Eliminar Datos
NOTA: Commit `4410276` de mi repo.

`/components/message/network.js`
```js
router.delete('/:id', function(req, res) {
    controller.deleteMessage(req.params.id)
    .then(() => {
        response.success(req, res, `Mensaje ${req.params.id} eliminado`, 200);
    })
    .catch(e => {
        response.error(req, res, 'Error interno', 500, e);
    })
})
```
`/components/message/controller.js`
```js
function deleteMessage(id) {
    return new Promise((resolve, reject) => {
        if (!id) {
            reject('Id invalido');
            return false;
        }
        store.remove(id)
        .then(() => {
            resolve();
        })
        .catch(e => {
            reject(e);
        })
    })
}

module.exports = {
    addMessage,
    getMessages,
    updateMessage,
    deleteMessage,
};
```
`/components/message/store.js`
```js
async function removeMessage(id) {
    return Model.deleteOne({
        _id: id
    });
}

module.exports = {
    add: addMessage,
    list: getMessage,
    updateText: updateText,
    remove: removeMessage,
}
```

### 24. Gestionar conexiones a la base de datos desde la API

Se refactorizar nuestro código para tener todo organizado de una mejor manera, crearemos un archivo db.js donde tendremos todos los datos de nuestra conexión a la base de datos.

Se crea el archivo `db.js` en la raiz del proyecto y se le traslada lo el codigo para conexión a la BD de mongo que estaba en el archivo `store.js`

`db.js`
```js
// ARCHIVO QUE SE ENCARGA DE LA CONECCIÓN A LA BD DE MONGODB
// SE IMPORTA LA DB DE MONGOOSE PARA GUARDAR EN LA DB
const db = require('mongoose');
// QUE MOONGOOSE UTILIZE LAS PROMESAS DE FORMA MAS SIMPLE(BUENA PRACTICA)
// url = 'mongodb+srv://db_usr_rodolfo:V7bNFXijjR9iyPxo@cluster0-6lojz.mongodb.net/test'
db.Promise = global.Promise;
async function connect(url) {
    await db.connect(url, {
        useNewUrlParser: true, // PARA ELIMINAR PROBLEMAS DE CO,PATYIBILIDAD EN CSO DE EL SERVISOR SEA MÁS NUEVO O MAS ANTIGUO
        useUnifiedTopology: true, // RECOMENDACIÓN DE MOOGOOSE
    });
    console.log('[db] CONECTYADA CON EXITO')
}

module.exports = connect;
```
Y en el archivo `server.js` se importa para hacer la conección
```js
const bodyParser = require('body-parser');
const db = require ('./db');
db('mongodb+srv://db_usr_rodolfo:V7bNFXijjR9iyPxo@cluster0-6lojz.mongodb.net/test');
```


## 5. Uso de entidades para crear aplicaciones escalables
### 25. Escalando la arquitectura: Múltiples entidades
Dentro de la carpeta `componentes` se crea las carpetas para agregar otra entidad. 

+ `user`
    * (1)network.js _SE ENCARGA DE LLEVAR LA LOGICA DE RED_
    * (2)controller.js _LLERARA TODA LA LOGICA DEL CONTROLADOR_
    * (3)store.js _SE ENCARGA DE LA LOGICA DE ALMACENAMIENTO DE DATOS_
    * (4)model.js _EL MODELO DE DATOS_

Los archivos para realizar **POST** y **GET** de la entidad "User" quedaria de la siguient manera.

`network.js`
```js
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
```
`controller.js`
```js
// SE IMPORTA STORE PARA ALMACENAR 
const store = require('./store');
// FUNCION PARA AÑADIR UN USUARIO
function addUser(name) {
    console.log(name);
    if (!name) {
        // SE DEBUELVE UNA PROMESA RECHAZADA
        return Promise.reject('Invalid name');
    }
    const user = {
        name: name,
    }
    // SE ALMACENA EN store/add: addUser,
    // SE DEBUELVE UNA PROMESA
    return store.add(user);
}

function getUser() {
    return new Promise((resolve, reject) => {
        resolve(store.list());
    });
}

module.exports = {
    addUser,
    getUser,
    // updateMessage,
    // deleteMessage,
};
```
`store.js`
```js
// SE IMPORTA LA SCHEMMA PARA QUE SE GUARDE EN EL MODELO ESTYABVLECIDO
const Model = require('./model');

// FUNCION PARA AGREGAR LOS MENSAJES QUE LLEGAN EN controller.js
function addUser(user) {
    const myUser = new Model(user);
    // SE GUARDA CON EL MODELO EXTENDIDO DE MOONGOSE
    return myUser.save();
}

// FUNCION PARA RETORNAR LA LISTA DE MENSAGES, SI ES QUE EXISTEN A controller.js
async function getUser() {
    const users = await Model.find();
    return users;
}

module.exports = {
    add: addUser,
    list: getUser,
    // updateText: updateText,
    // remove: removeMessage,
}
```
`model.js`
```js
const mongoose = require('mongoose');
// DE MONGOOSE IMPORTAMOS EL ESCHEMA
const Schema = mongoose.Schema;

// SE LE INDICA A MONGOOSE QUE CLASE DE ESCHEMA DESEAMOS PARA NUESTRO COMPONENTE
const mySchema = new Schema({
    name: String,
});
// CUANDO SE TIENE EL SCHEMMA DEFINIDO, SE CREA EL MODELO EN MONGOOSE
// SE DEFINE EL NOMBRE DE LA TABLA Y EL SCHEMA
const model = mongoose.model('User', mySchema);

module.exports = model;
```
**NOTA**: Commit "Mod. apuntes _25. Escalando la arquitectura: Múltiples entidades_" en mi repo

### 26. Relacionando nuestras entidades
Para que en los mensajes aparesca el usuario al que pertenece el como en el ejemplo:
```json
"message": [
        {
            "_id": "5eceb9897b62ff568005f21c",
            "user": {
                "_id": "5eceb882457b305419debb4b",
                "name": "primer-usuario",
                "__v": 0
            },
            "message": "MENSAJE DE PRIMER USUARIO",
            "date": "2020-05-27T19:03:37.159Z",
            "__v": 0
        }
```
En este caso para insertar un mensaje rn **POST** por _Postman_ seria así:
```json
{
    "user": "5eceb882457b305419debb4b", // ID DEL USUARIO PREVIAMENTE EN LA BD
    "message": "MENSAJE DE PRIMER USUARIO"
}
```

En `/components/message/model.js` se modifica el **Schema**
```js
const mySchema = new Schema({
    // A user SELE ASIGNA EL TIPO ESPECIAL DE MONGO "Object ID",  SE ESPERA QUE RECIBA COMO USUARIO EL id Y NO string
    user: {
        type: Schema.ObjectId,
        ref: 'User',
    },
    message: {
        type: String,
        required: true,
    },
    date: Date,
});
```
En `components/message/store.js` se modifica la funcion `getMessage` 
```js
async function getMessage(filterUser) {
    return new Promise((resolve, reject) => {
        let filter = {} // SE DECLARA OBJETO FILTRO VACIO
        // SI filterUser ES DIFERENTE DE null DECLARADO EN network.js
        if (filterUser !== null) {
            filter = { user: filterUser }
        }
        Model.find(filter)
            // LO QUE HACE ES BUSCAR DENTRO DE CADA ELELEMTO QUE SE BUSQUE Y SE LE DICE QUE POPULE user
            .populate('user')
            // SE EJECUTA populate
            .exec((error, populated) => {
                if (error) {
                    reject(error);
                    return false;
                }
                // SE REGRESA EN EL resolve LA RELACIÓN ENCONTRADA
                resolve(populated);
            });
    });
}
```

Dentro de la carpeta `componentes` se crea las carpetas para agregar otra entidad. 

+ `chat`
    * (1)network.js _SE ENCARGA DE LLEVAR LA LOGICA DE RED_
    * (2)controller.js _LLERARA TODA LA LOGICA DEL CONTROLADOR_
    * (3)store.js _SE ENCARGA DE LA LOGICA DE ALMACENAMIENTO DE DATOS_
    * (4)model.js _EL MODELO DE DATOS_

En `/components/chat/model.js` se establece el **array** `Schema.ObjectId`
```js
const mongoose = require('mongoose');

// DE MONGOOSE IMPORTAMOS EL ESCHEMA
const Schema = mongoose.Schema;

// SE LE INDICA A MONGOOSE QUE CLASE DE ESCHEMA DESEAMOS PARA NUESTRO COMPONENTE
const mySchema = new Schema({
    users: [{
        type: Schema.ObjectId,
        ref: 'User',
    }]
});
// CUANDO SE TIENE EL SCHEMMA DEFINIDO, SE CREA EL MODELO EN MONGOOSE
// SE DEFINE EL NOMBRE DE LA TABLA Y EL SCHEMA
const model = mongoose.model('Chat', mySchema);

module.exports = model;
```
En `/components/chat/store.js`
```js
// SE IMPORTA LA SCHEMMA PARA QUE SE GUARDE EN EL MODELO ESTYABVLECIDO
const Model = require('./model');

function addChat(chat) {
    const myChat = new Model(chat);
    return myChat.save();
}

function listChats(userId) {
    return new Promise((resolve, reject) => {
        let filter = {};
        if (userId) {
            filter = {
                users: userId
            }
        }
        Model.find(filter)
            .populated('users')
            .exec((err, populated) => {
                if (err) {
                    reject(err);
                    return false;
                }
                resolve(populated);
            })
    })
}

module.exports = {
    add: addChat,
    list: listChats,
}
```

En `/components/chat/controller.js`
```js
// SE IMPORTA STORE PARA ALMACENAR 
const store = require('./store');

function addChat(users) {
    //  SE COMPRUEBA SI HAY USUARIOS Y SI LOS USUARIOS SON UN ARRAY
    if (!users || !Array.isArray(users)) {
        return Promise.reject('Invalid user list');
    }
    const chat = {
        users: users,
    }
    return store.add(chat);
}

function listChats(UserId) {
    return store.list(userId);
}

module.exports = {
    addChat,
    listChats,
}
```
En `/components/chat/network.js`
```js
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

```
Borra los mensajes de la base de datos.   
Ten creados dos usuarios en la base de datos.   
Ahora ve a crear un chat nuevo (**POST**) y debe ser un _body JSON_ así:   
```json
{
    "users": [
        "idDelUser1",
        "idDelUser2"
    ]
}
```
Para crear un **chat**
```json
{
    "users": [
        "idDelUser1",
        "idDelUser2"
    ]
}
```
Luego, ve a crear un mensaje (**POST**), a diferencia de la versión anterior, ahora se de le debe agregar el `id` del _chat_ correspondiente de la creación que hicimos.
```json
{
    "chat": "idChat",
    "user": "idUser1",
    "message": "mensaje"
}
```
Ahora se pueden ahí crear más mensajes.

Luego para hacer el **GET** de chat, _se debe poner el ID del User en la URL: `http://localhost:3000/chat/userId`

### 27. Cómo recibir ficheros desde NodeJS
Para subir archivos se puede hacer por el metodo de `Multipart Form` o `form-data` en _Postman_ y las llaves se pueden seleccionar como si fueran `Text` o `File` 

Se utiliza **multer** para subir archivos a través de nuestros chats; se encarga de todo lo que tanga que ver con la transmisión de archivos, gestión de tipo.
:link: [npm multer](https://www.npmjs.com/package/multer)
```bash
$ npm i multer
```
Para guardar ahora con **file** se tiene que hacer de la siguiente forma el **message** por el metodo de `Multipart Form` o `form-data` en _Postman_
```json
{
    "chat": "idChat",
    "user": "idUser1",
    "message": "mensaje"
    "file": "string_del_archivo"
}
```
![Guardar via form data con archivo](imgs/guardar_via_form_data_con_archivo.png)


En el archivo `/components/message/model.js` se tiene que modifcar el schema en mongoose
```js
const mongoose = require('mongoose');
// DE MONGOOSE IMPORTAMOS EL ESCHEMA
const Schema = mongoose.Schema;
// SE LE INDICA A MONGOOSE QUE CLASE DE ESCHEMA DESEAMOS PARA NUESTRO COMPONENTE
const mySchema = new Schema({
    // A user SELE ASIGNA EL TIPO ESPECIAL DE MONGO "Object ID",  SE ESPERA QUE RECIBA COMO USUARIO EL id Y NO string
    chat: {
        type: Schema.ObjectId,
        ref: 'Chat',
    },
    user: {
        type: Schema.ObjectId,
        ref: 'User',
    },
    message: {
        type: String,
        required: true,
    },
    date: Date,
    file: String,
});
// CUANDO SE TIENE EL SCHEMMA DEFINIDO, SE CREA EL MODELO EN MONGOOSE
// SE DEFINE EL NOMBRE DE LA TABLA Y EL SCHEMA
const model = mongoose.model('Message', mySchema);

module.exports = model;
```
En el archivo `/components/message/store.js` la funcion `addMessage`
```js
function addMessage(message) {
    // SE AGREGAN LOS MENSAJES NUEVOS A LA LISTA PARA DESPUES AGREGAR A LOS MENSAJES
    // list.push(message);
    // SE INSTYANCIA LA VBUEVA CLASE DEL MODELO
    const myMessage = new Model(message);
    // SE GUARDA CON EL MODELO EXTENDIDO DE MOONGOSE
    myMessage.save();
}
```
En el archivo `/components/message/controller.js` se modifica la funcion `addMessage` para agregar el archivo `file`
```js
function addMessage(chat, user, message, file) {
    return new Promise((resolve, reject) => {
        if (!chat || !user || !message) {
            console.error('[messageController] No hay chat, usuario o mensaje');
            return reject('Los datos son oncorrectos');
        }
        let fileUrl = '';
        if (file) {
            fileUrl = `http://localhost:3000/app/files/${file.filename}`
        }

        const fullMessage = {
            chat: chat,
            user: user,
            message: message,
            date: new Date(),
            file: fileUrl,
        }
        // SE ALMACENA EN store
        store.add(fullMessage);
        resolve(fullMessage);
    });
}
```
En el archivo `/components/message/network.js` se modifica el metodo **POST** para poder agregar un archivo `file` y es en donde se tiene que importar `multer` 
```js
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
// ...
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
```


### 28. Guardar el fichero en el servidor
La información que tiene `file.req`
```json
{
  fieldname: 'file',
  originalname: 'mex_twitter_bash.png',
  encoding: '7bit',
  mimetype: 'image/png',
  destination: 'public/files/',
  filename: 'ddb98f2fecff19b0f2b20d2894026c1c',
  path: 'public/files/ddb98f2fecff19b0f2b20d2894026c1c',
  size: 298828
}
```
**NOTA**: Commit `Mod. apuntes _Mod. apuntes _24. Gestionar conexiones a la base de datos desde la API__` en mi repo para ver los cambios en los archivos.

## 6. Conocer el protocolo de websockets, e implementar comunicación cliente/servidor con SocketIO.
### 29. WebSockets: Qué son, por qué son interesantes y cómo usarlos

**Websocket**
>Es un protocolo de comunicacion en tiempo real que crea un tunel entre un cliente y un servidor y que soporta multiples clientes conectados al mismo tunel.

>WebSocket es una tecnología que proporciona un canal de comunicación bidireccional y full-duplex sobre un único socket TCP. Está diseñada para ser implementada en navegadores y servidores web, pero puede utilizarse por cualquier aplicación cliente/servidor.

### 30. Manejo de Websockets con NodeJS
Se instala :link: (npm socket.io)[https://www.npmjs.com/package/socket.io] `npm i socket.io`
Se crea el archivo `socket.js` ala altura de `package.json`
```js
```

```js
```


### 31. Conectar la API al servidor de WebSockets


## 7. Revisión de lo aprendido, y próximos pasos
### 32. Revisión y próximos pasos


### 33. Tips para escalar nuestro 





































































































































