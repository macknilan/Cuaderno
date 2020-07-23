
# Curso Práctico de Node.js
:octocat: :link: [Repo del curso en mi repo](https://github.com/macknilan/proyecto-backend-node-platzi) las clases en los commits

(RE TOMAR ESTE CURSO)

## 1. Introducción al proyecto del curso y su arquitectura
### 1. Arquitectura de un backend complejo

![NODEJS ARQUITECTURA APLICACIÓN](imgs/nodejs_arquitectura_aplicación.png)

+ PRIMER NIVEL DE CARPETAS
    + Store(archivo de almacenamiento, logica para acceso a la BD) es accesible desde toda la aplicación. Tiene que estar diaponible desde todos los componentes
    + Network, Tiene que estar diaponible desde todos los componentes para que todas las respuestas sean mogeneas y coherentes ysalgan desde un solo lado.
    + Configguración, Sea globla para todos los componentes
+ MICRO-SERVICIO
    + Network que se encarga de comunicar con los servicios de rutas
    + Controller, que se dedica que y como va pasar, es la logica de nuestra aplicación
    + Secure, se encarga que todas las reglas se seguridad se cumplan
+ index.js Es un archivo para cada componente donde se establece como se interactura con el micro-servicio y se expone hacia afuera.

*NOTA*

### 2. Estructuras de datos para nuestro proyecto

![Propuesta de modelo MER](modelo er-propuesto.jpg)

## 2. Creando la estructura principal
### 3. Estructura inicial del proyecto: API y rutas

Estructura principal del proyecto
```bash
├── api # CARPETA CONDE ESTARAN TODOS LOS MICRO-SERCICIOS
│   ├── components # CARPETA DONDE DE LOS COMPONENTES 
│   │   └── user # COMPONENTE USER
│   │       └── network.js # ARCHIVO DONDE SE RECIBEN TODAS LAS PETICIONES(GET,POST...) PARA EL COMPONENTE
│   └── index.js # ARCHIVO QUE SE ENCARGA DE RUTEAR LOS REQUESTS/RESPONSE HACIA LOS COMPONENTES
├── config.js # ARCHIVO QUE TIENE UN OBJETO CON VARIABLES DE ENTORNO PARA LA APP
├── network # TODO LO QUE SE NECESITE PARA LA RED
│   └── response.js # ARCHIVO QUE SE ENCARGA DE LAS RESPUESTAS(SUCCES/ERROR) UNIFORME PARA LA APP 
├── package.json
├── package-lock.json
└── README.md

```

**NOTA**: EN CASO DE QUE LA DIRECCION YA ESTE EN USO(PUEDE SER QUE POR QUE NO SE CERRO BIEN)

```bash
Error: listen EADDRINUSE: address already in use :::3000
```
La forma mas rapida es que se cierre el proceso **PID** del puerto **3000** buscandolo
```bash
sudo lsof -i :3000
# SALIDA
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
node    12585 mack   21u  IPv6 269162      0t0  TCP *:3000 (LISTEN)
```
Despues matando el número de PID
```bash
sudo kill -9 12585
```

### 4. Aislar el código de la base de datos

**NOTA**: Ejecutar la app `nodemon api/index`

Se crea una carpeta nueva `store` al nivel de `package.json` que tiene la logica de CRUD para `user` para `dummy.js` de ejemplo

Se crea el archivo `controler.js` tiene acceso al `network.js` de `user` dentro del componente `user` que tiene como objetivo usar la BD `dummy.js` y determinar que accion del CRUD con parametros se tiene que realizar.

`/proyecto-backend-node-platzi/store/dummy.js`
```js

const db = {
    "user": [
        {id: 1, name: "Mack"}
    ],
};

function list(tabla) {
    return db[tabla];
}

function get(tabla, id) {
    let cole = list(tabla);
    return col.filter(item => item.id === id)[0] || null;
}
// PARA ACTUALIZAR/INSERTAR
function upsert(tabla, data) {
    db[collection].push(data)
}

function remove(tabla, id) {
    return true;
}

module.exports =  {
    list,
    get,
    upsert,
    remove,
}
```
`/proyecto-backend-node-platzi/api/components/user/crontroller.js`
```js

const store = require('../../../store/dummy');

// user ES ELPARAMETRO A BUSCAR EN LA BD
const TABLA = 'user';

function list() {
    return store.list(TABLA);
}

module.exports = {
    list,
};
```
`proyecto-backend-node-platzi/api/components/user/network.js`
```js
const express = require('express');

const response = require('../../../network/response');
const Controller = require('./crontroller')

const router = express.Router();

router.get('/', function (req, res) {
    const lista = Controller.list();
    response.success(req, res, lista, 200);
})

module.exports = router;
```



### 5. Rutas para usuarios
Se crea el archivo `index.js` dentro del componente `user` para hacer la exportación de los controladores.

A `/api/components/user/crontroller.js` se convierte a una funcion que se exporta como modulo directamente para poder pasarle valores por parametros y realise cualquier accion de CRUD en la BD que le pasen los componentes

En `store` el archivo `dummy.js` las funciones se convierten en funciones asincronas para poder manejar los _succes_ y _error_ en el archivo `network.js` en donde se crean nuevas rutasy de igual manera en `api/components/user/crontroller.js`


**NOTA**: Commit "Mod. apuntes _5. Rutas para usuarios_" en mi repo.
**NOTA**: :octocat: [Repo de curso clase 5](https://github.com/CodingCarlos/proyecto-backend-node-platzi/tree/664659ff76b1f88feb95f1b4538824bc54b7bc09)

### 6. Documentación de nuestra API

Para poder insertar/actualizar se :link: [npm body-parser](https://www.npmjs.com/package/body-parser) para poder parsear el formato/archivo _json_ y se importa en el `index.js` para que lo use la `app.use(bodyParser.json())`

> Node.js body parsing middleware. Parse incoming request bodies in a middleware before your handlers, available under the req.body property.

```bash
$ npm i body-parser
```

Para insertar nuevos uauarios se se tienen que generar nuevos _id_ para los cual se instala el paquete de :link: [npm nanoid](https://www.npmjs.com/package/nanoid) y se ocupa en el _componente user_ en `controller.js` por que ahí es donde se tiene que generar un `id` nuevo y no repetido para cuando se inserte el nuevo usuario. `consts nanoid = require('nanoid')`

> A tiny, secure, URL-friendly, unique string ID generator for JavaScript.

```bash
$ npm i nanoid
```

Para realizar la documentación una opción es hacer la con :link: [Homa page Swaffer](https://swagger.io/) con ayuda de su :link: [Swagger Edditor](http://editor.swagger.io/) 

> Simplify API development for users, teams, and enterprises with the Swagger open source and professional toolset. Find out how Swagger can help you design and document your APIs at scale.

Para implementar Swagger con nodeJS en el proyecto se instala [Swagger UI Express NPM](https://www.npmjs.com/package/swagger-ui-express)
```bash
$ npm i swagger-ui-express
```
Swagger Editor nos ayuda para realizar la documentación de la API, y se puede trabajar con el ejemplo que viene por defecto en su página del lado derecho para ayudar a documentar el del proyecto.

Cuando el archivo creado esta como se desea para documentar nuestra API se guarda
![exportar swagger de editor a json](imgs/exportar_swagger_de_editor_a_json.png)

El cual se guarda ya convertido en `/api/components/swagger.json` y se importa _swagger_ para que se pueda ocupar en la app

Se importa y se instala en `/api/index.js` para que se pueda servir en la direccion `localhost:3000/api-docs`

![Ejemplo de swagger en localhost](swagger_ejecutandose_localhost.png)

**NOTA**: Commit Mod. apuntes NodeJS Paractico _6. Documentación de nuestra API_ en mi repo.


## 3. Autenticación basada en tokens
### 7. JWT: Gestión de acceso
:link: [JSON Web Tokens](https://jwt.io/)

Un usuario identificado y autentificdo pueda modificar la información

Ejemplo: El usuario logeado solo puede modificar su información y nadie más.

Se tiene que añadir una capa de autentificación

**JWT** es un estándar de la industria que nos permite manejar demandas de información entre dos clientes.

Un _JSON Web Token_ es un estandar que nos permite generar demandas entre _2 clientes de manera segura_.

- Un **JWT** está encriptado, pero tiene 3 partes principales divididas por **“.”** (punto)
    + **Header**: Contiene los archivos de configuración (el tipo y el algoritmo de encriptación)
    + **Payload**: Guarda la información de nuestros usuarios
    + **Signature**: es la firma que contiene el header códificado más el payload códificado, para poder dar acceso a un contenido, éste deberá de ser firmado con un secret, que es la clave secreta con la que se firman los tokens, misma que sólo la deberá de conocer el backend.

- Dentro del **payload** tenemos información que puede ser relevante para la autorización tal como:
    + La expiración
    + Id’s
    + Nombres
    + etc

    Es importante saber que los **JWT** acabarán firmando mucha parte de la comunicación, por lo que no es recomendable que mucha información viaje, ésto puede acabar alentando tu aplicación.


### 8. Autenticación: registro

Se tiene que crear usuarios para luego hacer login de estos usuarios y cuando se hace login se autentican y usar los tokens de autentificación.

Se crea otro nueva carpeta de componentes `auth` y dentro se crea el archivo `index.js` que es donde se esta el controlador de usuario en donde se inserta de forma automatica donde queremos que sea el almacenamiento.

Tembien se crea el archivo `controller.js` para crear autentificaión que tiene que funcionar cada ves que se crea un usuario; por esto se tiene que modificar `controller.js` en el componente _user_ en la funcion `function upsert(body) {` 

Para comprobar se tienen que hacer una peticion `GET` por medio de _Postman_ a `http://localhost:3000/api/user` para ver el/los usuarios que estan dados de alta en el store/dummy

Da como respuesta
```json
{
    "error": false,
    "status": 200,
    "body": [
        {
            "id": "1",
            "name": "Mack"
        }
    ]
}
```
Para añadir un suario a store/dummy a `http://localhost:3000/api/user`
```json
{
    "name": "Mack",
    "username": "nomackayu",
    "password": "123456"
}
```
Con el `console.log(db)` del archivo `dummy.js` da como respuesta cuando se hace un *POST* exitoso
```js
{
  user: [ { id: '1', name: 'Mack' } ],
  auth: [
    {
      id: '3iJY2uLp3FnejRGcxgm0A',
      username: 'user-name-usuario_2',
      password: '123456'
    }
  ]
}
{
  user: [
    { id: '1', name: 'Mack' },
    {
      name: 'nombre_usuario_2',
      username: undefined,
      id: '3iJY2uLp3FnejRGcxgm0A'
    }
  ],
  auth: [
    {
      id: '3iJY2uLp3FnejRGcxgm0A',
      username: 'user-name-usuario_2',
      password: '123456'
    }
  ]
}
```
**NOTA**: :octocat: [Clase 8: Autenticación 1: Registro - Repo proyecto](https://github.com/CodingCarlos/proyecto-backend-node-platzi/commit/a01e5830567dfd176cb749ea9b4d900737e804c0)

**NOTA**: :octocat: Commit mi repo "Mod. apuntes NodeJS Paractico _8: Autenticación 1: Registro_"

### 9. Autenticación: login

Primero se tiene que hacer el login y después cifrar las contraseñas

Se modifica `/api/components/auth/controller.js` para poner una funcion "login" en esta funcion se gerea el "**token**" paa hacer login/autenticar al usuario que a su ves hace el _query_ en _store/dummy.js_ que es la funcion _query_

Se crea el archivo para poder acceder a la funcion "login" `/login` y para esto se crea el router `router.post('/login', function(req, res) {`

hasta aqui se puede comprobar un usuario con haciendo POST `http://localhost:3000/api/user`
```json
{
    "name": "nombre_usuario_3",
    "username": "user-name-usuario_3",
    "password": "123456"
}
```
En el archivo `/api/index.js` se instala la ruta del complemento _auth_ añadiendo las lineas
```js
const auth = require('./components/auth/network');
app.use('/api/auth', auth);
```
Primero se crea un usuario nuevo para depues acceder a el desde `http://localhost:3000/api/auth/login` con
```json
{
    "username": "user-name-usuario_3",
    "password": "123456"
}
```
Y debe d regresar 
```json
{
    "error": false,
    "status": 200,
    "body": {
        "id": "d6oGnCw05_toD4viyNhvY",
        "username": "user-name-usuario_3",
        "password": "123456"
    }
}
```
Pagra **generar el token** se tiene que crear una nueva carpta(en raiz de la app)**auth** con el archivo `index.js` se tiene que instalar el archivo :link: [npm jsonwebtoken](https://www.npmjs.com/package/jsonwebtoken)

> An implementation of [JSON Web Tokens](https://tools.ietf.org/html/rfc7519)

```bash
$ npm i jsonwebtoken
```
Y la funcion **sing** del archivo `proyecto-backend-node-platzi/auth/index.js` se importa a `/api/components/auth/controller.js`

Se registra un nuevo usuario y al moment de hacer login(POST) a `http://localhost:3000/api/auth/login` tienen que regresar

```json
{
    "error": false,
    "status": 200,
    "body": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IllwbVVmXy05V2k0SG1adWwyb0lnRyIsInVzZXJuYW1lIjoidXNlci1uYW1lLXVzdWFyaW9fMyIsInBhc3N3b3JkIjoiMTIzNDU2IiwiaWF0IjoxNTkwOTgwNjM5fQ.lWKNXpRGJY_QL2G58GmKx5cCk2deIxyK6bYJhgt4znc"
}
```
**NOTA**: :octocat: [9: Autenticación 2: Login](https://github.com/macknilan/proyecto-backend-node-platzi/commit/bb162c83db67b784b28a8d7cee9581e1fab27215)
**NOTA**: :octocat: Commit en mi repo Mod. apuntes NodeJS Paractico _9: Autenticación 2: Login_



### 10. Autenticación: cifrar contraseñas para evitar problemas de seguridad

:link: [Github  nodejs/node-gyp ](https://github.com/nodejs/node-gyp)

Se tienen que instalar la libreria :link: [NPM bcrypt](https://www.npmjs.com/package/bcrypt) para que las contraseñas se almacenen encriptadas/hasheadas y tambien se puedan leer para poder hacer login a la app
```bash
$ npm i bcrypt
```
La logica marca que se tiene que instalar en el componente **auth** en el controlador(`controller.js`) por que es en esta funcion donde se manda a almacenar la contraseña y se lee para comprobar autenticidad.

(EjecutaR `nodemon api/index`) Se crea un usuario en `http://localhost:3000/api/user` y en consola se tiene que mostrar
```bash
{
  user: [ { id: '1', name: 'Mack' } ],
  auth: [
    {
      id: 'GrW4MyGQbKdH6Q6-MrNhl',
      username: 'user-name-usuario_3',
      password: '$2b$05$vclsT1EkXxH/4I8S1JmClO2kaOUkRl.RCxvFsiVjahlf4xoCeJmQG'
    }
  ]
}
{
  user: [
    { id: '1', name: 'Mack' },
    {
      name: 'nombre_usuario_3',
      username: 'user-name-usuario_3',
      id: 'GrW4MyGQbKdH6Q6-MrNhl'
    }
  ],
  auth: [
    {
      id: 'GrW4MyGQbKdH6Q6-MrNhl',
      username: 'user-name-usuario_3',
      password: '$2b$05$vclsT1EkXxH/4I8S1JmClO2kaOUkRl.RCxvFsiVjahlf4xoCeJmQG'
    }
  ]
}
```
El proceso para comrobar si la contraseña con la entra el usuario es la misma que esta "_hasheada_" en la BD en la funcion `login` del mismo archivo `api/components/auth/controller.js` se implementa `bcrypt` 

1. Cuando se registra usuario se guarda su contraseña _hasheada_
2. Cuando el usuario entra a `api/auth/login` la contraseña que inserta se _hashea_ para comparar con la contraseña _hasheada_ que esta lamancenada
3. bcrypt hace la comparacion y si es correcta la contraseña entra a sistema

Y la respuesta del POST a `api/auth/login` regresa el body _hasheado_ con la herramienta **bcrypt**
```bash
{
    "error": false,
    "status": 200,
    "body": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJaTE9PbUpCSDRSR1NnX3Z5Q0x5ayIsInVzZXJuYW1lIjoidXNlci1uYW1lLXVzdWFyaW9fMyIsInBhc3N3b3JkIjoiJDJiJDA1JDhRZi9EOGJEbFVCNVEzNWwxa0lCUi5WSHNia2xXUi9WRjNNSjE5UHI3MHFER3l3VnF6TUVXIiwiaWF0IjoxNTkwOTg0MjUzfQ.yC65y183XZ6kmsLEMqe-k0atcchBOG4RAQ-OU4xU3JQ"
}
```
**NOTA**: Commit en mi repo `Mod. apuntes NodeJS Paractico _10. Autenticación: cifrar contraseñas para evitar problemas de seguridad_`

**NOTA**: :octocat: Commit mi repo de proyecto [10: Autenticación 3: Cifrar contraseñas](https://github.com/macknilan/proyecto-backend-node-platzi/commit/d47d2487349eae872d74bc1337b897ab4e0d9d1c)

### 11. Autenticación: gestión de permisos

**FUNCIONES CON NOMBRE FACILITAN AL MOMENTO DE HACER DEGUG**

El objetivo es no dejar pasar el usuario a la logica del componente si no se tienen  permisos.

Dentro del _componente user_ se crea el archivo `secure.js` en el cual se creará un **middleware** para exportarlo

+ :link: [Bearer Authentication](https://swagger.io/docs/specification/authentication/bearer-authentication/)
+ :link: [Authorization MDN web docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)


En el archivo se `/proyecto-backend-node-platzi/config.js` se configura que se obtenga la variable de ambiente si no toma una por defecto

Para comprobar si funciona se rienen que crear un usuario en `http://localhost:3000/api/user` despues se logea con ese usuario en `http://localhost:3000/api/auth/login` posteriormente se hace **PUT** a `http://localhost:3000/api/user` añadiendo parametro `id` con un `id` diferente
```json
{
    "id": "2", //ES DIFERENTE CON EL CUAL SE GUARDO
    "name": "nombre_usuario_3",
    "username": "user-name-usuario_3",
    "password": "123456"
}
```
 y se comprueba que lo cambió. ESTO NO DEBERIA DE SUCEDER POR QUE NO ESTA EL TOKEN AÑADIDO, Y SE CORREGIRÁ

**NOTA:** Commit en mi repo "Mod. apuntes NodeJS Paractico _11. Autenticación: gestión de permisos_"
**NOTA:** :octocat: Commit mi repo de proyecto [Clase 11: Autenticación 4: Descifrar el token](https://github.com/macknilan/proyecto-backend-node-platzi/commit/eaa2356247f39c7753f85ea3bf09ec5059e76e3e)

### 12. Comprobar verificación con token

Comentarios importantes a este punto:

En el replace de _Bearer_ se esta haciendo como `replace(“Bearer”, “”)` pero por defecto cuando se manda un token con este formato, por defecto se le agrega un espacio en el medio. Digamos que tu token es **“qwerty12345”** al servidor va a llegar como **“Bearer qwerty12345”** por ende para obtener correctamente el token y que no explote tenemos que hacer un replace con _Bearer_ y un espacio, osea `replace("Bearer ", “”)`.

A este punto cuando hagan el **update** les va a crear un usuario nuevo. Esto esta bien por que en el metodo upsert definido en nuestro dummy simpletemente hacemos un push sobre nuestra tabla, no hacemos primero una **buesqueda por id** si el mismo nos viene y actualizamos o en caso contrario creamos un nuevo **“record”**. Esto seguro va a estar resuelto cuando se use un store en si mismo pero si quieren arreglarlo por ahora pueden _agregar un metodo de busqueda por id dentro de la tabla_ aunque como tip deberia la tabla en vez de ser un array ser un hash, donde cada key es un id, asi la busqueda se hace mas optima.

Les puede pasar que algunas _exceptions_ que les salgan, lleguen hasta el cliente en la response.


Se tienen que hacer la verificación del token que le pertenesca al usuario, para esto en el archivo `/proyecto-backend-node-platzi/auth/index.js` en la repuesta de la función `decodeHeader` se comprueba sy es o no propio el token


En `/api/components/user/network.js` se agrega el middleware que se creo en `/api/components/user/secure.js` en el router `router.put('/',secure('update'), upsert);` 


El token se obtiene cuando se hace login del usuario creado y se muestra en la etiqueta "body"; y es el que se manda por el token 
```json
{
    "error": false,
    "status": 200,
    "body": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Imw4dl9iYTUxSDdMeDB2VllXc3ZFdSIsInVzZXJuYW1lIjoidXNlci1uYW1lLXVzdWFyaW9fMyIsInBhc3N3b3JkIjoiJDJiJDA1JHduMVNpMXZvcDljS0NtaVp5MlhHdHUwbXhCLmRpMVRObzhxMVViY255WFVpM01KN0ZoQ2l1IiwiaWF0IjoxNTkxMDQwMzQ5fQ.4Aw06S0Kv8ZpsGzFNwHZaCX2nVeF54k_OdqV6etK7VQ"
}
```
Para mandar el token se tienen que madar la funcion de autentificación con _Postman_

![Mandar el token "Bearer" con postman](imgs/mandar_token_postman_bearer.png)

Ahora para editar(con PUT en `http://localhost:3000/api/user`) el usuario creado con su token, se tiene que editar con el token y con el id que se le asigno automaticamente.

![editar user con token y id postman bearer](imgs/editar_user_con_token_y_id_postman_bearer.png)

**NOTA:** Commit en mi repo "Mod. apuntes NodeJS Paractico _12: Autenticación 5: Comprobar verificación con token_"
**NOTA:** :octocat: Commit mi repo de proyecto [12: Autenticación 5: Comprobar verificación con token](https://github.com/macknilan/proyecto-backend-node-platzi/commit/068ba34ff4292d0afe7460fcb40819ca1dd18387)

### 13. Gestión avanzada de errores: Throw

Es un middleware para mejar errores

Para gestionar los errores más personalisados y desde un solo lugar y al mismo tiempo que no se puestre información del sistema cuando ocurren errores, se tiene que crear el archivo `errors.js` dentro de la carpeta `network`

Para que funcione se tiene que instalar/usar en al api `/api/index.js` 
```js
app.use(erros);
```
`/network/errors.js`
```js
const response = require('./response');

function errors(err, req, res, next) {
    console.error('[error]', err);
    // CONFIGURACIÓN DE LOS ERRORES QUE DESEAN CONFIGURAR
    const message = err.message || 'Error interno';
    const status = err.statusCode || 500;

    response.error(req, res, message, status);
}

module.exports = errors;
```
Se crea un carpeta en en raiz del proyecto **utils** en la cual estaran las todas las tulidades para toda la _app_ y que no pertenesen a nungún componente, y se crea el archivo `errors.js` para mostrar errores personalisados en toda la app

Para implementar como un ej. es el archivo `/auth/index.js` donde se arroja un nuevo error
```js
// de esto
throw new Error('No puedes hacer esto');
// a esto
throw error( 'No puedes hacer esto', 401);
```
**NOTAS DE CLASE**  
Este tipo de utilidad se debe de implmentar en todo el la app  
`next()` permite avanzar al siguiente middleware que se definió en la app. De ese modo, la app puede seguir su ejecución sin problemas.

En el caso que explica el profesor sucede lo siguiente:

1. Se define un middleware para manejar errores y lo posiciona como el **último middleware** a ser aplicado en el archivo `/api/index.js` -> `app.use(erros);`
2. En el network se controlaba cada error usando “catch” pero el profesor lo reemplaza por **“next”**. Lo que significa: “no maneje el error acá, solo siga al siguiente middleware”
3. La app pasa por los middlewares restantes hasta que llega al middleware de error
4. Cuando llega el middleware de error, este se encarga de manejar el error que se lanzó y retornar al respuesta correcta a la petición HTTP realizada

Este enfoque es muy útil, porque el middleware de error podrá manejar cualquier tipo de error que llegue a la app y siempre retornar una respuesta adecuada para cada petición.


**NOTA:** Commit en mi repo "Mod. apuntes NodeJS Paractico _13: Gestion avanzada de errores_"
**NOTA:** :octocat: Commit mi repo de proyecto [13: Gestion avanzada de errores](https://github.com/macknilan/proyecto-backend-node-platzi/commit/95ab108724c124f469be5804db41b18c3581174a)



## 4. Almacenando datos: MySql
### 14. Base de datos real: MySQL
Se tiene que instalar el modulo mysql para que sirva de controlador con la BD

:link: [mysql NPM](https://www.npmjs.com/package/mysql)

```bash
$ npm i mysql
```

Para guardar la configuración con la conexción a la BD MySql se crea el archivo `mysql.js` en la carpeta **store**

En localhost instalo MySQL

```bash
CREATE USER 'nodejs_platzi_2020'@'localhost' IDENTIFIED BY 'curso practico nodejs';
CREATE DATABASE nodejsplatzi2020;
GRANT CREATE, DELETE, DROP, EXECUTE, INSERT, SELECT, UPDATE ON database.nodejsplatzi2020 TO 'nodejs_platzi_2020'@'localhost';
```

- Datos para la BD del Curso practico de NodeJS
    + USER: nodejs_platzi_2020
    + PWD: curso practico nodejs
    + DBNAME:nodejsplatzi2020
    + HOST: localhost:3306


En los archivos `api/components/auth/index.js` y `api/components/user/index.js` se cambia la varia `store` para que se conecte a _mysql_ -> `const store = require('../../../store/mysql');`

Tabla **user**
```sql
CREATE TABLE `user` (
  `id` varchar(64) NOT NULL,
  `username` varchar(32) DEFAULT NULL,
  `name` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```
Insertar datos en la tabla **user**
```sql
INSERT INTO `nodejsplatzi2020`.`user`
(`id`, `username`, `name`)
VALUES (1, 'macknilan', 'rodo');
```

**NOTA:** Commit en mi repo "Mod. apuntes NodeJS Paractico _14. Base de datos real: MySQL_"
**NOTA:** :octocat: Commit mi repo de proyecto [14. Base de datos real: MySQL](https://github.com/macknilan/proyecto-backend-node-platzi/commit/17f319715e70bb14307dfd1a0413fadffa3ca229)


### 15. Completando la base de datos

Tabla **auth**
```sql
CREATE TABLE `auth` (
  `id` varchar(64) NOT NULL,
  `username` varchar(32) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

Para comprobar que funcione se hace con _Postman_ GET a `http://localhost:3000/api/user` para que traiga los usuarios en la BD

Y tiene que dar como respuesta
```json
{
    "error": true,
    "status": 200,
    "body": [
        {
            "id": 1,
            "username": "macknilan",
            "name": "rodo"
        }
    ]
}
```
Para hacer insert de un usuario nuevo se hace **PUT** en `http://localhost:3000/api/user` con el cuerpo json
```json
{
    "name": "nombre_usuario_3",
    "username": "user-name-usuario_3",
    "password": "123456"
}
```
Se hace login con el usuario creado con **POST** `http://localhost:3000/api/auth/login`
```json
    {
        "username": "user-name-usuario_3",
        "password": "123456"
    }
```
Contesta con el **token** de autorización 
```json
{
    "error": true,
    "status": 200,
    "body": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImlJOENSY3lDUG5KbVhUb1RqRWpTNCIsInVzZXJuYW1lIjoidXNlci1uYW1lLXVzdWFyaW9fMyIsInBhc3N3b3JkIjoiJDJiJDA1JGVaRUpCc3dwNFVEOGs2aHM0QWZHL2VzNzkzUnJaRVBvdHNVcko2anFIbnBJM3h6bi9SSDVTIiwiaWF0IjoxNTkxMTU2MjIzfQ.ryY5pr2YSFFN8d1GJgmwb-n1VZIAzASAJWLumkSrxxE"
}
```
Para **modificar** el usuario con el que se izo login, se tiene que copiar el **token** haciendo **PUT** en `http://localhost:3000/api/user` y en la pestaña **Authorization** en la opción **Bare Token** se copia el token y en el cuerpo
```json
{
    "id": "iI8CRcyCPnJmXToTjEjS4", // ID QUE SE TRAE DE LA BD
    "name": "nombre_usuario_3-MODICAR", // MODIFICAR UN DATO
    "username": "user-name-usuario_3",
    "password": "123456"
}
```
Se tiene que modificar el archivo `/store/mysql.js` para poder hacer las petiones **GET**, **POST**, **PUT** apra euse pueda hacer desde la BD de MySql
```js
// ARCHIVO PARA CONECTAR LA BA CON MYSQL
const mysql = require('mysql');
// SE IMPORTA LA CONFIGURACIÓN PARA LA CONEXIÓN A LA BD
const config = require('../config');

const dbconf = {
    host: config.mysql.host,
    port: config.mysql.port,
    user: config.mysql.user,
    password: config.mysql.password,
    database: config.mysql.database,
};

let connection;
// FUNCION PARA MANEGAR LA CONEXION
function handleCon() {
    connection = mysql.createConnection(dbconf);

    connection.connect((err) => {
        if (err) {
            // AL MOMENTO DE HACER LA CONEXION SI HAY UN ERROR SE MUESTYRA CUAL ES EL ERROR
            console.error('[db err]', err);
            // SI SE DESCONECTA HACE LA PETICIÓN EN 2 SEGUNDOS
            setTimeout(handleCon, 2000);
        } else {
            // CUANDO SE CONECTA MANDA MENSAJE
            console.log('DB Connected!');
        }
    });
    // SI DURANTYE LA CONEXION HAY ERROR PROTOCOL_CONNECTION_LOST SE VUVLVA A CONECTYAR
    connection.on('error', err => {
        console.error('[db err]', err);
        if (err.code === 'PROTOCOL_CONNECTION_LOST') {
            handleCon();
        } else {
            throw err;
        }
    })
}

handleCon();

// SE REALIZA LA CONSULTA QUE TRAIGA TODO SOBRE LA TABLA
function list(table) {
    return new Promise( (resolve, reject) => {
        connection.query(`SELECT * FROM ${table}`, (err, data) => {
            if (err) return reject(err);
            resolve(data);
        })
    })
}
// FUNCION PARA TRAER UN USUARIO CON UN ID EN ESPECIFICO
function get(table, id) {
    return new Promise((resolve, reject) => {
        console.log("ID TO BE GET: ", id);
        console.log("IN TABLE TO GET: ", table);
        connection.query(`SELECT * FROM ${table} WHERE id=${id}`, (err, data) => {
            if (err) return reject(err);
            console.log("QUERY DONE: ", data);
            resolve(data);
        })
    })
}
// FUNCION PARA INSERTAR UN USUARIO
function insert(table, data) {
    return new Promise((resolve, reject)=>{
        console.log(`GOING TO MAKE AN INSERT INTO TABLE: ${table} with data: ${data}`)
        connection.query(`INSERT INTO ${table} SET ?`, data, (err, result) => {
            if(err) {
                console.error("### ERR ###: ",err)
                return reject(err)
            } else {
                resolve(result)
            }
        })
    })
}
// FUNCION PARA ACTUALIZAR UN USUARIO
function update(table, data) {
    return new Promise((resolve, reject)=>{
        console.log("DATA TO BE UPDATED: ",data);
        connection.query(`UPDATE ${table} SET ? WHERE id= ?`,[data, data.id],(err,result)=>{
            if(err) {
                console.error("UPDATE CANNOT BE DONE: ",err)
                return reject(err)
            } else {
                console.log("UPDATE DONE: ", result)
                resolve(result)
            }
        })
    })
}

// FUNCION PARA ACTUALIZAR MODIFICAR
// LA FUNCION  upsert VA VA A HACER LA DIFERENCIA QUE ENTRE UN INSERT Y UN UPDATE
// SI LA DATA TIENE IN data.id SERA UN UPDATE POR QUE ASI VIENEN DE
// ROUTER /api/components/user/network.js
const upsert = async (table, payload) =>
  new Promise((resolve, reject) => {
    console.log("DATA TO BE UPSERT: ", payload);
    connection.query(`INSERT INTO ${table} SET ? ON DUPLICATE KEY UPDATE ?`, [payload, payload], (error, data) => {
        console.log("UPSERT DATA: ", data);
        console.log("UPDATE TABLE: ", table);
        if (error) {
            return reject(error);
        }
        resolve(data);
    });
  });

// FUNCION ASINCRONA PARA SABER SI ESTA REGISTRADO EL USUARIO
// SE GUARDA LA LISTA PARA FILTRAR
function query(table, query) {
    return new Promise((resolve, reject) => {
        console.log("DATA TO BE QUERY: ", query);
        console.log("IN TABLE: ", table);
        connection.query(`SELECT * FROM ${table} WHERE ?`, query, (err, res) => {
            console.log('QUERY RESULT: ', res)
            if (err) return reject(err);
            resolve(res[0] || null);
        })
    })
}

module.exports = {
    list,
    get,
    upsert,
    query

};
```

### 16. Relacionando entidades: follow

Para hacer la relacion de los usuario de _muchos a muchos_ se tiene que crear una tabla intermedia en la BD user_folow con dos campos y cada uno de los dos campos se convierten en indices

```sql
CREATE TABLE `user_follow` (
  `user_from` varchar(32) DEFAULT NULL,
  `user_to` varchar(32) DEFAULT NULL,
  UNIQUE KEY `idx_user_folow_user_to` (`user_to`),
  UNIQUE KEY `idx_user_folow_user_from` (`user_from`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

En el archivo `api/components/user/network.js` se tiene que habilitar la funcion de **folow** en la "ruta" 

1. Listar los usuario
2. Seleccionar a dos usuarios(el que sigue, el seguido su _id_)
3. Hacer login con "el que sigue" y guardar el _token_ 
4. En la dirección `http://localhost:3000/api/user/follow/:id` con el  bear _token_ copiado para autorización se pega en la direccion el `id` de "el seguido"


**NOTA:** Commit en mi repo _Mod. apuntes NodeJS Paractico 16: Relacionando entidades: Follow_
**NOTA:** Commit en repo del curso [Clase 16: Relacionando entidades: Follow](https://github.com/macknilan/proyecto-backend-node-platzi/commit/548c2f6ff38ee2dfef2a5d3a964079becb834c68)

### 17. Posts y likes


## 5. Microservicios en Node
### 18. Microservicios: pros y contras
### 19. Separando la base de datos a un microservicio
### 20. Conectando con nuestro microservicio de datos
### 21. Separando los posts a un microservicio
### 22. Gestión de microservicios con PM2


## 6. Puesta en producción serverless
### 23. Microservicios en Zeit Now, serverless y seguridad
### 24. Variables de entorno en Now y despliegue local


## 7. Cacheando nuestra aplicación
### 25. Caché como un microservicio. Redis
### 26. Conectando el microservicio a Redis
### 27. Conectar la API al caché


## 8. Puesta en producción en virtual machine
### 28. Desplegando los servicios de Node
### 29. Nginx como proxy inverso



































































































