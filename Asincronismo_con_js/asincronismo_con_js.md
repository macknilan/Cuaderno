

# Curso de Asincronismo con JavaScript


**API**
> Interfaz de programación de aplicaciones (Application Programming Interface). Es un conjunto de rutinas que provee acceso a funciones de un determinado software.

**Concurrencia**
> Cuando dos o más tareas progresan simultáneamente.

**Paralelismo**
> Cuando dos o más tareas se ejecutan, literalmente, a la vez, en el mismo instante de tiempo.

**Bloqueante**
> Una llamada u operación bloqueante no devuelve el control a nuestra aplicación hasta que se ha completado. Por tanto el thread queda bloqueado en estado de espera.

**Síncrono**
> Es frecuente emplear 'bloqueante' y 'síncrono' como sinónimos, dando a entender que toda la operación de entrada/salida se ejecuta de forma secuencial y, por tanto, debemos esperar a que se complete para procesar el resultado.

**Asíncrono**
> La finalización de la operación I/O se señaliza más tarde, mediante un mecanismo específico como por ejemplo un callback, una promesa o un evento, lo que hace posible que la respuesta sea procesada en diferido.

**Call Stack**
> La pila de llamadas, se encarga de albergar las instrucciones que deben ejecutarse. Nos indica en que punto del programa estamos, por donde vamos.

**Heap**
> Región de memoria libre, normalmente de gran tamaño, dedicada al alojamiento dinámico de objetos. Es compartida por todo el programa y controlada por un recolector de basura que se encarga de liberar aquello que no se necesita.

**Cola o Queue**
> Cada vez que nuestro programa recibe una notificación del exterior o de otro contexto distinto al de la aplicación, el mensaje se inserta en una cola de mensajes pendientes y se registra su callback correspondiente.

**Eventloop o Loop de eventos**
> Cuando la pila de llamadas (call stack) se vacía, es decir, no hay nada más que ejecutar, se procesan los mensajes de la cola. Con cada 'tick' del bucle de eventos, se procesa un nuevo mensaje.

**Hoisting**
> Sugiere que las declaraciones de variables y funciones son físicamente movidas al comienzo del código en tiempo de compilación.

**DOM**
> DOM permite acceder y manipular las páginas XHTML como si fueran documentos XML. De hecho, DOM se diseñó originalmente para manipular de forma sencilla los documentos XML. 

**XML**
> Lenguaje de marcado creado para la transferencia de información, legible tanto para seres humanos como para aplicaciones informáticas, y basado en una sencillez extrema y una rígida sintaxis. Así como el HTML estaba basado y era un subconjunto de SGML, la reformulación del primero bajo la sintaxis de XML dio lugar al XHTML; XHTML es, por tanto, un subconjunto de XML.

**Events**
> Comportamientos del usuario que interactúa con una página que pueden detectarse para lanzar una acción, como por ejemplo que el usuario haga click en un elemento (onclick), que elija una opción de un desplegable (onselect), que pase el ratón sobre un objeto (onmouseover), etc.

**Compilar**
> Compilar es generar código ejecutable por una máquina, que puede ser física o abstracta como la máquina virtual de Java.

**Transpilar**
> Transpilar es generar a partir de código en un lenguaje código en otro lenguaje. Es decir, un programa produce otro programa en otro lenguaje cuyo comportamiento es el mismo que el original.


## 1. Apropiar los conceptos de asincronismo
### 1. Bienvenida al curso

```javascript
```

### 2. Introducción al asincronismo

JavaScript es un lenguaje de programación "asíncrono" y "no bloqueante", con un manejador de eventos, mejor conocido como "Event Loop", implementado en un unico hilo para sus interfases de entrada y salida.

**Asincronismo es la acción que no ocurre al mismo tiempo**

### 3. Presentación del reto

