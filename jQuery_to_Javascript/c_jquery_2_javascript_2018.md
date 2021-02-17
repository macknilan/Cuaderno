
# Jquery to Javascript

* :link: [Promesas - async - await ](https://dev.to/ardennl/about-promises-and-async--await-5ebm)
* :link: [Learn ES6 without leaving Dev.to](https://dev.to/andersonjoseph/learn-es6-without-leave-devto-57o3)
* :link: [Lista de API's publicas](https://github.com/toddmotto/public-apis)
* :link: [Lista de API's publicas "local-file-in-repo" ](https://github.com/macknilan/Cuaderno/blob/master/jQuery_to_Javascript/Public_APIs.md)
* :link: [The Vanilla JS Toolkit](https://vanillajstoolkit.com/code-snippets/)
* :link: [ES2015+ cheatsheet](https://devhints.io/es6)
* :link: [You might not need jQuery](http://youmightnotneedjquery.com/)



### Async Arrow functions 

La **async arrow function** seria asi...
```javascript
const foo = async () => {
    // do something
}
```

La **anonima** async arrow function seria asi...
```javascript
const foo = async function() {
    // do something
}
```

La **declaración** de la funcion async arrow seria asi...
```javascript
async function foo() {
    // do something
}
```

Usando la funcion async en un **callbak**
```javascript
const foo = event.onCall(async () => {
    // do something
})
```

## Promesas

```javascript
// SE REGRESA -resolve- -reject- VASADOS EN EL VALOR QUE SE LE PASO POR PARAMETRO
function isTonyStark(name) {
    // SE CREA LA PROMESA CON ARROWFUNCTION
    return new Promise((resolve, reject) => {
        if (name === 'Tony') {
            resolve(`Welcome ${name}`);
        } else {
            reject(Error('Danger, Will Robinson, danger!'));
        }
    });
}
// CONSUMIR UNA PROMESA
isTonyStark('Tony')
    .then(console.log)
    .catch(err => console.error(err));
```

```javascript
// CONSUMIR VARIAS PROMESAS A LA VEZ.
// EL THEN SE EJECUTAN CUANDO TERMINEN TODAS LAS PROMESAS.
// EL CATCH SE EJECUTA EN EL PRIMER ERROR.
Promise.all([
  promesa1,
  promesa2
])
.then(function() {})
.catch(function() {})

// SE EJECUTA EL THEN DE LA PROMESA QUE TERMINE PRIMERO.
Promise.race([
  promesa1,
  promesa2
])
.then(function() {})
.catch(function() {})
```

## Ajax

### Ajax con jQuery

```javascript
$.ajax({
    type: "POST", // GET, DELETE, PUT
    url: '/ruta/del/API/', // -VARIABLE QUE CONTIENE LA RUTA -RUTA DE LA PAGINA EN DONDE RECIVE LA DATA
    data: {
        'variable_a_pasar': valor_de_la_variable,
    },
    dataType: 'json',
    success: function(data) {
        console.log(data); // EN CASO DE SER EXITOSA LA RESPUESTA
    },
    error: function(data) {
        console.log(err); // EN CASO DE NO SER EXITOSA LA RESPUESTA
    }
});

```
## Ajax con JavaScript
Ejempo con [Random User Generator API -free-](https://randomuser.me/)
```javascript

fetch('https://randomuser.me/api/') // -VARIABLE QUE CONTIENE LA RUTA -RUTA DE LA PAGINA EN DONDE RECIVE LA DATA
    .then(function (response){
        // CUANDO UNA RESPUESTA ES CORRECTA LA RESPUESTA ES CORRECTA
        return response.json()
    })
    .then(function (user) {
        console.log('user', user.results[0].name.first)
    })
    .catch(function () {
        console.log('fallo algo... ')
    });
```
## Funciones asíncronas
Ejemplo mostrado con la API [https://yts.am/api -free-](https://yts.am/api)
```javascript
console.log(fetch('https://yts.lt/api/v2/list_movies.json')); // DEVUELVE UNA PROMESA -PENDIENTE-
```
__Ejemplo con arrow function__ en en [link](https://www.imdb.com/feature/genres/) es para saber los generos que estan disponibles. Action, Crime, Drama, Thriller

```javascript
// REGRESA LA PROMESA Y SE PUEDE VER EL STATUS OK
fetch('https://yts.lt/api/v2/list_movies.json?genres=sci-fy')
    .then(data => console.log(data));
```
```javascript
// REGRESA LA PROMESA Y SE PASAN LOS DATOS A FORMATO JSON
fetch('https://yts.lt/api/v2/list_movies.json?genres=sci-fy')
    .then(data => data.json()) // EN LA RESPUESTA EN __proto__ HAY UN METODO JSON, QUE REGRESA OTRA PROMESA
    .then(data => console.log(data)); // REGRESA UN ARRAY DE OBJETOS QUE SE OBTIENEN EN LA RESPUESTA
```

```javascript
// REGRESA LA PROMESA Y SE PRESENTA UN ERROR
fetch('yts.lt/api/v2/list_movies.json?genres=sci-fy')
    .then(data => data.json()) // EN LA RESPUESTA EN __proto__ HAY UN METODO JSON, QUE REGRESA OTRA PROMESA
    .then(data => console.log(data)) // REGRESA UN ARRAY DE OBJETOS QUE SE OBTIENEN EN LA RESPUESTA
    .catch(err => console.error('HAY UN ERROR EN LA CONSULTA DEL API -->', err));
```

El metodo **finaly** Retorna la promesa sin importar si esta es exitosa o es rechazada; puede ser de utilidad para poner a un estado inicial la promesa ejecutada.

* :link: [Finally - MDN web docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally)

```javascript
fetch('https://yts.lt/api/v2/list_movies.json?genres=sci-fy')
    .then(data => data.json()) // EN LA RESPUESTA EN __proto__ HAY UN METODO JSON, QUE REGRESA OTRA PROMESA
    .then(data => console.log(data)) // REGRESA UN ARRAY DE OBJETOS QUE SE OBTIENEN EN LA RESPUESTA
    .catch(err => console.error('HAY UN ERROR EN LA CONSULTA DEL API -->', err))
    .finally(() => console.log('FIN DE LA PROMESA'));
```

## Async / Await
Async/Await estan basadas en promesas. En orden para que **async** se ejecute, **await** se necesita una funcion para que retorne una promesa.

**await** "**SIEMPRE**" se necesita llamar de una funcion "**async**"

```javascript
function wait(ms) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(console.log(`waited for ${ms}ms`));
        }, ms);
    });
}

const go = async () => {
    await wait(600);
    await wait(1200);
    await wait(1800);
}
go();

// SALIDA
// waited for 600ms
// VM431:4 waited for 1200ms
// VM431:4 waited for 1800ms

```
```javascript
// Async/Await ARROW FUNCTION
const getData = async (url) =>  {
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
}
getData('https://yts.lt/api/v2/list_movies.json?genres=action');
```
Ejecutar al momento Async/Await Categorias Action, Crime, Drama, Thriller
```javascript
(async () => {
    const getData = async (url) => {
        const response = await fetch(url);
        const data = await response.json()
        return data;
    }
    const actionList = await getData('https://yts.lt/api/v2/list_movies.json?genres=action')
    const crimeList = await getData('https://yts.lt/api/v2/list_movies.json?genres=crime')
    const DramaList = await getData('https://yts.lt/api/v2/list_movies.json?genres=drama')
    const thrillerList = await getData('https://yts.lt/api/v2/list_movies.json?genres=thriller')
    console.log('actionList -->', actionList);
    console.log('crimeList -->', crimeList);
    console.log('DramaList -->', DramaList);
    console.log('thrillerList -->', thrillerList);
})()
```
## Selectores
Por convención una variable que este represente un objeto del DOM lleva el signo $, esto es para tener claro que estamos manipulando un objeto del DOM y no algún tipo de información o dato.

Dentro de JavaScript existen distintas funciones para hacer selectores, entre ellas se encuentra:

+ **getElementById**: recibe como parámetro el id del objeto del DOM que estás buscando. Te regresa un solo objeto.
+ **getElementByTagName**: recibe como parámetro el tag que estas buscando y te regresa una colección html de los elementos que tengan ese tag.
+ **getElementByClassName**: recibe como parámetro la clase y te regresa una colección html de los elementos que tengan esa clase.
+ **querySelector**: va a buscar el primer elemento que coincida con el selector que le pases como parámetro.
+ **querySelectorAll**: va a buscar todos los elementos que coincidan con el selector que le pases como parámetro.

### jQuery
```jquery
const $home = $(".home") // ELEMENTO CON LA CLASE HOME
const $home = $("#home") // ELEMENTO CON EL ID HOME
```

### Javascript

```javascript
// RETORNA UN ELEMENTO CON EL ID HOME
document.getElementById("home")

// RETORNA UNA LISTA DE ELEMENTOS CON LA CLASE HOME
document.getElementsByClassname("home")

// RETORNA UNA LISTA DE ELEMENTOS CON EL TAG DIV
document.getElementsByTagName("div")

// DEVUELVE EL PRIMER ELEMENTO QUE COINCIDA CON EL QUERY DE BÚSQUEDA.
document.querySelector("div .home #modal")

// DEVUELVE TODOS LOS ELEMENTOS QUE COINCIDAN CON EL QUERY DE BÚSQUEDA.
document.querySelectorAll("div .home #modal")

```
## Creación de templates
Para realizar debug en javascript se puede hacer escribiendo `debugger` despues de una variable para saver los valores que obtiene

### Jquery
Dentro de jQuery, la creación de un template seria con un texto base y si nuestro texto cuenta con distintas líneas más aparte tuviera valores dinámicos.

```javascript
function videoItemTemplate(src, title) {
  return (
    '<div class="primaryPlaylistItem">' +
      '<div class="primaryPlaylistItem-image">' +
        '<img src="' + src + '">' +
      '</div>' +
      '<h4 class="primaryPlaylistItem-title">' +
        title +
      '</h4>' +
    '</div>'
  )
}

```
### Javascript
Se usa una característica de ES6 que se llama `template literals`. Desde ECMAScript 6 contamos con una nueva característica llamada template literals que se representan con las comillas invertidas ` `` `

```javascript
functionv ideoItemTemplate(src, title) {
  return (
    `<div class="primaryPlaylistItem">
      <div class="primaryPlaylistItem-image">
        <img src="${src}">
      </div>
      <h4 class="primaryPlaylistItem-title">
        ${title}
      </h4>
    </div>`
  )
}

```
## Creación de DOM
Para la creación de documentos en el DOM y poder hacer uso de diferentes maneras (reutilización) se puede hacer con este __metodo__ para crear un nuevo HTML

* :link: [DOMImplementation.createHTMLDocument()](https://developer.mozilla.org/en-US/docs/Web/API/DOMImplementation/createHTMLDocument)
* :link: [Element.innerHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML)

`innerHTML` gets or sets the HTML or XML markup contained within the element.

```javascript
const actionList = await getData('https://yts.lt/api/v2/list_movies.json?genre=action')
console.log(actionList)

function funcionAEjecutar(title) {
  return (
    `<h1>${title}</h1>`
  )
}

const $nombreSelector = document.querySelector('#nombreID');
actionList.data.movies.forEach((movie) => {
    // debugger
    // SE TRAE LA PLANTILLA Y SE GUARDA EN UNA VARIABLE
    const HTMLString = funcionAEjecutar(movie); 
    const html = document.implementation.createHTMLDocument();
    // SE AGREGA LA NUEVA PLANTILLA AL DOM, ESTO HACE QUE LA PLANTILLA EN TEXTO SE CONVIERTA EN ELEMTOS DOM
    html.body.innerHTML = HTMLString;
    //SE AGREGA EL PRIMER HIJO (QUE ES DONDE SE ENCUENTRA LA PLANTILLA) AL CONTENEDOR DONDE SE QUIERE AGREGAR LA PLANTILLA
    $nombreSelector.append(html.body.children[0]);
}) 

```

## Eventos en Javascript

* :link: [MDN web docs Event reference](https://developer.mozilla.org/en-US/docs/Web/Events)
* :link: [Standard events](https://developer.mozilla.org/en-US/docs/Web/Events#Standard_events)
* :link: [EventTarget.addEventListener()](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)

### jQuery

```javascript
$("div").on("click", function(event) {

})
```
```javascript
const $element = document.getElementById("elementID");
$element.addEventListener("click", (event) => {

})
```
### Clases y estilos CSS

SOLO en chrome con el "Inspector de elementos" y la "Consola" al mismo tiempo en abiertos; se selecciona el elemento que se desea inspeccionar, despues en la **consola** con el elemento seleccionado se escribe `$0` (no es jQuery), seguido de un elemento que tenga el HTML.
```
$0.classList
```
```javascript
// AGREGA UNA CLASE
$element.classList.add("clase");

// REMUEVE UNA CLASE
$element.classList.remove("clase");

// INTERCAMBIA ENTRE AGREGAR Y REMOVER UNA CLASE
$element.classList.toggle("clase");
```
Estilos Inline

```javascript
$modal.style.animation = "modalOut .8s forwards";
```

## Creación de elementos y asignación de atributos

### jQuery
```javascript
$("#element").attr({
  src: "",
  height: ""
})
```
Para crear un elemento `ìmg` y se le asigna a una variable del DOM
```javascript
const $loader = document.createElement("img");
```
```javascript
function setAttributes($element, attributes) {
    for (const attribute in attributes) {
        $element.setAttribute(attribute, attributes[attribute]);
    }
}

const $loader = document.getElementById("img");

// SE CREA UNA FUNCION CON UN OBJETO DE LOS ATRIBUTOS A CREAR COMO SEGUNDO PARAMETRO
setAttributes($loader, {
    src: 'ruta/de/la/imagen.jpg',
    height: 50,
    width: 50,
})
```
### Formularios
* :link: [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData/FormData)

```javascript
<form action="" class="search" id="form">
    <input type="text" name="searchTextBox" placeholder="Buscar un artista o tema favorito"/>
</form>

const $form = document.getElementById('form');
cons data = new FormData($form);
data.get('searchTextBox'); // EL RESULTADO ES EL CONTENIDO DE -input- CON -name- "searchTextBox"

```

### Asignación de una variable por destructuración "Destructuring assignment"
* :link: [Destructuring assignment MDN web ocs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)
* :link: [Desestructuración en Javascript. Parte 1 - http://www.etnassoft.com](http://www.etnassoft.com/2016/07/04/desestructuracion-en-javascript-parte-1/)

```javascript
// EL FETCH DEVUELVE UNA PROMESA CON LA SIGUIENTE ESTRUCTURA: ->promesa.data.movies<-
// CON EL "destructuring assignmen" ESTAMOS CREANDO UNA VARIABLE QUE SE LLAMA "pelis" Y SOLO CONTIENE LA INFORMACIÓN DE MOVIES.
const { 
  data: {
    movies: pelis
  }
} = await fetch(`api_url`); 

// LO ANTERIOR SERÍA IGUAL A ESTO:
const response = await fetch(`api_url`);
const pelis = response.data.movies;
```

### DataSet's

* :link: [Using data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes)
* :link: [data-*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/data-*)

The `data-*` global attributes form a class of attributes called custom data attributes, that allow proprietary information to be exchanged between the HTML and its DOM representation by scripts.

HTML5 is designed with extensibility in mind for data that should be associated with a particular element but need not have any defined meaning. `data-*` attributes allow us to store extra information on standard, semantic HTML elements without other hacks such as non-standard attributes, extra properties on DOM, or `Node.setUserData()`.


```javascript
<divid="element"data-id="10"data-category="action"></div>

const $element = document.getElementById("element");

// GUARDA EL VALOR DE DATA-ID
const id = $element.dataset.id;
// GUARDA EL VALOR DE DATA-CATEGORY
const category = $element.dataset.category;

// parseInt("número", base)
let n = parseInt("500", 10)
```

### Encontrando elementos en una lista

* :link: [Array.prototype.find()](https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Objetos_globales/Array/find)

El método `find()` devuelve el valor del primer elemento del array que cumple la función de prueba proporcionada. En cualquier otro caso se devuelve `undefined`.

```javascript
var array1 = [5, 12, 8, 130, 44];

var found = array1.find(function(element) {
  return element > 10;
});

console.log(found);
// expected output: 12
```

### Manejo de errores

* :link: [try...catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
* :link: [error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
* :link: [throw](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)

```javascript
// ALGO SALIO MAL EN RESULTADO NO DESEADO Y SE CREA UN throw
throw new Error('No se encontró ningun resultado');


try {
    // CODIGO A EVALUAR Y QUE intente EJECUTARLO SIN ERRORES
    
} catch(error) {
    // CÓDIGO POR SI SUCEDE UN ERROR
    alert(error.message);
    // PUEDEN IR MAS LINEAS DE CODIGO DESPUES MOSTRAR EL MENSANJE
}
```
### Local Storage

* :link: [window.localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)

- `localStorage` permite almacenar datos sin tiempo de expiración
- `sessionStorage` permite almacenar datos. Estos datos se van a borrar cuando se termine la sessión del navegador

En local storage solo se puede guardar texto plano. No se pueden guardar objetos.

La propiedad `localStorage` te permite acceder al objeto local Storage. `localStorage` es similar a `sessionStorage`. La única diferencia es que, mientras los datos almacenados en `localStorage` no tienen fecha de expiración, los datos almacenados en `sessionStorage` son eliminados cuando finaliza la sesion de navegación - lo cual ocurre cuando se cierra el navegador.

Con `sessionStorage` los datos persisten sólo en la ventana/tab que los creó, mientras que con `localStorage` los datos persisten entre ventanas/tabs con el mismo origen.

```javascript
// ELIMINAR LOS DATOS
window.localStorage.clear();

// SETEAR UN VALOR
window.localStorage.setItem("nombre", "Toshi");

// OBTENER EL VALOR DE UN KEY
window.localStorage.getItem("nombre");

// SETEAR UN OBJETO
// PRIMERO SE TIENE QUE CONVERTIR EL OBJETO EN UN STRING
window.localStorage.setItem("objeto", JSON.stringify({"peli": "wonder woman"});
// window.localStorage.setItem("objeto", JSON.stringify(VARIABLE_PARA_MANDAR_POR_PARAMETRO);

// OBTENER EL VALOR DE UN TEXTO OBJETO Y CONVERTIRLO A OBJETO
JSON.parse(window.localStorage.getItem("objeto"));
```

### Obtener datos almacendos.

```javascript
async function cacheExist(category) {
    const listName = `${category}List`;
    const cacheList = window.localStorage.getItem(listName);

    if (cacheList)
    returnJSON.parse(cacheList);

    const { data: { movies: data } } = await getData(`${BASE_API}list_movies.json?genre=${category}`);
    window.localStorage.setItem(listName, JSON.stringify(data));
    return data;
}
```
Si se desea volver a traer los datos se puede hacer lo siguiente:

- Poner un botón que traiga los datos
-   Hacer un setTimeout que borre el localStorage.

```javascript
console.log('hola mundo!');
const noCambia = "Leonidas";

let cambia = "@LeonidasEsteban"

function cambiarNombre(nuevoNombre) {
  cambia = nuevoNombre
}

const getUserAll = new Promise(function(todoBien, todoMal) {
  // llamar a un api
  setTimeout(function() {
    // luego de 3 segundos
    todoBien('se acabó el tiempo');
  }, 5000)
})

const getUser = new Promise(function(todoBien, todoMal) {
  // llamar a un api
  setTimeout(function() {
    // luego de 3 segundos
    todoBien('se acabó el tiempo 3');
  }, 3000)
})

// getUser
//   .then(function() {
//     console.log('todo está bien en la vida')
//   })
//   .catch(function(message) {
//     console.log(message)
//   })

Promise.race([
  getUser,
  getUserAll,
])
.then(function(message) {
  console.log(message);
})
.catch(function(message) {
  console.log(message)
})



$.ajax('https://randomuser.me/api/sdfdsfdsfs', {
  method: 'GET',
  success: function(data) {
    console.log(data)
  },
  error: function(error) {
    console.log(error)
  }
})

fetch('https://randomuser.me/api/dsfdsfsd')
  .then(function (response) {
    // console.log(response)
    return response.json()
  })
  .then(function (user) {
    console.log('user', user.results[0].name.first)
  })
  .catch(function() {
    console.log('algo falló')
  });


(async function load() {
  // await
  // action
  // terror
  // animation
  async function getData(url) {
    const response = await fetch(url);
    const data = await response.json();
    if (data.data.movie_count > 0) {
      // aquí se acaba
      return data;
    }
    // si no hay pelis aquí continua
    throw new Error('No se encontró ningun resultado');
  }
  const $form = document.getElementById('form');
  const $home = document.getElementById('home');
  const $featuringContainer = document.getElementById('featuring');


  function setAttributes($element, attributes) {
    for (const attribute in attributes) {
      $element.setAttribute(attribute, attributes[attribute]);
    }
  }
  const BASE_API = 'https://yts.am/api/v2/';

  function featuringTemplate(peli) {
    return (
      `
      <div class="featuring">
        <div class="featuring-image">
          <img src="${peli.medium_cover_image}" width="70" height="100" alt="">
        </div>
        <div class="featuring-content">
          <p class="featuring-title">Pelicula encontrada</p>
          <p class="featuring-album">${peli.title}</p>
        </div>
      </div>
      `
    )
  }

  $form.addEventListener('submit', async (event) => {
    event.preventDefault();
    $home.classList.add('search-active')
    const $loader = document.createElement('img');
    setAttributes($loader, {
      src: 'src/images/loader.gif',
      height: 50,
      width: 50,
    })
    $featuringContainer.append($loader);

    const data = new FormData($form);
    try {
      const {
        data: {
          movies: pelis
        }
      } = await getData(`${BASE_API}list_movies.json?limit=1&query_term=${data.get('name')}`)

      const HTMLString = featuringTemplate(pelis[0]);
      $featuringContainer.innerHTML = HTMLString;
    } catch(error) {
      alert(error.message);
      $loader.remove();
      $home.classList.remove('search-active');
    }
  })

  function videoItemTemplate(movie, category) {
    return (
      `<div class="primaryPlaylistItem" data-id="${movie.id}" data-category=${category}>
        <div class="primaryPlaylistItem-image">
          <img src="${movie.medium_cover_image}">
        </div>
        <h4 class="primaryPlaylistItem-title">
          ${movie.title}
        </h4>
      </div>`
    )
  }
  function createTemplate(HTMLString) {
    const html = document.implementation.createHTMLDocument();
    html.body.innerHTML = HTMLString;
    return html.body.children[0];
  }
  function addEventClick($element) {
    $element.addEventListener('click', () => {
      // alert('click')
      showModal($element)
    })
  }
  function renderMovieList(list, $container, category) {
    // actionList.data.movies
    $container.children[0].remove();
    list.forEach((movie) => {
      const HTMLString = videoItemTemplate(movie, category);
      const movieElement = createTemplate(HTMLString);
      $container.append(movieElement);
      const image = movieElement.querySelector('img');
      image.addEventListener('load', (event) => {
        event.srcElement.classList.add('fadeIn');
      })
      addEventClick(movieElement);
    })
  }

  async function cacheExist(category) {
    const listName = `${category}List`;
    const cacheList = window.localStorage.getItem(listName);

    if (cacheList) {
      return JSON.parse(cacheList);
    }
    const { data: { movies: data } } = await getData(`${BASE_API}list_movies.json?genre=${category}`)
    window.localStorage.setItem(listName, JSON.stringify(data))

    return data;
  }

  // const { data: { movies: actionList} } = await getData(`${BASE_API}list_movies.json?genre=action`)
  const actionList = await cacheExist('action');
  // window.localStorage.setItem('actionList', JSON.stringify(actionList))
  const $actionContainer = document.querySelector('#action');
  renderMovieList(actionList, $actionContainer, 'action');

  const dramaList = await await cacheExist('drama');
  const $dramaContainer = document.getElementById('drama');
  renderMovieList(dramaList, $dramaContainer, 'drama');

  const animationList = await await cacheExist('animation');
  const $animationContainer = document.getElementById('animation');
  renderMovieList(animationList, $animationContainer, 'animation');

  // const $home = $('.home .list #item');
  const $modal = document.getElementById('modal');
  const $overlay = document.getElementById('overlay');
  const $hideModal = document.getElementById('hide-modal');

  const $modalTitle = $modal.querySelector('h1');
  const $modalImage = $modal.querySelector('img');
  const $modalDescription = $modal.querySelector('p');

  function findById(list, id) {
    return list.find(movie => movie.id === parseInt(id, 10))
  }

  function findMovie(id, category) {
    switch (category) {
      case 'action' : {
        return findById(actionList, id)
      }
      case 'drama' : {
        return findById(dramaList, id)
      }
      default: {
        return findById(animationList, id)
      }
    }
  }

  function showModal($element) {
    $overlay.classList.add('active');
    $modal.style.animation = 'modalIn .8s forwards';
    const id = $element.dataset.id;
    const category = $element.dataset.category;
    const data = findMovie(id, category);

    $modalTitle.textContent = data.title;
    $modalImage.setAttribute('src', data.medium_cover_image);
    $modalDescription.textContent = data.description_full
  }

  $hideModal.addEventListener('click', hideModal);
  function hideModal() {
    $overlay.classList.remove('active');
    $modal.style.animation = 'modalOut .8s forwards';

  }
```
