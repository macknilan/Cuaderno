
# Curso de Single Page Application con JavaScript Vanilla

## 1. Development
### 1. ¿Qué vamos a aprender?
JavaScript vanilla y consumo de API

### 2. Introducción a SPA
Creación de una SPA(Single App Aplication) para el consumo de del API de **Rick and Morthy** :link: [THE RICK AND MORTY API HEY, DID YOU EVER WANT TO HOLD A TERRY FOLD? I GOT ONE RIGHT HERE, GRAB MY TERRY FLAP](https://rickandmortyapi.com/)

**SPA** Son aplicaciones construidas con JavaScript que nos permiten cargar nuestro contenido una sóla vez, es decir, se envían los archivos HTML, CSS y JS una sóla vez al navegador y ahí es donde va a vivir toda nuestra aplicación, de tal forma que la aplicación no necesita ser recargada, por ello, si se necesita navegar en la aplicación, se navega entre secciones y no páginas.

- **Ventajas**
    + Son fáciles de debuggear.
    + Son fáciles de crear.

+ **Desventajas**
    + No es tan compatible con el SEO.
    + No es recomendable aplicarlas para grandes aplicaciones (Aplicación grande => más de 1000 usuarios y más de 50 secciones en la página).

1. Crear carpeta `cuentifico`
2. Dentro de la carpeta `cientifico` ejecutar `npm init`
    + description: single page application
    + keywords: javascript
    + license: (MIT)
3. La carpeta `scr` es donde esta el codigo
    1. Dentro de `scr` la carpeta `pages` donde estan las paginas del proyecto
    2. Dentro de `scr` la carpeta `routes` las rutas del proyecto
    3. Dentro de `scr` la carpeta `styles` los estilos del proyecto
    4. Dentro de `scr` la carpeta `util` utilerias del proyecto
    5. Dentro de `scr` la carpeta `index.js` la implementación del proyecto
6. `public` esta el codigo que vamos a utilizar y es el que se va aproducción.
    1. El archivo `index.html`

```bash
├── package.json
├── public
│   └── index.html
└── src
    ├── index.js
    ├── pages
    ├── routes
    ├── styles
    └── utils
```

### 3. Configurar el entorno de trabajo
Instalar donde se encuentra el archivo `package.json`
```bash
npm i @babel/core babel-loader html-webpack-plugin webpack webpack-cli webpack-dev-server --save-dev
```
Cada una de estos paquetes se pueden buscar el :link: [Npm Home page](https://www.npmjs.com/)

### 4. Preparar Webpack
A la misma altura del archivo `package.json` se crea el archivo `webpack.config.js` en el cual se configura como debe de funcionar `WebPack` para este proyecto especifico.
```javascript
const path = require('path'); // NOS PERMITE ACCEDER A DONDE ESTÁMOS EN LAS CARPETAS. YA SEA EN LOCAL O EN LA NUBE.
const HtmlWebpackPlugin = require('html-webpack-plugin'); // ARCHIVO NECESARIO PARA TRABAJAR CON HTML.

module.exports = {  // AQUÍ SE ENCUENTRA TODA LA CONFIGURACIÓN DE LO QUE VA A SUCEDER. MODULO PARA EXPORTAR.
    entry: './src/index.js', // PUNTO DE ENTRADA CON SU DIRECCIÓN.AQUÍ VIVE EL CÓDIGO INICIAL Y DE AQUÍ PARTE AL DESARROLLO
    output: { // DONDE SE ENVÍA EL PROYECTO ESTRUCTURADO Y COMPILADO LISTO PARA PRODUCCIÓN.
        path: path.resolve(__dirname, 'dist'),  // CREAMOS EL LUGAR DÓNDE SE EXPORTARÁ EL PROYECTO.
        filename: 'main.js'// ESTE ES EL NOMBRE DEL ARCHIVO FINAL PARA PRODUCCIÓN.
    },
    resolve: {
        extensions: ['.js'], // EXTENSIONES QUE VAMOS A UTILIZAR.
    },
    module: { // SE CREA UN MODULO CON LAS REGLAS NECESARIAS QUE VAMOS A UTILIZAR.
        rules: [    // REGLAS
            {   //  ESTRUCTURA DE BABEL
                test: /\.js?$/, // NOS PERMITE IDENTIFICAR LOS ARCHIVOS SEGÚN SE ENCUENTRAN EN NUESTRO ENTORNO. (REGEX)
                exclude: /node_modules/,    // EXCLUIMOS LA CARPETA DE NODE MODULES
                use: {
                    loader: 'babel-loader',    // UTILIZAR UN LOADER COMO CONFIGURACIÓN ESTABLECIDA.
                }
            }
        ]
    },
    plugins: [  // ESTABLECEMOS LOS PLUGINS QUE VAMOS A UTILIZAR
        new HtmlWebpackPlugin(    // PERMITE TRABAJAR CON LOS ARCHIVOS HTML
            {
                inject: true,   // CÓMO VAMOS A INYECTAR UN VALOR A UN ARCHIVO HTML.
                template: './public/index.html',    // DIRECCIÓN DONDE SE ENCUENTRA EL TEMPLATE PRINCIPAL
                filename: './index.html'// EL NOMBRE QUE TENDRÁ EL ARCHIVO
            }
        )
    ]
}
```
```json
{
    "name": "cientifico",
    "version": "1.0.0",
    "description": "single page appication",
    "main": "index.js",
    "scripts": {
        // COMPILAR TODO EL PROYECTO PARA MANDARLO A PRODUCCION
        "build": "webpack --mode production",
        // HABILITAR EL ENTORNO DE DARROLLO
        "start": "webpack-dev-server --open --mode development"
    },
    "keywords": [
        "javascript"
    ],
    "author": "",
    "license": "(MIT)",
    "devDependencies": {
        "@babel/core": "^7.9.0",
        "babel-loader": "^8.1.0",
        "html-webpack-plugin": "^4.2.0",
        "webpack": "^4.43.0",
        "webpack-cli": "^3.3.11",
        "webpack-dev-server": "^3.10.3"
    }
}
```

## 2. Templates
### 5. Crear el Home
Ejecutar `npm run build` para compilar el proyecto con webpack y ver que todo este correcto y se crea la carpeta `dist` y dentro estan
```
├── index.html
└── main.js
```
Dentro de la carpeta de `pages` se crea el archivo `Home.js`
```javascript
const Home = () => {
    const view = `
        <div class="Characters">
            <article class="Character-item">
                <a href="#/1/">
                    <img src="image" alt="name">
                    <h2>Name</h2>
                </a>
            </article>
        </div>
    `;
    return view;
};
export default Home;
```

### 6. Crear template de personajes
Crear los diferentes templates que hacen falta.

Dentro de carpeta `src` crear la carpta `templates` secciones que no son paginas pero son parte de un apagina.

Se crea el archivo `Header.js`
```javascript
const Header = () => {
    const view = `
        <div class="Header-main">
            <div class="Header-logo">
                <h1>
                    <a href="/">
                        100tifi.co
                    </a>
                </h1>
            </div>
            <div class="Header-nav">
                <a href="#/about/">
                    About
                </a>
            </div>
        </div>
    `;
    return view;
};
export default Header;
```
Se crea el archivo `Character.js` dentro de la carpeta `pages`
```javascript
const Character = () => {
    const view = `
        <div class="Characters-inner">
            <article class="Characters-card">
                <img src="image" alt="name">
                <h2>Name</h2>
            </article>
            <article class="Characters-card">
                <h3>Episodes:</h3>
                <h3>Status:</h3>
                <h3>Species:</h3>
                <h3>Gender:</h3>
                <h3>Origin:</h3>
                <h3>Last Location:</h3>
            </article>
        </div>
    `;
    return view;
};
export default Character;
```
### 7. Crear página de error 404
Se crea el archivo `Error404.js` dentro de la carpeta `pages`
```javascript
const Error404 = () => {
    const view = `
        <div class="Error404">
            <h2>Error 404</h2>
        </div>
    `;
    return view;
};
export default Error404;
```
Con el comando `npm run start` se compila el proyecto y si al final del resultado se muestra `ℹ ｢wdm｣: Compiled successfully.` quiere decir que esta bien.

## 3. Router
### 8. Crear rutas del sitio
:link: [Wikipedia ECMAScript](https://en.wikipedia.org/wiki/ECMAScript)

1. 6th Edition - ECMAScript 2015
2. 7th Edition - ECMAScript 2016
3. 8th Edition - ECMAScript 2017
4. 9th Edition - ECMAScript 2018
5. 10th Edition - ECMAScript 2019


Se crea el archivo `index.js` dentro de la carpeta `routes` para importar los templates para y maejar las rutas para el render de la aplicacion.
```javascript
import Header from '../templates/Header';
import Home from '../pages/Home';
import Character from '../pages/Character';
import Error404 from '../pages/Error404';

const routes = {
    '/': Home,
    '/:id': Character,
    '/contact': 'Contact',
};

// MANEJADOR HACER RENDER DE NUESTROS TEMPLATES A ESTA FUNCION
const router = async() => {
    const header = null || document.getElementById('header');
    const content = null || document.getElementById('content');

    header.innerHTML = await Header();
};

export default router;
```
Dentro de la carpta `src` en el archivo `index.js` se importan las rutas del archivo `index.js` de la carpeta `routers`
```javascript
import router from './routes';

window.addEventListener('load', router);
```
Se comprueba con el comando `npm run start` (se para si esta corriendo) y para ver si hay errores con las herramientas de desarrollo (Console) nos podemos ver cuenta su algo pasa mal.

Si todo sale bien se muestra la pagina de incio de `Header.js` de la carpeta `Header.js`

### 9. Conectar las rutas con los templates
Dentro de la carpeta de `src/utils` se crea el archivo `getHash.js` para manejar la logica para poder navegar dentro de la aplicación.

El hash es el contenido de una url que parte desde el signo de numero(#). Ej:  
Código :
```
Url: http://www.example.com/index.html#algo-aqui
Hash: #algo-aqui
```

La forma más común de utilizarse y que quizás mucho ya conocen es la de hacer un scroll en la pantalla a la etiqueta HTML con esa **ID asignada**.

Si en la url el hash indica, por ejemplo… **#4** _http://www.dominio.com/pagina.html_`#4`; el navegador desplazará la pantalla hasta el elemento qué posea ese **ID**. Aquí tienen un ejemplo para que quede claro.

Hash con javascript:  
La forma de obtener el hash con javascript es la siguiente:  
Código:  
`window.location.hash;`  Sería práctico almacenarlo en una variable si lo vas a utilizar.
Código:  `var jash = window.location.hash;`

```javascript
const getHash = () =>
  location.hash.slice(1).toLocaleLowerCase().split('/')[1] || '/';

export default getHash;
```
Y el archivo `resolveRoutes.js` para "resolver las rutas" y saber a que template se va a mandar el "hash"
```javascript
const resolveRoutes = (route) => {
  if (route.length <= 3) {
    let validRoute = route === '/' ? route : '/:id';
    return validRoute;
  }
  return route;
  // return `/${route}`;
};

export default resolveRoutes;
```

Por ultimo en el carchivo `index.js` en la carpeta `src/routes`  se importan las funciones.
```javascript
import getHash from '../utils/getHash';
import resolveRoutes from '../utils/resolveRoutes';
```

### 10. Implementar y probar las conexiones

En el archivo `index.js` de la carpeta `/src/routes/` se añaden las siguientes lineas para mandar a llamar el _hash_ y resolver la ruta con _resolveRoutes_ y después renderisar con `content.innerHTML = await render();`
```javascript
    header.innerHTML = await Header();
    // 
    let hash = getHash();
    let route = await resolveRoutes(hash);
    let render = routes[route] ? routes[route] : Error404;
    content.innerHTML = await render();
    // 
};

export default router;
```
En el archivo `index.js` de la carpeta `/src/` se añade la linea para _ESCUCHAR LAS RUTAS A LAS CUALES EL USUARIO SE ESTA MOBIENDO_
```javascript
window.addEventListener('hashchange', router); // ESCUCHAR LAS RUTAS A LAS CUALES EL USUARIO SE ESTA MOBIENDO
```
Ejecutar `npm run build` para compilar el proyecto con webpack y ver que todo este correcto y en la página se mostrara algo parecido

![Ejemplo de OK](img/10_implementar_y_probar_las_conexiones_01.png)

## 4. Fetch Data
### 11. Obtener personajes con la función de llamado a la API
API de **Rick and Morthy** :link: [THE RICK AND MORTY API HEY, DID YOU EVER WANT TO HOLD A TERRY FOLD? I GOT ONE RIGHT HERE, GRAB MY TERRY FLAP](https://rickandmortyapi.com/)

Del archivo `getData.js` en la de la carpeta `/src/utils/` se crea la logica para traer del API los datos de manera _ASINCRONA_; para esto se tiene que leer la documentación del API

```javascript
// getData.js
const API = 'https://rickandmortyapi.com/api/character/';

const getData = async (id) => {
    const apiURl = id ? `${API}${id}` : API;
    try {
        const response = await fetch(apiURl);
        const data = await response.json();
        return data;
    } catch (error) {
        console.log('Fetch Error', error);
    };
};
export default getData;
```
Del archivo `Home.js` en la de la carpeta `src/pages/` se crea la logica para cuando se carga la pagina por primera vez en el _Home_
```javascript
// Home.js
import getData from '../utils/getData.js';

const Home = async () => {
    const characters = await getData();
    const view = `
        <div class="Characters">
            ${characters.results.map(character => `
            <article class="Character-item">
                <a href="#/${character.id}/">
                    <img src="${character.image}" alt="${character.name}">
                    <h2>${character.Name}</h2>
                </a>
            </article>
            `).join('')}
        </div>
    `;
    return view;
};
export default Home;
```

### 12. Conectar la función con la descripción de personajes
Se modifica el archivo `Character.js` que esta en la carpeta `/src/pages/` para que se despliegue el caracter al cual el usuario selecciono con las funciones de `getHash.js` y `getData.js`

```javascript
// Character.js
import getHash from '../utils/getHash';
import getData from '../utils/getData';

const Character = async () => {
    const id = getHash();
    const character = await getData(id);
    const view = `
        <div class="Characters-inner">
            <article class="Characters-card">
                <img src="${character.image}" alt="${character.name}">
                <h2>Name</h2>
            </article>
            <article class="Characters-card">
                <h3>Episodes: <span>${character.episode.length}</span></h3>
                <h3>Status: <span>${character.status}</span></h3>
                <h3>Species: <span>${character.species}</span></h3>
                <h3>Gender: <span>${character.gender}</span></h3>
                <h3>Origin: <span>${character.origin.name}</span></h3>
                <h3>Last Location: ${character.location.name}</h3>
            </article>
        </div>
    `;
    return view;
};
export default Character;
```

## 5. Deploy
### 13. Configurar CSS para administrar elementos visuales
:octocat: [Gist estilos para este proyecto](https://gist.github.com/gndx/cf251e88979581d6228028710bbff87c)

Los cuales se colocan en el archivo `styles.css` de la carpeta `styles`

Se tiene que instalar un complemento de Webpack para com copiar los estilos al compilado que se esta generando. 
```bash
$ npm install copy-webpack-plugin --save-dev
```
En archivo `webpack.config.js` se añade la siguiente linea
```javascript
const path = require('path'); // NOS PERMITE ACCEDER A DONDE ESTÁMOS EN LAS CARPETAS. YA SEA EN LOCAL O EN LA NUBE.
const HtmlWebpackPlugin = require('html-webpack-plugin'); // ARCHIVO NECESARIO PARA TRABAJAR CON HTML.

// ESTA LINEA PARA IMPORTAR EL COMPLEMENTO DE WEBPACK
const CopyWebpackPlugin = require('copy-webpack-plugin') // COMPLEMENTO DE WEBPACK PARA COM COPIAR LOS ESTILOS AL COMPILADO QUE SE ESTA GENERANDO
```

En el archivo `index.html` de la carpeta `public` se añade el link para la hoja de estilo.
```html
<link type="text/css" href="styles.css" rel="stylesheet">
```
Para compilar se tiene que correr el comando `npm run build` y revisar que todo salga bien para que se muestren los estilos añadidos cuando se corre el proyecto con `npm run start`

### 14. Github Pages
+ :link: [Travis CI - Test and Deploy Your Code with Confidence](https://travis-ci.org/)
    * Herramienta genera (flujos de trabajo) un script que esta conectado a nuestro repositorio en la rama master, y cuando detecta un cambio publica los cambios
+ :link: [Travis CI User Documentation Travis CI User Documentation](https://docs.travis-ci.com/)
    * 
+ :link: [https://yarnpkg.com/](Home | Yarn - Package Manager)
    * 
+ :octocat: [GitHub Pages](https://pages.github.com/)

Se tiene que generar un "_token_" desde Github para que funcione con "_Travis_" el deploy.

Se tiene que configurar "_Travis_" para que tome en cuenta el repositorio de Github :link: [Curso de Travis CI](https://platzi.com/cursos/travis/)

Se tiene que crear un archivo en la raiz del proyecto con el nombre de `.travis.yml` (tiene que estar con punto)
```yml
language: node_js
cache:
  directories:
    - ~/.npm
node_js:
  - '12'
git:
  depth: 3
script:
  - yarn build
deploy:
  provider: pages
  edge: true,
  skip-cleanup : true
  keep-history: true
  github-token: $GITHUB_TOKEN
  local-dir: dist/
  target-brach: gh-pages
  commit_message: "Deploy Release"
  on:
    branch: master
```

### 15. Crear el script para enviar a producción


### 16. Repaso, recomendaciones y tips para seguir aprendiendo







































