Consumir la API de :link: [THE RICK AND MORTY API](https://rickandmortyapi.com/)

## 2. Desarrollar soluciones utilizando asicronismo
### 4. Definición Estructura Callback

> Se define como la función que es pasada como parámetro, mas no la función que lo recibe.

Una funcion que recibe como argumento otra funcion se ejecuta cuando es llamada

Crear la siguiente estructura
```bash
asincronismo
├── package.json
└── src
    └── callback
        └── index.js

```
`package.json`
```javascript
{
  "name": "asincronismo",
  "version": "1.0.0",
  "description": "trabajar con asincronismo con JavaScript",
  "main": "src/index.js",
  "scripts": {
    "callback": "node src/callback/index.js"
  },
  "keywords": [
    "callbacks",
    "promise",
    "async"
  ],
  "author": "",
  "license": "MIT"
}
```
`index.js`
```javascript
function sum(num1, num2) {
    return num1 + num2;
}

function calc(num1, num2, callback) {
    return callback(num1, num2);
}

console.log(calc(2, 7, sum));

// ------------------------------------------

function date(callback) {
    console.log(new Date);

    setTimeout(()=>{ 
        // ESTE CODIGO SE EJECUTA DESPUES DE UN TIEMPO ESPECIFICADO
        let date = new Date;
        // SE EJECUTA LA FUNCION QUE NUESTRA FUNCION DATE RECIBE COMOPARAMETRO
        callback(date); 
    },3000);
}

// ESTA SERA LA FUNCION MANDADA A LLAMAR COMO CALLBACK
function printDate(dateNow){
    console.log(dateNow);
}

date(printDate);
```

Poara ejecutar este archivo `npm run callback`


### 5. Peticiones a APIs usando Callbacks
1. Se tiene obtener la información del API de :link: [Rick and Morty Character](https://rickandmortyapi.com/api/character/)
2. Se tiene que instalar el programa de Postmand [Postman](https://www.postman.com/)
3. :link: [AJAX - Server Response](https://www.w3schools.com/xml/ajax_xmlhttprequest_response.asp)

+ Los estados de un request de acuerdo a la documentacion:
    1. request not initialized
    2. server connection established
    3. request received
    4. processing request
    5. request finished and response is read

Instalar dependencia de npm `npm install xmlhttprequest` por que este ejemplo se esta haciendo con node.js

XMLHttpRequest fue desarrollado por Microsoft

Archivo `chalenge.js` en la carpeta `/asincronismo/src/callback/` oara hacer el llamado a la API mediante XMLHttpRequest

```javascript
let XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest;

function fetchData(url_api, callback) {
    let xhttp = new XMLHttpRequest();
    xhttp.open('GET', url_api, true); // EL VALOR DE true ES ACTIVAR EL ASINCRONISMO EN XMLHttpRequest POR DEFAULT ESTA ACTIVADO
    xhttp.onreadystatechange = function (event) {
        if(xhttp.readyState === 4) { // VELIDACIÓN DE CONEXION EXITOSA
            if(xhttp.status === 200) { // VELIDACIÓN DE LA CONECCIÓN FUE ACEPTADA
                callback(null, JSON.parse(xhttp.responseText)) // DENTRO DE NODE EL 1ER VALOR ES EL ERROR, Y EL SEGUNDO ES LA INFO DEL RESULTADO DEL API
            } else {
                const error = new Error('Error' + url_api);
                return callback(error, null)
            }
        }
    }
    xhttp.send();
}
```

### 6. Múltiples Peticiones a un API con Callbacks

Pregunta
Es recomendable de no realizar mas de 3 callback para no caer en un callback Hell, si tu proyecto tiene una funcion con mas de 3 callback, se recomienda hacer una revision y utilizar una mejor forma de ejecutar el codigo, para ello estan las promesas o el Async Away

En el archivo `package.json` se añade la linea para ejecutar directamente un archivo dentro de nuestro proyecto.
```json
"callback:challenge": "node src/callback/challenge.js"
```
Para que quede de la siguiente manera
```javascript
{
  "name": "asincronismo",
  "version": "1.0.0",
  "description": "trabajar con asincronismo con JavaScript",
  "main": "src/index.js",
  "scripts": {
    "callback": "node src/callback/index.js",
    "callback:challenge": "node src/callback/challenge.js"
  },
  "keywords": [
    "callbacks",
    "promise",
    "async"
  ],
  "author": "",
  "license": "MIT",
  "dependencies": {
    "xmlhttprequest": "^1.8.0"
  }
}
```
Y se ejecute..
```bash
$ npm run callback:challenge
```
Se tiene que ejecutar el archivo y mostrar el resultado del API
```bash
npm run callback:challenge

> asincronismo@1.0.0 callback:challenge /home/mack/Documents/mi_cuaderno/Asincronismo_con_js/asincronismo
> node src/callback/challenge.js

493
Rick Sanchez
Dimension C-137
```
Archivo `challenge.js`
```javascript
let XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest;
let API = 'https://rickandmortyapi.com/api/character/';

function fetchData(url_api, callback) {
    let xhttp = new XMLHttpRequest();
    xhttp.open('GET', url_api, true); // EL VALOR DE true ES ACTIVAR EL ASINCRONISMO EN XMLHttpRequest POR DEFAULT ESTA ACTIVADO
    xhttp.onreadystatechange = function (event) {
        if(xhttp.readyState === 4) { // VELIDACIÓN DE CONEXION EXITOSA
            if(xhttp.status === 200) { // VELIDACIÓN DE LA CONECCIÓN FUE ACEPTADA
                callback(null, JSON.parse(xhttp.responseText)) // DENTRO DE NODE EL 1ER VALOR ES EL ERROR, Y EL SEGUNDO ES LA INFO DEL RESULTADO DEL API
            } else {
                const error = new Error('Error' + url_api);
                return callback(error, null)
            }
        }
    }
    xhttp.send();
}

fetchData(API, function(error1, data1) {
    if (error1) return console.error(error1);
    fetchData(API + data1.results[0].id, function (error2, data2) {
        if (error2) return console.error(error2);
            fetchData(data2.origin.url, function (error3, data3) {
                if (error3) return console.error(error3);
                    console.log(data1.info.count)
                    console.log(data2.name)
                    console.log(data3.dimension)
            });
    })
});
```



### 7. Implementando Promesas
En el archivo `package.json` se añade la linea para ejecutar directamente un archivo dentro de nuestro proyecto.
```json
"promise": "node src/promise/index.js"
```
El archivo `index.js` que esta en la ruta `asincronismo/src/promise/` queda de la siguiente manera.
```javascript

const somethingWillHappen = () => {
    return new Promise((resolve, reject) => {
        if (true) {
            resolve('Hey');
        } else {
            reject('Whoooops');
        }

    });
};

somethingWillHappen()
    .then(response => console.log(response))
    .catch(err => console.error(err));


const somethingWillHappen2 = () => {
    return new Promise((resolve, reject) =>  {
        if (true) {
            setTimeout(() => {
                resolve('True')
            }, 2000)
        } else {
            const error = new Error('Whoooops');
        }

    });
}

somethingWillHappen2()
    .then(response => console.log(response))
    .catch(err => console.error(err));


Promise.all([somethingWillHappen(), somethingWillHappen2()])
    .then(response => {
        console.log('Array of result',  response);
    })
    .catch(err => {
        console.error(err);
    })
```

### 8. Resolver problema con Promesas
> The **Promise** object represents the eventual completion (or failure) of an asynchronous operation, and its resulting value.

+ :link: [Promise MDN web docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
+ :link: [Promises In Javascript A Complete Guide For 2019](https://dev.to/nileshsanyal/promises-in-javascript-a-complete-guide-for-2019-4o99)

Se crea el archivo `fechData.js` en la ruta de nuestro proyecto `/asincronismo/src/utils/` el cual se encarga de ejecutar la _Promesa_ con el metodo `XMLHttpRequest` y se exporta como modulo para quelo consuma el archivo `challenge.js`

```javascript
let XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest;
// let API = 'https://rickandmortyapi.com/api/character/';

const fetchData = (url_api) => {

    return new Promise((resolve, reject) => {

        const xhttp = new XMLHttpRequest();
        xhttp.open('GET', url_api, true); // EL VALOR DE true ES ACTIVAR EL ASINCRONISMO EN XMLHttpRequest POR DEFAULT ESTA ACTIVADO
        xhttp.onreadystatechange = (() => {
            if (xhttp.readyState === 4) { // VELIDACIÓN DE CONEXION EXITOSA
                (xhttp.status === 200) ? resolve(JSON.parse(xhttp.responseText)) : reject(new Error('Error', url_api))
            }
        });
        xhttp.send();
    });
}
module.exports = fetchData;
```

Se crea el archivo `challenge.js` que esta en la ruta `asincronismo/src/promise/` he importa el modulo `fetchData` que ejecuta la _promesa_ y con el archivo `challenge.js` se encadenan las promesas para asociar acciones en la promesa. Y estos métodos devuelven un objeto de promesa recien generado que opcionalmente se puede usar para encadenar.
```javascript
const fetchData = require('../utils/fechData');
const API = 'https://rickandmortyapi.com/api/character/';

fetchData(API)
    .then(data => {
        console.log(data.info.count);
        return fetchData(`${API}${data.results[0].id}`)
    })
    .then(data => {
        console.log(data.name)
        return fetchData(data.origin.url)
    })
    .then(data => {
        console.log(data.dimension)
    })
    .catch(err => {
        console.error(err)
    });
```
En el archivo `package.json` se agrega la linea `"promise:challenge": "node src/promise/challenge.js"` para poder ejecutar la promesa con _npm_
```javascript
{
  "name": "asincronismo",
  "version": "1.0.0",
  "description": "trabajar con asincronismo con JavaScript",
  "main": "src/index.js",
  "scripts": {
    "callback": "node src/callback/index.js",
    "callback:challenge": "node src/callback/challenge.js",
    "promise": "node src/promise/index.js",
    "promise:challenge": "node src/promise/challenge.js"
  },
  "keywords": [
    "callbacks",
    "promise",
    "async"
  ],
  "author": "",
  "license": "MIT",
  "dependencies": {
    "xmlhttprequest": "^1.8.0"
  }
}
```

### 9. Conociendo Async/await

Se crea el archivo `index.js` en la ruta `/asincronismo/src/async/` para escribir el ejemplo de como funciona **async/await** y como debe de ser la manera correcta para usar el **try/catch** en caso de que algo suceda mal. 
```javascript
const doSomethingAsync = () => {
    return new Promise ((resolve, reject) => {
        (true) ? setTimeout(() => resolve('Do something Async'), 3000) : reject(new Error('Test error'))
    });
}

const doSomething = async () => {
    const something = await doSomethingAsync();
    console.log(something);
}

console.log('Before')
doSomething();
console.log('After')


const anotherFunction = async () => {
    try {
        const something = await doSomethingAsync();
        console.log(something);
    } catch(error) {
        console.log(error)
    }
}

console.log('Before_1')
anotherFunction();
console.log('After_1')
```
En el archivo `package.json` se escribe la linea `"async": "node src/async/index.js"`  par apoder ejecutar el archivo en especifivo con **npm**


### 10. Resolver problema con Async/Await

Se crea el archivo `challenge.js` en la ruta `/asincronismo/src/async/` el cual hace referencia al archivo `fechData.js`

```javascript
const fetchData = require('../utils/fechData');
const API = 'https://rickandmortyapi.com/api/character/';

const anotherFunction = async (url_api) => {
    try {
        const data = await fetchData(url_api);
        const character = await fetchData(`${API}${data.results[0].id}`);
        const origin = await fetchData(character.origin.url);
        console.log(data.info.count)
        console.log(character.name)
        console.log(origin.dimension)
    } catch (error) {
        console.error(error);
    }
}
console.log('Before')
anotherFunction(API);
console.log('After')
```
En el archivo `package.json` se agrega la linea
```javascript
"async:challenge": "node src/async/challenge.js"
```
para ejecutar el archivo `npm run async:challeng` para que tenga la siguiente salida.
```bash
Before
After
493
Rick Sanchez
Dimension C-137
```


## 3. Comprender las diferencias entre las estructuras asíncronas
### 11. Callbacks Vs Promesas Vs Async/Await
+ **Callbacks**
    * _Ventajas_: Simple(una función que recibe otra función). Son universales, corren en cualquier navegador.
    * _Desventajas_: Composición tediosa, anidando cada vez más elementos. Caer en Callback Hell.

+ **Promesas**
    + _Ventajas_: Facilmente enlazables .Then( return… ).Then - Fácil e intuitivo de leer.
    + _Desventajas_: Posible error si no se retorna el siguiente llamado. No corre en todos los navegadores.

+**Async-Await**
    * _Ventajas_: Se puede usar try-catch . Código más ordenado e intuitivo.
    * _Desventajas_: No corre en todos los navegadores (se requiere un transpilador).










