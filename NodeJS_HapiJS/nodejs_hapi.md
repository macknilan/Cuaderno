

# Curso de Node.js con Hapi

:octocat: :link: [ hapijs/hapi ](https://github.com/hapijs/hapi/blob/master/API.md)
:octocat: :link: [ hapijs ](https://github.com/hapijs)

## 1. Introducción
### 1. Bienvenida al curso y prerrequisitos

**¿Qué es Hapi?**
Hapi es uno de los frameworks más usados en el ecosistema de NodeJS. Está diseñado pensando en plicativos modularizados de grandes dimensiones. Contempla la separación de la configuración de la lógica del egocio y utiliza su propia forma de hacer las cosas.

+ Es usado para crear: 
    + Aplicativos Web
    + APIs REST
    + APIs en GraphQL
    + Proxies HTTP e Integrador de múltiples Backends
    + entre otros...

+ Prerrequisitos
    + Conocimientos básicos de NodeJS
    + Conocimientos generales de arquitectura MVC
    + Y opcionalmente, conocimientos básicos de: Express, Asincronía en Node con async / await y Firebase


### 2. Breve historia y estado actual
### 3. Conceptos principales de hapi y creación de nuestro primer servidor
:link: [hapi The Simple, Secure Framework Developers Trust](https://hapi.dev/)

Ejemplo en la la carpeta "hapi-overflow-1"

**Hapi fue creado por Eran Hammer**, el mismo desarrollador y creador de la especificación OAuth, quien siendo líder del equipo de Mobile en Walmart, se vió en la necesidad de buscar una solución a los problemas relacionados con el tráfico del sitio web durante los días cercanos al BlackFriday.

**Junto a su equipo crea Hapi**, como un **middleware de Express**, ya que éste no les ofrecía solución a los problemas que estaban enfrentando. Luego de probar diferentes combinaciones de soluciones, decidieron crear todo el framework desde cero sobre la base del principio: _“mejor configuración que código_”, e inspirados en Express y Director. Así que crearon un concepto nuevo con el que lograron soluciones más eficientes para su problema.

Recientemente Hapi (en su versión más reciente 17.x) fue rediseñado para aprovechar toda la funcionalidad y potencialidad que ofrece el trabajo asincrónico con **Async / Wait de NodeJS**.

## 2. Creando un sitio básico con Hapi
Se crea el la carpeta `primer_servidor_hapi` y se instalan los paquetes
```bash
$ npm install @hapi/hapi
```
Y tambien se instala _standard_ :link: (npm standar)[https://www.npmjs.com/package/standard] que ayuda en escribir bien en Javascript "_JavaScript Standard Style_"
```bash
$ npm i standard
```
La propiedad method indica si el request esperado es de tipo **GET** o **POST**, y el path es la url relativa asociada a esta ruta definida. El _handler_ es la función que manejará la respuesta que se enviará al navegador.

### 4. El objeto h, response y sus herramientas
:link: [Response Toolkit](https://hapi.dev/api/?v=19.1.1)

El _objeto_ **h**, es el segundo argumento que recibe la función `handler` de una ruta definida.

Contiene una colección de utilidades y propiedades relativas a la información de respuesta que se va a enviar al cliente, al navegador.

+ :link: [Response object](https://hapi.dev/api/?v=19.1.1#response-object)

- Métodos básicos del objeto **h**:
    + `h.response()`: Crea un objeto de respuesta.
    + `h.redirect()`: Redirecciona una petición.

El objeto _Response_ (creado con el método `h.response`), permite definir las _propiedades de la respuesta_. A través de este objeto se pueden _especificar las cabeceras_, tipo de documento y código de respuesta devuelto al cliente, mediante los métodos: `.header()`, `.type()` y `.code()`


### 5. Uso de plugins - Contenido estático
:link:[Hapi Server](https://hapi.dev/api/?v=19.1.1)

_Los plugins son módulos_ o archivos de Javascript creados _generalmente por terceros_, que le **adicionan funcionalidades** al framework base de Hapi.

Para implementar un plugin nuevo a nuestro proyecto, lo primero es importarlo en el `index.js` con la función _requier()_ de NodeJS. Luego es necesario registrarlo con _await server.register(plugin)_.

Por el momento, incluiremos en nuestro proyecto los plugins de **Inert** y **Path**

+ `const inert = require('inert')`
+ `const path = require('path')`

+ El plugin `Inert` extiende los métodos disponibles en el objeto h.
+ `Path` nos permite definir una ubicación relativa para todos los routes de nuestro proyecto, entre otras cosas.

Código: usando `Inert` para servir un directorio de archivos y un `index.html` en el path `‘/’`

**NOTA**: Para matar los procesos de node `pkill node`

Se tiene que instalar el plug-in :link: [@hapi/inert](https://www.npmjs.com/package/@hapi/inert)
```bash
$ npm i @hapi/inert
```
>inert is part of the hapi ecosystem and was designed to work seamlessly with the hapi web framework and its other components (but works great on its own or with other frameworks). If you are using a different web framework and find this module useful, check out hapi – they work even better together.

Archivo `index.js`
```js
'use strict'

const Hapi = require('@hapi/hapi');
// SE IMPORTA EL PLUGING PARA SERVIR LOS ARCHIVOS ESTATICOS
// const inert = require('inert')
// SE IMPORTA path QUE PARTE DE NODE
const path = require('path')

// SE CREA EL SERVIDOR COMO OBJETO 
const server = Hapi.Server({
    // EL PUERTO SE ESTABLECE COMO PARAMETRO CON LA VARIALBLE DE ENTORNO PORT Y SI NO CON EL PUERTO 3000
    port: process.env.PORT || 3000,
    // CORRE EN EL LOCALHOST
    host: 'localhost',
    // SE DECLRAR LA VARIABLE/OBJETO PARA DECLRAR LA RUTA A LA CARPETA DE ARCHIVOS ESTATICOS
    routes: {
        files: {
            relativeTo: path.join(__dirname, 'public')
        }
    }
})

// DEFINICION DE FUNCIÓN PARA INICIALIZAR EL PROYECTO. INTENAMNETE HAY TAREAS ASINCRONAS
async function init() {
    try {
        // REGISTRAR LOS PLUGINS QUE HAPI VA A NECESITAR PARA SERVIR ARCHIVOS ESTATICOS
        await server.register(require('@hapi/inert'));

        // DEFINICIÓN DE RUTAS SE INDICA EL MÉTODO HTTP, URL Y CONTROLADOR/handler DE RUTA
        // SE DECLARAN DESPUÉS DEL PLUGIN YA QUE LAS RUTAS HACEN USO DEL MISOM PARA DEVOLVER ARCHIVOS ESTATICOS
        server.route({
            method: 'GET',
            path: '/home',
            handler: (req, h) => {
                // POR EL INERT SE TIENEN ACCESO AL METODO h.file()
                return h.file('index.html')
            }
        })
        // RUTA PARA SERVIR ARCHIVOS ESTÁTICOS ASOCIADOS (IMG/CSS/JS)
        server.route({
            method: 'GET',
            path: '/{param*}',
            handler: {
                directory: {
                    path: '.',
                    index: ['index.html']
                }
            }
        })
        // ES EL METODO QUE INICIA EL SERVIDOR
        await server.start()
    } catch (error) {
        console.error(error)
        // SALIR DE NODEJS CON UN CÓDIGO DE ERROR (1), 0 ES UN CODIGO DE EXITO
        process.exit(1)
    }

    console.log(`Servidor lanzado en: ${server.info.uri}`)
}

// SE INICIALIZA EL PROCESO
init()
```

### 6. Plantillas con Handlebars

+ :link: [Handlebars.js NPN](https://www.npmjs.com/package/handlebars)
+ :link: [Handlebars Home page](https://handlebarsjs.com/)
+ :link: [Try Handlebars.js right now in your browser](http://tryhandlebarsjs.com/)
+ :link: [Installation Handlebars.js](https://handlebarsjs.com/installation/)

Las plantillas son generalmente archivos html con marcadores particulares que permiten la inserción de variables y la ejecución de algunas instrucciones de programación, antes de ser renderizados. Esta interpretación previa la realiza un plugin conocido como motor de plantillas, como es el caso de **Handlebars**.

Para incluir variables o instrucciones de código con **Handlebars** es necesario el uso de dobles llaves (o curly braces). Un bloque de html con **Handlebars** sería algo como lo siguiente:

```js
<div class=""post"">
  <h1>Author: {{fullName author}}</h1>
  <div class=""body"">{{body}}</div>

  <h1>Comments</h1>

  {{#each comments}}
  <h2>By {{fullName author}}</h2>
  <div class=""body"">{{body}}</div>
  {{/each}}
</div>
```
Los bloques de instrucción en Handlebars comienzan con `#` y se cierran con `/`.

Para más información, recuerda consultar la documentación oficial en :link: [Handlebarsjs Minimal templating on steroids](http://handlebarsjs.com/) y así conocer mucho más de las opciones que te brinda este potente motor de plantillas.

Para instalar Handlebars
```bash
$ npm i handlebars
```


### 7. Renderizado de vistas - Layout y template del home

En Hapi podemos usar la arquitectura **MVC** (_Modelo-Vista-Controlador_) para organizar la lógica de nuestras aplicaciones. Para implementar el uso de vistas es necesario instalar el plugin _Vision_ y configurarlo de la siguiente manera:

Se tienen que instalar :link: [@hapi/vision](https://www.npmjs.com/package/@hapi/vision) que es el renderisador de templates que ocupa Hapi

:link: [Documentacion vision Template rendering support for hapi.js](https://hapi.dev/module/vision/)

```js
server.views({
  engines: { // --- HAPI PUEDE USAR DIFERENTES ENGINES
    hbs: handlebars // --- ASOCIAMOS EL PLUGIN AL TIPO DE ARCHIVOS  
  },
  relativeTo: __dirname, // --- PARA QUE LAS VISTAS LAS BUSQUE FUERA DE /PUBLIC
  path: 'views', // --- DIRECTORIO DONDE COLOCAREMOS LAS VISTAS DENTRO DE NUESTRO PROYECTO
  layout: true, // --- INDICA QUE USAREMOS LAYOUTS 
  layoutPath: 'views' // --- UBICACIÓN DE LOS LAYOUTS
})
```
Al crear el archivo `layout.hbs` evitaremos repetir las mismas secciones de html en cada una de las vistas, remplazando sólo lo relativo al contenido que cambiará según las rutas definidas en nuestra aplicación.

En la definición de las rutas, tendremos que cambiar la respuesta devuelta en handler para que invoque a `h.view()` en lugar de `h.file()`, con los parámetros esperados por el layout.

Para poder incorporar el html de las vistas dentro del `layout.hbs`, es necesario usar _triples llaves_ en lugar de dobles, ya que por defecto _Handlebars_ escapa el código html convirtiéndolo en su equivalente texto plano.

Para instalar _Handlebars_ & _Vision_
```bash
$ npm i handlebars @hapi/vision
```
Se crea la carpeta `views` la cual contendra la plantillas con la extención  `.hsb` con los archivos `index.hbs` y `layout.hbs` a la altura de `packages.json`

El index --> layout
```js
'use strict'

const Hapi = require('@hapi/hapi');
// SE IMPORTA EL PLUGING PARA SERVIR LOS ARCHIVOS ESTATICOS
const inert = require('@hapi/inert');
// SE IMPORTA VISION PARA RENDESIZAR LOS TEMPLATES
const Vision = require('@hapi/vision');
// SE IMPORTA path QUE PARTE DE NODE
const path = require('path');
// SE EIMPORTA HANDLEBARS
const handlebars = require('handlebars');


// SE CREA EL SERVIDOR COMO OBJETO 
const server = Hapi.Server({
    // EL PUERTO SE ESTABLECE COMO PARAMETRO CON LA VARIALBLE DE ENTORNO PORT Y SI NO CON EL PUERTO 3000
    port: process.env.PORT || 3000,
    // CORRE EN EL LOCALHOST
    host: 'localhost',
    // SE DECLRAR LA VARIABLE/OBJETO PARA DECLRAR LA RUTA A LA CARPETA DE ARCHIVOS ESTATICOS
    routes: {
        files: {
            relativeTo: path.join(__dirname, 'public')
        }
    }
})
// CONFIGURACIÓN DE LAS RUTAS
const initRoutes = async () =>{
    // DEFINICIÓN DE RUTAS SE INDICA EL MÉTODO HTTP, URL Y CONTROLADOR/handler DE RUTA
    // SE DECLARAN DESPUÉS DEL PLUGIN YA QUE LAS RUTAS HACEN USO DEL MISOM PARA DEVOLVER ARCHIVOS ESTATICOS
    server.route({
        method: 'GET',
        path: '/',
        handler: (req, h) => {
            // METODO h REGRESA LA VISTA index EN EL LAYOUT CON EL VALOR EN EL OBJETO
            return h.view('index', {
                title: 'home'
            })
        }
    })
    // RUTA PARA SERVIR ARCHIVOS ESTÁTICOS ASOCIADOS (IMG/CSS/JS)
    server.route({
        method: 'GET',
        path: '/{param*}',
        handler: {
            directory: {
                path: '.',
                index: ['index.html']
            }
        }
    })
}
// CONFIGURACION DE PANTILLAS
const initViews = async ()=>{
    server.views({
        // EL ENGINE ES hbs: handlebars
        engines: {
          hbs: handlebars
        },
        // SE BUSCA APARTIR DEL DIRECTORIO ACTUAL
        relativeTo: __dirname,
        // LAS VISTAS SE ENCUENTRAN EN VIEWS(DIRECTORIO)
        path: 'views',
        // SE HABILITA LAYOUT PARA NO REPETIR PEDASOS DE HTML EN TODAS LAS VISTAS
        layout: true,
        // LOS LAYOUTS SE ENCUENTRAN EN VIEW(DIRECTORIO) ESTABLECEMOS LA DIFERENCIA
        layoutPath: 'views'
    })
}
// FUNCION INICIAL
const main = async () =>{
    try {
        // REGISTRAR LOS PLUGINS QUE HAPI VA A NECESITAR PARA SERVIR ARCHIVOS ESTATICOS
        await server.register(require('@hapi/inert'));
        // SE REGISTRA VISION
        await server.register(Vision)
        // ES EL METODO QUE INICIA EL SERVIDOR
        await server.start()
        await initRoutes()
        await initViews()

    } catch {
        console.error(error)
        // SALIR DE NODEJS CON UN CÓDIGO DE ERROR (1), 0 ES UN CODIGO DE EXITO
        console.exit(1)
    }finally{
        console.log(`Servidor lanzado en ${server.info.uri}`)
    }
}
// SE INICIALIZA EL PROCESO
main()

```
**NOTA**: Commit en mi repo "Mod. apuntes _7. Renderizado de vistas - Layout y template del home_"


### 8. Recibiendo parámetros en una ruta POST - Creación del registro
El objeto request nos permite obtener datos de la petición recibida desde el cliente. El método pasado como parámetro para la creación de este objeto define si trabajaremos con _GET_ o _POST_.

- Proipiedades del request:
    + `equest.path`
    + `equest.method`
    + `equest.get`
    + `request.payload`: es en esta propiedad donde recibimos los datos enviados con el método POST.

- _Ciclo de vida del objeto request_, se refiere a los eventos que suceden durante la carga, existencia y descarga del objeto:
    + OnRequest
    + OnPreAuth
    + OnCredentials
    + OnPostAuth
    + OnPreHandler
    + OnPostHandler
    + OnPreResponse

Más información sobre el ciclo de vida del objeto request en el repositorio oficial del proyecto: :octocat: [Request lifecycle](https://github.com/hapijs/hapi/blob/master/API.md#request-lifecycle)

Código: Definimos rutas GET y POST para registrar usuarios y recibir
parámetros en el request.

Se añade una nueva ruta `/register` junto con su vista archivo `register.html` en _public_ y su archivo en _views_ `register.hbs` en la carpeta _public_
```js
// RUTA REGISTER GET
    server.route({
        method: 'POST',
        path: '/registyer',
        handler: (req, h) => {
            // METODO h REGRESA LA VISTA index EN EL LAYOUT CON EL VALOR EN EL OBJETO
            return h.view('register', {
                title: 'Registro'
            })
        }
    })
// RUTA REGISTER POST
    server.route({
        method: 'POST',
        path: '/create-user',
        handler: (req, h) => {
            // PROPIEDAD DONDE SE RECIBEN LOS DATOS
            console.log(req.payload)
            return 'USUARIO CREADO EXITOSAMENTE'
        }
    })
```
El `action` del formulario se tiene que setear a la ruta POST `/create-user` **en el view**

Lo que en consola de debe de ver con `console.log(req.payload)`
```bash
[Object: null prototype] {
  name: 'rodolfo',
  email: 'mack@mail.com',
  password: 'sdfasdfasdfasf'
}
```

### 9. Definir una mejor estructura con buenas prácticas en Hapi
### 10. Validando la información - Implementando Joi
### 11. Introducción a Firebase
### 12. Creando un modelo y guardando en firebase
### 13. Implementando el login y validación del usuario
### 14. Autenticación de usuarios - Cookies y estado
### 15. Manejando errores
### 16. Visualización de errores
### 17. Controlar el error 404 en inert y el error de validación
### 18. Repaso - Creación del modelo y controlador para preguntas
### 19. Repaso - Creación de las rutas para crear preguntas
### 20. Listar las últimas preguntas en el home


## 3. Aplicacion de conceptos avanzados
### 21. Enrutamiento avanzado - visualizando una pregunta


### 22. Enrutamiento avanzado - respondiendo una pregunta
### 23. Generando la lógica de la plantilla según si es creador o contribuidor
### 24. Métodos de servidor - respuesta correcta
### 25. Usando métodos de servidor
### 26. Manejo del caché - Agregando el home al caché
### 27. Procesamiento de archivos - Aceptando imágenes
### 28. Logging con Good - Monitoreando el servidor
### 29. Creación de plugins - Teoría
### 30. Creación de plugins - Implementando un API REST
### 31. Estrategías de autenticación - Asegurando el API REST
### 32. Seguridad básica - Asegurando el servidor contra CSRF
### 33. Seguridad básica - Asegurando el servidor contra XSS


## 4. Herramientas de desarrollo
### 34. Depuración del proyecto


### 35. Ecosistema de Hapi







































































