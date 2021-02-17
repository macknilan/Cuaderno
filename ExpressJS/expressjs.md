
# Curso de Express.js

- :link: :octocat: [platzi-express](https://github.com/glrodasz/platzi-express)
- :link: [ES6 Destructuring: The Complete Guide](https://codeburst.io/es6-destructuring-the-complete-guide-7f842d08b98f)

## 1. Bienvenida e introducción
### 1. Introducción y bienvenida
### 2. ¿Qué es express y para qué sirve?

**Express.js** es un framework para crear aplicaciones web, apis y web services que ha sido inspirado en la librería Sinatra de Ruby. Es software libre y de código abierto con licencia MIT.

- Algunas de las características de Express.js:
    + Es minimalista, lo que lo hace muy liviano ya que muchas de sus funcionalidades deben ser instaladas posteriormente a través de plugins y módulos adicionales.
    + Incluye un sistema de template engines muy poderoso, con Handlebars, Pug, Mustach, etc. disponibles por defecto.
    + Maneja Routing, con wildcards, parámetros, etc.
    + Implementa middlewares, lo que es una de sus características más notables e importantes.
    + Permite la instalación de plugins a travpes de middlewares.

:link: [Generate a New Set of Random Passwords and Keys](https://randomkeygen.com/)

### 3. Creando tu primer servidor

- :link: [expressJS](http://expressjs.com/)
- :link: [Express Hello word example](http://expressjs.com/en/starter/hello-world.html)

Para crear un servidor Express básico es necesario crear una carpeta para el proyecto, inicializar npm en este directorio e instalar Express.js como la primera dependencia de nuestro proyecto: `npm i -S express`. Seguidamente creamos el `index.js` con el código básico para requerir y ejecutar el servidor y la ruta base de nuestra aplicación.

Con el método `.listen` inicializamos nuestro server en el puerto que elijamos. Este método devuelve el servidor como un objeto, que luego podemos utilizar para hacer un log con información que se mostrará por consola.

En el archivo `package.json` definimos el script con el que arrancaremos nuestro server, el cual ejecutará la instrucción `node index`, adicionalmente podemos definir un script para desarrollo en el que ejecutemos el `index` con `nodemon` que es una dependencia que ejecutará el servidor y actualizará su ejecución de manera automática cada vez que se hagan cambios en los archivos.

Archivos en :open_file_folder: `ExpressJS/platzi-express-que-es-un-template-engine/hello-world`

Finalmente con `npm run dev` iniciamos el servidor y estamos listos para ver los resultados en el navegador, ya sea como html o como JSON.


### 4. Express application generator

- :link: [expressJS generator](https://expressjs.com/en/starter/generator.html)
- :link: [npm express-generator](https://www.npmjs.com/package/express-generator)

En esta clase veremos cómo usar el generador de aplicaciones oficial de Express, llamado express-generator, _que permite generar toda una estructura base o scafold predeterminada para iniciar un proyecto nuevo_.

Se puede instalar para versinoes posteriores de node 8.2.0 "_PREFERENTEMENTE_" y dentro de una carpeta _vacia_ con el nombre del proyecto
```bash
$ npx express-generator
```
Primero debemos instalarlo como una dependencia global con la instrucción para versiones anteriores de node:
```bash
npm i express-generator -g
```
Para generar una aplicación con el nombre de la aplicación(para versinoes posteriores de node 8.2.0), ejecutamos la instrucción para instalar el sistema de templates "PUG"  _PREFERENTEMENTE_:
```bash
$ npx express-generator --view=pug <NOMBRE-DE-LA-APLICACION>
# OUTPUT
# SEGUIR LAS INSTRUCCIONES
change directory:
     $ cd <NOMBRE-DE-LA-APLICACION>

   install dependencies:
     $ npm install

   run the app:
     $ DEBUG=<NOMBRE-DE-LA-APLICACION>:* npm start
```
Para versiones anteriores a node 8.2.0
```
express --view=pug <NOMBRE-DE-LA-APLICACION>
```
Finalmente seguimos las instrucciones que nos indica:
```bash
#Cambiar de directorio:
cd <NOMBRE-DE-LA-APLICACION>

#Instalar las dependencias:
npm install

#Ejecutar la app:
DEBUG=<NOMBRE-DE-LA-APLICACION>:* npm start
```

Con esta funcionalidad creamos una estructura inicial, predeterminada para un nuevo proyecto con Express.js, con algunas rutas y middlewares iniciales con los que podemos empezar a trabajar, ahorrándonos algunos pasos de configuración.


## 2. Template Engines y archivos estáticos
### 5. Qué es y cómo crear tu propio template engine

Un _template engine_ es una implementación de software que nos permite mezclar datos con una plantilla o template con el fin de generar un documento que será renderizado en el navegador. Algunos de los template engines más conocidos son: Handlebars (para JavaScript), Twig y Blade (para Laravel / PHP), JSP (para Java) o Ninja (de python).

Express nos permite crear nuestro propio template engine personalizado. Además permite el uso de múltiples engines según la extensión de los archivos que le hayamos indicado.
```js
app.engine('<extension>', function( filePath, options, callback ) {});

app.set('views', '<directorio-de-vistas>');
app.set('view engine', '<extension>');
```
Donde `filePath` indica la ruta del template, options indica las variables que vamos a mezclar con el template y _callback_ será la función que mezcle la plantilla con las opciones para obtener el documento que será mostrado en el navegador.

Algo importante que debemos notar es que en Node, los callbacks son **“error first”**, por lo que el primer parámetro devuelto por las funciones por lo general serán siempre el objeto que contenga los detalles del error, si es que los hay.

Además en el objeto `options` recibido en el _callback del engine_, no solo se pasan las variables que definimos en la llamada, sino otros datos como `settings` y `locals` que deberemos descartar cuando estamos creando nuestro propio engine, pero que, cuando trabajamos con los template engines predefinidos, ya es Node quien se encarga de manejarlos.
Templates engine   
![Templates engine](imgs/exrepessjs_01.png)

Forma de trabajo   
![Forma de trabajo](imgs/exrepessjs_02.png)

La logica para el el manego de los templates propios es en el archivo `/platzi-express-que-es-un-template-engine/template-engine/express-jsx.js`

### 6. Implementando un template engine

La logica para el el manego de los templates propios es en el archivo `/platzi-express-que-es-un-template-engine/template-engine/express-jsx.js`


```js
const fs = require("fs");

function getKeysFromOptions(options) {
  const { settings, _locals, ...objectKeys } = options;
  return Object.keys(objectKeys);
}

function getRenderedContent(content, options) {
  const keys = getKeysFromOptions(options);
  let contentString = content.toString();

  for (let key of keys) {
    contentString = contentString.replace(
      new RegExp(`\{${key}\}`, "gi"),
      options[key]
    );
  }

  return contentString;
}

function expressJxs(filePath, options, callback) {
  fs.readFile(filePath, function(err, content) {
    if (err) {
      return callback(err);
    }

    const rendered = getRenderedContent(content, options);

    return callback(null, rendered);
  });
}

module.exports = expressJxs;
```

### 7. Usando Pug como template engine
- :link: [Pug](https://pugjs.org/api/getting-started.html)
- :link: [Pug cheatsheet](https://devhints.io/pug)
- :link: [Pug2Html](https://pughtml.com/)
- :link: [HTML to JADE/PUGrealtime online ](https://html2jade.org/)

:link: :octocat: [Mi repo en rama usando-pug-como-template](https://github.com/macknilan/platzi-express/tree/usando-pug-como-template/ecommerce)


### 8. Usando Handlebars como template engine

- :link: [npm Consolidate.js](https://www.npmjs.com/package/consolidate)
- :link: [handlebarsjs](https://handlebarsjs.com/)
- :link: [nopm express-handlebars](https://www.npmjs.com/package/express-handlebars)

Para poder hacer uso de Handlebars en nuestro proyecto de _Express.js_ lo único que debemos hacer es instalar como dependencia la librería [consolidate](https://www.npmjs.com/package/consolidate) y registrarla como engine.

Instalar consolidate
```bash
npm i consolidate
```

Como se muestra con el ejemplp de _Express.js_ en `platzi-express-que-es-un-template-engine/ecommerce_handlebars/index.js`

```js
const express = require("express");

const app = express();

app.get("/", function(req, res) {
  res.render("index", { hello: "hola", world: "mundo" });
});

const server = app.listen(3000, function() {
  console.log(`Listening http://localhost:${server.address().port}`);
});
```
Justo antes de las definiciones de rutas agregamos:
```js
const engines = require('consolidate');

app.engine('hbs', engines.handlebars)

app.set('views', './views')
app.set('view engine', 'hbs')
```
De esta manera podemos crear un nuevo template llamado `index.hbs` en la carpeta `views`.
```hbs
extends layout

block content
  h1= title
  p Welcome to #{title}
```
Y eso es todo, ya podemos usar nuestros templates hecho con _Handlebars_.

### 9. Creando nuestro layoutde productos usando Pug

Para implementar templates con PUG, sólo bastará con instalar PUG con la instrucción `npm i -D pug` y definir el uso del _view engine_ respectivo usando los _middlewares_ de manera similar a como vimos antes con Handlebars.

- PUG incluye instrucciones que facilitan el trabajo con las vistas:
    + **extends**: define un template base del que extiende el template actual.
    + **include**: define la inclusión o importación de otro template.
    + **block**: define un placeholder para el contenido de bloques en los que se insertarán partes de un template.

Para más información sobre el uso de PUG, Bulma y FontAwesome, recuerden consultar los enlaces adicionales de esta clase.

Los archivos se encuentran en el folder :open_file_folder: `platzi-express-creando-nuestro-layout-de-productos-usando-pug/ecommerce/views`


### 10. Manejo de archivos estáticos

:link: :octocat: [Rama "Manejo de archivos estáticos" en mi repo](https://github.com/macknilan/platzi-express/blob/manejo-de-archivos-estaticos/ecommerce/index.js)

```js
const express = require("express");
const path = require("path");
const app = express();
const productsRouter = require('./routes/products');

// SE LE DICE A EXPRESS QUE COMO VA A MANEJAR LOS ARCHIVOS ESTATICOS CON EL PREFIJO /static Y LA DIRECCIÓN DE DONDE ESTA LA CARPETA
// SE CREA LA CARPETA public DENTRO CON LAS CARPETAS assets, images, logo
// SE MODIFICAN LOS ARCHIVOS .pug DENTRO DE LAS CARPETA view PARA QUE IMPORTEN LOS ARCHIVOS STATIC
app.use("/static", express.static(path.join(__dirname, "public")));

app.set("views", path.join(__dirname, "views"));
app.set("view engine", "pug");

app.use("/products", productsRouter);

const server = app.listen(8000, function() {
  console.log(`Listening http://localhost:${server.address().port}`);
});
```

## 3. Creando un API Restful
### 10. Anatomía de una API RESTful e implementación CRUD

:link: :octocat: [Anatomía de una API RESTful e implementación CRUD en mi repo](https://github.com/macknilan/platzi-express/blob/anatomia-de-una-api-restful/ecommerce/index.js)

Se modifica el archivo index para implementar la logica para añadir a express la ruta para hacer CRUD

Se crea dentro de la carpeta `routes\api\products.js`

Acciones en las diferentes tipos de peticiones del CRUD en los endpoints   
![Acciones en las diferentes tipos de peticiones del CRUD en los endpoints](imgs/exrepessjs_03.png)

Forma de las las peticiones al API para ahcer CRUD   
![Forma de las las peticiones al API para ahcer CRUD](imgs/exrepessjs_04.png)

Para consumir los datos quemados se crean en la ruta `utils\mokcs\products.js`

Con Postman en la ruta se hace una peticion GET en la ruta `http://localhost:8000/api/products` y devuelve los datos mok y con los mensajes y codigos 200 de OK
```json
const productMocks = [
    {
      name: "Red shoes",
      price: 75,
      image: "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=0e44599932dce6b8440e26fb91e10a69&auto=format&fit=crop&w=800&q=60"
    },
    {
      name: "Black bike",
      price: 300,
      image: "https://images.unsplash.com/photo-1532298229144-0ec0c57515c7?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=53d820e6622fadd53b8638d60f468ccd&auto=format&fit=crop&w=800&q=60"
    }
  ];

  module.exports = productMocks;
```

### 11. Implementando nuestra capa de Servicios.

Se crea el archivo en la ruta `ecommerce/services/products.js` que tiene una clase con la logica de los metodos (GET, POST, PUT, PATCH, DELETE) la cual se encarga de los servicios del negocio, tiene la responsabilidad de llamar a los datos


Se tienen que instalar la libreria :link: [body-parser](https://www.npmjs.com/package/body-parser) para parsear las peticiones en formato JSON **request** y **response** en la capa de servicios que actue como _middleware_ y se importa en el archivo principal `indexjs` 

```bash
npm i body-parser
```

:link: :octocat: [Anatomía de una API RESTful e implementación CRUD EN MI REPO](https://github.com/macknilan/platzi-express/blob/implementando-nuestra-capa-de-servicios/ecommerce/index.js)


Capa de servicios modelo vista-controlador MVC   
![Capa de servicios modelo vista-controlador MVC](imgs/exrepessjs_05.png)

En el archivo `routes\api\products.js` (CONTROLADOR) es donde esta lal logica del del negocio, se implementan los metodos de para los **request** y **response** y se manejan los errores en las peticiones las cuales estan relacionadas con el archivo `routes\products.js` (VISTA) que recibe y envia parametros al controlador

### 12. Recapitulando el proyecto

:link: [Destructuring and Function Arguments](https://davidwalsh.name/destructuring-function-arguments)

:link: :octocat: [Recapitulando el proyecto EN MI REPO](https://github.com/macknilan/platzi-express/blob/recapitulando-el-proyecto/ecommerce/index.js)

Se hacen comentarios al proyecto para saber que es lo que realiza en algunas lineas.

Correción de paquete **dody-parser** se corrige como se importa y se instala el adecuado `const bodyParser = require('body-parser');`

Para entender mejor la logica de la estructura, se crea la carpeta `views` por que ahi es donde esta las vistas, y se mueve de lugar el archivo `products.js` dentro `ecommerce/routes/views/products.js`. 

En en archivo `/ecommerce/routes/api/products.js` se insertan `console.log` despues de cada peticion para poder saber que es lo que contiene las peticines **request** y **response** `(req, res)` 

### 13. Request object

:link: [POST](https://developer.mozilla.org/es/docs/Web/HTTP/Methods/POST)

Request Object

El objeto `req` _(Request)_ en Express representa el llamado HTTP y _tiene diferentes propiedades_ del llamado, como la _cadena de texto query_ **(Query params)**, los _parámetros de la URL_ **(URL params)**, el _cuerpo_ **(Body)**, los _encabezados_ **(HTTP headers)**, etc.

Para acceder al `req` basta con acceder al primer parámetro de nuestros router handlers (_router middleware_) ó _middlewares_.

Como por ejemplo así lo hemos visto siempre:
```js
app.get('/user/:id', function(req, res) {
  res.send('user ' + req.params.id);
});
```
Pero también funcionaría sin problemas:
```js
app.get('/user/:id', function(request, response) {
  response.send('user ' + request.params.id);
});
```
Exploremos las propiedades más importantes

:traffic_light: `req.body`

Contiene los pares de _llave-valor_ de los datos enviados el cuerpo **body** del llamado **request**. Por defecto es `undefined` pero es establecido cuando se usa algún “body-parser” middleware como body-parser y multer.

En Postman cuando hacemos un request y enviamos datos en la pestaña _Body_, estos _middlewares_ son los que nos ayudan a entender el tipo de datos que vamos a recibir en el `req.body`.

Aquí podemos ver como se pueden usar estos middlwares para establecer el valor del `req.body`:
```js
const app = require('express')();
const bodyParser = require('body-parser');
const multer = require('multer');
const upload = multer(); // Para datos tipo multipart/form-data

app.use(bodyParser.json()); // Para datos tipo application/json
app.use(bodyParser.urlencoded({ extended: true })); // Para datos tipo application/x-www-form-urlencoded

app.post('/profile', upload.array(), function (req, res, next) {
  console.log(req.body);
  res.json(req.body);
});
```
:traffic_light: `req.params`

Esta propiedad contiene un objeto con las propiedades equivalentes los parámetros nombrados en la ruta. Por ejemplo si tenemos una ruta de la forma `/user/:name` entonces la propiedad `name` esta disponible como `req.params.name` y alli podremos ver su valor, supongamos que llamáramos la ruta con `/user/glrodasz`, entonces el valor de `req.params.name` seria `glrodasz`. Este objeto por defecto tiene el valor de un objeto vacío `{}`.

```js
// GET /user/glrodasz
req.params.name
// => "glrodasz"
```
:traffic_light: `req.query`

Esta propiedad contiene un objeto con las propiedades equivalentes a las cadenas de texto `query` de la ruta. Si no hay ninguna cadena de texto `query` tendrá como valor por defecto un objeto vacío `{}`.
```js
req.query.q
// => "tobi ferret"

// GET /shoes?order=desc&shoe[color]=blue&shoe[type]=converse
req.query.order
// => "desc"

req.query.shoe.color
// => "blue"

req.query.shoe.type
// => "converse"
```
:link: [3.4 Query](https://tools.ietf.org/html/rfc3986#section-3.4)


## 4. Conectando Express.js con servicios externos
### 14. Conexión a Mongodb en Express.js

MongoDB Atlas es un servicio de bases de datos como servicio que nos permite configurar nuestras bases de datos para entornos de pruebas o producción con diferentes proveedores de nube. Además de todas sus características, Atlas se destaca por ser un servicio mantenido oficialmente por el equipo que desarrolla MongoDB.

mLab también era un servicio de bases de datos con Mongo. Pero fue adquirido por MongoDB a inicios del 2019 para darle más fuerza a MongoDB Atlas y unir fuerzas con el anterior equipo de mLab.

:link: [mongoDB](https://www.mongodb.com/)

Usa _MongoDB_ Atlas en lugar de _mLab_

Para crear tu cuenta y base de datos con MongoDB Atlas solo debes seguir esta clase:

:link: [Creación de una BD en MongoAtlas](https://platzi.com/clases/1646-backend-nodejs/22033-creacion-de-una-bd-en-mongoatlas/)

Recuerda que los nombres de tus bases de datos y clusters deben ser los mismos en el servicio de Atlas y en tu código.

### 15. Conectando nuestros servicios con mongo DB

:link: :octocat: [Conectando nuestros servicios con mongo DB EN MI REPO](https://github.com/macknilan/platzi-express/blob/conectando-nuestros-servicios-con-mongodb/ecommerce/index.js)


Se tienen que instalar la libreria _dotenv_ para que lear los archivos que comiencen por punto (.)
:link: [dotenv nom](https://www.npmjs.com/package/dotenv)
```bash
$ npm i dotenv
```

Para conectar la app con la BD de mongo se tienen que instalar :link: [mongodv](https://www.npmjs.com/package/mongodb)
```bash
$ npm i mongodb
```

### 16. Implementando acciones CRUD en MongoDB
- :link: [MongoDB CRUD Operations](https://docs.mongodb.com/manual/crud/)
- :link: [Collection Methods](https://docs.mongodb.com/manual/reference/method/js-collection/)
- :link: :octocat: [ karlseguin / the-little-mongodb-book ](https://github.com/karlseguin/the-little-mongodb-book)

- :link: :octocat: [Implementando acciones CRUD en MongoDB](https://github.com/macknilan/platzi-express/blob/conectando-nuestros-servicios-con-mongodb/ecommerce/index.js)

Se crea el archivo para que el/los devs sepan como es el archivo de muestra `ecommerce/.env.example` como crear el archivo `.env`
```
// CONFIG
PORT=8000

// **MONGODB ATLAS**
DB_USER= USUARIO DE LA BD
DB_PASSWORD= PASSWORD DE LA BD
DB_HOST= ES EL NOMBRE DEL Clusters DESPUES DE LA @ HASTA LA / QUE ESTA ANTES DEL NOMBRE DE LA BD
DB_PORT= ES EL PUERTO QUE USA MONGODB ATLAS QUE PUEDE SER 27017, 27018, 27019
DB_NAME= NOMBRE DE LA BD

// CONFIGURACIÓN PARA CONEXION CON MONGODB ATLAS CON LA LIGA Conect your application
const MONGO_URI = `mongodb+srv://${USER}:${PASSWORD}@${config.dbHost}/${DB_NAME}?retryWrites=true&w=majority`; // prettier-ignore
```

Se crea el archivo `.env` en la raiz del proyecto con con el contenido de `ecommerce/.env.example`

En el archivo `.gitignore` se establece que el archivo `.env` git no lo tone en cuenta, agregando `.env`

Se crea el archivo de configuracion `config/index.js` para traer las variables de entorno a la app

El archivo `lib/mongo.js` tiene la logica para la conexión a la BD en mongoDB


Para revisar que se conecte a la BD `npm run dev` y con _Postman_ en la direccion `http://localhost:8000/api/products` hacer la peticion GET para traer los con ayuda de la clase en el archiv `lib/mongo.js` y su metodo `getAll` para hacer query en la DB

Y como respuesta
```json
{
    "data": [],
    "message": "products listed"
}
```
por que por el momento no cuanta con ningun dato.

Metodos HTTP   
![Metodos HTTP](imgs/exrepessjs_06.png)


Se modifico el archivo `/services/products.js` la clase ProductsService para que sus metodos llamaran asincronamente a los metodos de la clase MongoLib en `/ecommerce/lib/mongo.js` para poder hacer los querys en el forma de mongoDB y se conecte cada vez para poder realizarlo.

Para poder realizar las petiones HTTP por la API con _Postman_ para efectos de este ejemplo se toma en cuenta este documento/fila(BSON)

Revisar para hacer pruebas `npm run dev`

Se hace POST en `http://localhost:8000/api/products` con el _body_
 ```json
 {
	"name": "Butaco blanco",
	"price": "1",
	"image": "https://images.unsplash.com/photo-1503602642458-232111445657?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=bf884ad570b50659c5fa2dc2cfb20ecf&auto=format&fit=crop&w=800&q=60",
	"tags": ["white", "expensive"]
}
```
Manda como respuesta exitosa y debe de estar registrado en mondoDB Atlas.   
El valor de `"data"` es el valor del `_id` que le asigna mongoDB de forma automatica
```json
{
    "data": "5eea63bf96673e442488a92d",
    "message": "product created"
}
```
Se hace GET en `http://localhost:8000/api/products` para comprobar los datos guardados

Se hace GET en `http://localhost:8000/api/products/5eea63bf96673e442488a92d` traer el producto especifico por `id`

Se hace GET en `http://localhost:8000/api/products/?tags[]=white` para buscar en el arreglo de tags que se encuentra en cada producto y se pude realizar la busqueda por varios tags `http://localhost:8000/api/products/?tags[]=white&tags[]expensive`



Para actualizar PUT el producto se hace por `id` en la direccion `http://localhost:8000/api/products/5eea63bf96673e442488a92d` con el _body_ json a actualizar.
```json
{
	"name": "Black Bike",
	"price": "300",
	"image": "https://images.unsplash.com/photo-1503602642458-232111445657?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=bf884ad570b50659c5fa2dc2cfb20ecf&auto=format&fit=crop&w=800&q=60",
	"tags": ["expensive", "black"]
}
```
Y en caso que sea exitosa la actualización regresa
```json
{
    "data": "5eea63bf96673e442488a92d",
    "message": "product updated"
}
```
Para eliminar DELETE el producto se hace por `id` en la direccion `http://localhost:8000/api/products/5eea63bf96673e442488a92d` y regresa el mensaje que se elimino correctamente.
```json
{
    "data": "5eea63bf96673e442488a92d",
    "message": "product deleted"
}
```
### 17. Configurar una cuenta en Amazon AWS


## 5. Middlewares: En el medio del request
### 18. Qué es un middleware y qué tipos existen

:link: [Express middleware](https://expressjs.com/en/resources/middleware.html)

El middleware es una funcion con 3 argumentos, como una serie de capas que por lo regular es para validaciones   
![El middleware es una funcion con 3 argumentos, como una serie de capas que por lo regular es para validaciones](imgs/exrepessjs_07.png)

- Tipod de middleware
    1. 3rd party
    2. Router level
    3. Application level
    4. Built-in
    5. Error-handling

### 19. Manejo de errores usando un middleware
:link: [Error Handling](http://expressjs.com/en/guide/error-handling.html)

Error Handling   
![Error Handling](imgs/exrepessjs_08.png)

:link: :octocat: [19. Manejo de errores usando un middleware EN MI REPO](https://github.com/macknilan/platzi-express/blob/manejo-de-errores-usando-un-middleware/ecommerce/services/products.js)

Se crea una carpeta "middlewares" con el archivo "errorsHandlers.js" -> `ecommerce/utils/middlewares/errorsHandlers.js` 

Despues de tiene que instalar en la app en el archivo `index.js` y deben de ir al final de todas las rutas.
```js
const {
    logErrors,
    clientErrorHandler,
    errorHandler
  } = require("./utils/middlewares/errorsHandlers");
/* ... */

// error handlers
app.use(logErrors);
app.use(clientErrorHandler);
app.use(errorHandler);
```

Se tiene que crear despues una vista para los errores creando `ecommerce/views/error.pug` para mostrar los errores en vista.

Para comprovar su funcionameitno se puede hacer provocando un error en `/ecommerce/routes/views/products.js` dentro del `try`
```js
throw new Error('This is a new error');
```
Se muestra el stack error   
![Se muestra el stack error](imgs/exrepessjs_09.png)

Y tambien se muestra en consola el stack.

### 20. Validación de datos usando un middleware
Evitar datos que manden datos que no corresponden a esquemas que no corresponden.

Funcion para validar datos   
![Funcion para validar datos](imgs/exrepessjs_10.png)

La funcio que devuelve la funcion es el middleware. 

Para lograrlo se crea `ecommerce/utils/middlewares/validationHandler.js` la cual la libreria Joi se encargara de realizar la validación.

### 21. Implementando Sentry para el manejo de log de errores

Hcer una cuenta en :link: [Sentry](https://sentry.io/signup/) 

Al ingresar al dashboard de Sentry lo que podemos hacer es ir directamente onboarding haciendo click en la alerta amarilla que aparece en la parte superior o mediante el link [https://sentry.io/onboarding/<organización>/](https://sentry.io/onboarding/<organización>/)

![onboarding](imgs/expressjs_11.jpg)

Allí nos pedirá que seleccionemos un lenguage y un team, para el lenguaje seleccionaremos `Server > Node.js` le daremos un nombre al proyecto dejaremos el _team_ que tiene por defecto y a continuación haremos click en `Create Project`.

![Create Project](imgs/expressjs_12.jpg)

Después de ello nos entregara unas instrucciones para configurar Sentry. Lo que haremos es instalar la dependencia de Sentry e inicializar su configuración en el archivo `/utils/middlewares/errorsHandlers.js`

> Recordemos que no debemos dejar ninguna key, secret o identificador quemado en nuestro código por lo que la recomendación es moverlo a variables de entorno y configuración usando el archivo `.env`

```
// .env.example y .env

SENTRY_DNS=
SENTRY_ID=
```

```js
// config/index.js

require("dotenv").config();

const config = {
  sentryDns: process.env.SENTRY_DNS,
  sentryId: process.env.SENTRY_ID
};

module.exports = { config: config };
```

```js
// utils/middlewares/errorsHandlers.js

const Sentry = require("@sentry/node");
const { config } = require("../../config");

Sentry.init({ dsn: `https://${config.sentryDns}@sentry.io/${config.sentryId}` });
```
Y dentro de nuestro middleware logErrors agregamos el capturador de errores de Sentry:
```js
// utils/middlewares/errorsHandlers.js

function logErrors(err, req, res, next) {
  Sentry.captureException(err);
  console.error(err.stack);
  next(err);
}
```
Le damos click en _All done!_ y nos reenviara al dashboard dónde podremos monitorear los errores que ocurren en nuestra aplicación.

De esta manera cualquier error que ocurra en nuestra aplicación desplegada en producción estará registrado en Sentry y podremos revisarlos y corregirlos proactivamente.

> Si quieres obtener más información sobre cómo capturar eventos y mensajes manualmente puedes consultarlo aquí [https://docs.sentry.io/error-reporting/capturing/?platform=node](https://docs.sentry.io/error-reporting/capturing/?platform=node)

`/ecommerce/.env`
```
// CONFIG
PORT=8000

// **MONGODB ATLAS**
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_NAME=
SENTRY_DNS=
SENTRY_ID=
```

`/ecommerce/config/index.js`
```js
// ARCHIVO DE CONFIGURACION PARA TRAER LAS VARIABLES DE ENTORNO A LA APP
require("dotenv").config();

const config = {
  // VARIABLE QUE INDICA SI ESTA EN PRODUCCION O DESARROLLO
  dev: process.env.NODE_ENV !== "production",
  port: process.env.PORT,
  dbUser: process.env.DB_USER,
  dbPassword: process.env.DB_PASSWORD,
  dbHost: process.env.DB_HOST,
  dbPort: process.env.DB_PORT,
  dbName: process.env.DB_NAME,
  sentryDns: process.env.SENTRY_DNS,
  sentryId: process.env.SENTRY_ID
};

module.exports = { config };
```

`ecommerce/utils/middlewares/errorsHandlers.js`
```js
// import * as Sentry from '@sentry/node';
// or using CommonJS
const Sentry = require('@sentry/node');
const { config } = require("../../config");

Sentry.init({ dsn: `https://${config.sentryDns}@o408997.ingest.sentry.io/${config.sentryId}` });

// MIDDLEWARE PARA HACER LOG DE LOS ERRORES
function logErrors(err, req, res, next) {
    Sentry.captureException(err); // AGREGAMOS EL CAPTURADOR DE ERRORES DE Sentry
    console.log(err.stack);
  next(err); // SE LLAMA AL RPOXIMO MIDDLEWARE PASANDO LE EL ERROR CON EL CALLBACK next
}
```

### 22. Qué es Joi y Boom y cómo configurar Joi

* Joi: Object Schema Valitation
* Boom: HTTP-friendly error objects; enviar errores de forma mas agradable.

- :link: [Unacceptable Browser HTTP Accept Headers (Yes, You Safari and Internet Explorer)](https://www.newmediacampaigns.com/blog/browser-rest-http-accept-headers)
- :link: [@hapi/joi](https://www.npmjs.com/package/@hapi/joi)
    + :link: [Documentation joi](https://hapi.dev/module/joi/)
- :link: :octocat: [hapijs/joi](https://github.com/hapijs/joi)

```bash
$ npm install @hapi/joi
```

Se crea `ecommerce/utils/schemas/products.js` el cual tiene la logica para poder establecer los tipos de datos que se requieren y cuales son requeridos con la ayuda de la libreria [@hapi/joi](https://www.npmjs.com/package/@hapi/joi)

Despues en `utils/middlewares/validationHandler.js` se importa la libreria `@hapi/joi` para poder exportarla y que funcione como un middleware para validar los tipos de datos por medio de la funcion `validationHandler` la cual manda a llamar a otra funcion por medio de **scope** para ocupar la libreria _joi_ y validar el `schema` y la `data` que el json que se pretende validar para insertar datos.

En el archivo `/routes/api/products.js` se importa el `schema` y el _middleware_ para poder validar al momento de insertar y actualizar en la peticion POST y PUT con la logica de validación de _@hapi/joi_
```js
// ACTUA COMO MIDDLEWARE ANTES DE QUE SE EJECUTE LA PETICION POST
router.post("/", validation(createProductSchema), async function(req, res, next)
```

### 23. Configurando Boom y nuestra página 404

- :link: [Documentation boom](https://hapi.dev/module/boom/)
- :link: :octocat: [hapijs/boom](https://hapi.dev/module/boom/)

Se instala Boon como dependencia
```bash
$ npm install @hapi/boom
```
Y se importa en `/utils/middlewares/errorsHandlers.js` la lógica de los middlewares es que el error pasa por las capas de manejador de errores 

1. withErrorStack :arrow_down:
2. logErrors :arrow_down:
3. wrapErrors :arrow_down:
4. clientErrorHandler :arrow_down:
5. errorHandler :arrow_down:

Despues en `/utils/middlewares/validationHandler.js`se implenta _Boom_ para retornar error 400 de pagina no encontrada

Se crea el archivo `ecommerce/utils/isRequestAjaxOrApi.js` para realizar dos validaciones, si el `request` es de una llamada para vista "html" es una llamada por AJAX(API)

Al final se tiene que mandar a llmar y usar el middleware `wrapErrors` en `/ecommerce/index.js` 

Justo despues de todas las rutas y antes de los middlewares de validación se especifica que se si no encuentra la para html o API se muestre la pagina con el error 404 con ayuda de _Boom_
```js
// MIDDLEWARE PARAMOSTRAR LA PAGINA 404 AL FINAL DE TODAS LAS RUTAS
// SI NO CAE EN NINGUNA RUTA ENTONCES SE MUESTRA LA PAGINA 404
app.use(function (req, res, next) {
  if (isRequestAjaxOrApi(req)) {
    const {
      output: { statusCode, payload },
    } = boom.notFound();

    res.status(statusCode).json(payload);
  }

  res.status(404).render("404");
});
```
Al hacer peticion a una "vista" que no existe se muestra la paguina 404 y cuando se hace una peticion AJAX a API a una dirección que no existe con `X-Requested-With=XMLHttpRequest` en _Postman_ responde 
```json
{
    "statusCode": 404,
    "error": "Not Found",
    "message": "Not Found"
}
```

### 24. Middlewares populares

- Middlewares populares de express:
    + `express.json` o `body-parser.json`: Sirve para que nuestras requests entiendan json
    + `cors`: Middleware de seguridad que sirve para que los requests sean aceptados de ciertos dominios específicos
    + `morgan`: Middleware para el manejo de logs
    + `helmet`: Middleware de seguridad
    + `express-debug`: El debugger predeterminado de express para debuggear tu aplicación
    + `express-slash`: Permite aceptar urls sin el slash (’/’)
    + `passport`: Para autentifación y autorización
|

## 6. Autenticación en Express.js
### 25. JSON Web Tokens

- :link: [JWT])(https://jwt.io/)

- JWT su estructura es:
    + Header
    + Payload
    + Signature

JSON WEB TOKENS tiene la estructura   
![JSON WEB TOKENS tiene la estructura](imgs/exrepessjs_11.png)

### 26. Configuración y uso de Passport.js

- :link: [Passport](http://www.passportjs.org/)
- :link: [Passport-HTTP](http://www.passportjs.org/packages/passport-http/)
- :link: :octocat: [kelektiv /node.bcrypt.js](https://github.com/kelektiv/node.bcrypt.js#usage)

Instalar :link: [passport](https://www.npmjs.com/package/passport)
```bash
$ npm i passport
```
Instalar :link: [passport-http](https://www.npmjs.com/package/passport-http)
```bash
$ npm i passport-http
```
Instalar :link: [passport-jwt](https://www.npmjs.com/package/passport-jwt)
```bash
$ npm i passport-jwt
```
Instalar :link: [jsonwebtoken](https://www.npmjs.com/package/jsonwebtoken)
```bash
$ npm i jsonwebtoken
```
Instalar :link: [bcrypt](https://www.npmjs.com/package/bcrypt)
```bash
$ npm i bcrypt
```
Instalar :link: [chalk](https://www.npmjs.com/package/chalk)
```bash
$ npm i chalk
```
```bash
$ npm i passport passport-http passport-jwt jsonwebtoken bcrypt chalk
```

Se crean nuevas variables en `/ecommerce/.env.example`
```
// AUTH
AUTH_ADMIN_USERNAME=
AUTH_ADMIN_PASSWORD=
AUTH_ADMIN_EMAIL=
AUTH_JWT_SECRET=
```

Se crea el archivo `/ecommerce/scripts/mongo/seed-admin.js` el cual tiene como finalidad la administración del usuario admin con la bd de mongoDB ocupando la libreria _bcrypt_ para implementar hasheado de las credenciales

Ejecutar el archivo para crear el usuario admin si no esta creado.
```bash
$ node scripts/mongo/seed-admin.js
```
Coleccion user en mongo atlas
![Coleccion user en mongo atlas](imgs/exrepessjs_12.png)

En `ExpressJS/ecommerce/utils/auth/strategies/basic.js` se crea la estrategia básica para cuando un usuario _admin_ haga login sea autentificado, si esiste en la bd _se regresa el usuario_, caso cintrario se regresa el error de que le usuario no esta autentificado. 

Se crea `/ecommerce/routes/api/auth.js` para realizar un _end point_ en API para que el usuario admin haga login y se obtiene token de autentificación. 

Despues el endpoint se tiene que instalar en el `index.js` 
```js
const authApiRouter = require("./routes/api/auth");
/* ... */
app.use("/api/auth", authApiRouter);
```

Para verificar su funcionamiento con _Postman_ en el endpoint `http://localhost:8000/api/auth/token`se hace POST con el usuario y contraseña del usuario admin con el tipo de autentificación basica y como respuesta se obtiene el token de autentificación correcta

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtYWNrbmlsYW4iLCJlbWFpbCI6Im1hY2tAbWFpbC5jb20iLCJpYXQiOjE1OTI1MjkxMzgsImV4cCI6MTU5MjUzMDAzOH0.FNGk24hHHKvNNlO9iDz6gJwljTAStUbJWh-1t_o9nZ8"
}
```

### 27. Asegurando nuestra API e identificando rutas sensibles

- :link: :octocat: [node-jsonwebtoken use](https://github.com/auth0/node-jsonwebtoken#usage)
- :link: [Passport Docs](http://www.passportjs.org/docs/)
- :link: [passport-jwt](http://www.passportjs.org/packages/passport-jwt/)

En el archivo `/utils/auth/strategies/jwt.js` tiene la lógica para asegurar que las ritas sean solo usadas por un usuario autorizado, utlizando la estrategia `jsonwebtoken`

La cual se tiene que inluir en `/routes/api/products.js` para poder validar las rutas de actualización y de borrado y que solo los usuario autorizados tengan acceso a ejecutar estas peticiones HTTP

Para verificar su funcionamiento con _Postman_ en el endpoint `http://localhost:8000/api/products/5eea6d9796673e442488a92e`se hace PUT con el ID de un producto con el tipo de autentificación `Bare Token` y con el token de autorización puesto en _Postman_ y en el body el JSON a actualizar
```json
{
	"name": "Butaco blanco",
	"price": "2",
	"image": "https://images.unsplash.com/photo-1503602642458-232111445657?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=bf884ad570b50659c5fa2dc2cfb20ecf&auto=format&fit=crop&w=800&q=60",
	"tags": ["blue", "expensive"]
}
```
y como respuesta
```json
{
    "data": "5eea6d9796673e442488a92e",
    "message": "product updated"
}
```


## 7. Testing
### 28. Creando tests para nuestros endpoints
### 29. Creando tests para nuestros servicios
### 30. Creando tests para nuestras utilidades
### 31. Agregando coverage para ver la calidad de nuestras pruebas
### 32. Debugging e inspect


## 8. Deployment
### 33. Buenas prácticas para el despliegue en producción


### 34. npm script
### 35. Añadiendo manejo de cache y seguridad con helmet
### 36. Cómo usar las variables de entorno para diferente ambientes
### 37. Habilitando CORS en producción
### 38. Cómo funciona y por qué es importante el uso de HTTPS
### 39. Desplegando con Now y detectando vulnerabilidades con npm audit
### 40. Automatizar el chequeo de vulnerabilidades con snyk










































