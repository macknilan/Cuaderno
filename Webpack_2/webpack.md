

# C. Webpack

1. Introducción a Webpack
## ¿Qué es Webpack?
:link:[Webpack](https://webpack.js.org/)
Module bundlers son herramientas de frontend que nos permiten usar archivos con módulos JavaScript, 
entre otras características y convertiros a un JavaScript el cual el navegador pueda entender

Webpack es una herramienta que nos permite preparar nuestro código para llevarlo a producción (module bundler)

+ Webpack nos permite trabajar con
    - HTML
    - CSS
    - JavaScript
    - Archivos estáticos
    - Imágenes
    - Fuentes
Tambien nos permite tener un modo en desarrollo para nuestros proyectos para hacer pruebas
+ Nacio en el 2012, desde ese entonces varias empresas lo usan como ser
    - Twitter
    - Instagram
    - PayPal
También nos permite
    - Gestionar dependencias
    - Ejecutar tareas
    - Conversión de archivos
    - Nos permite trabajar en módulos
Permitiéndonos tener un código separado en desarrollo, pero en producción en una fuente
+ Webpack permite tener módulos de JS en formato
    - AMD
    - Common JS
    - ES15
_RESUMEN_: Webpack es un module _bundler_ que nos permite trabajar con una variedad de tecnologías web empezando
desde HTML y terminando con JS. Además de tener soporte para archivos estáticos

## Conceptos básicos
:link: [Concepts](https://webpack.js.org/concepts/)
**Webpack** es un paquete de módulos estáticos para aplicaciones de JS modernas

**Loader** _Te permite hacer un bundle de cualquier recurso estático más allá de JavaScript_

**Plugins** _Extienden recursos para añadir configuraciones y particularidades de recursos externos_

+ Webpack construye un gráfico de dependencias que mapea cada módulo para con verlo en uno o más módulos
+ Desde webpack 4 ya no dependemos de tener un archivo de configuración, pero si debemos tener un punto de entrada
+ Tambien tendremos que tener un punto de salida
    - En este punto se creará nuestro proyecto una vez esté preparado
    - Normalmente es la carpeta dist ⇒ Distribution
+ Tambien contamos con diferentes modos
    - Modo de desarrollo
    - Modo de producción
    - Modos de performance
        + Donde tu añades
            - Configuraciones de minificación
            - Donde se va enviar
            - Carpeta de destino
    + Modos de desarrollo local
        - Crear puertos específicos para tu proyecto
        - Ver cambios en tiempo real
+ _Dispone de loader y plugins_ permitiéndonos preparar particularidades de nuestro proyecto


2. Proyecto inicial
## Tu primer build con Webpack
:file_folder: Folder `ejemplo_no_uno`   
Se crea la estructura   
```bash
.
├── package.json
└── src
    └── index.js
```
Se instala webpack para desarrollo
```bash
$ yarn add webpack webpack-cli -D
```
Y luego ejecutamos webpack  
`npx` lo que hace es ejecutar paquetes directamente de npm, este viene instalado de npm

```bash
$ npx webpack
```
Al hacer esto webpack creo una carpeta llamada `dist`, esto lo hace por defecto webpack sin preguntarnos.   
**Modo de desarrollo**
Por defecto webpack al compilar nuestro proyecto setea el modo **“production”** implícitamente pero podemos
definirle el modo explícitamente corriendo:
```bash
$ npx webpack --mode production
$ npx webpack --mode development
```
_La diferencia radica_ que el modo development deja el código mas legible para los desarrolladores pero con comentarios,
el modo production deja el código comprimido y mas limpio para usarse.



## Instalación de Webpack y construcción del proyecto
:file_folder: Folder del proyecto de ejemplo `js-porfolio`
```bash
# gndx/js-portfolio
$ git clone https://github.com/gndx/js-portfolio.git
```
Agregar
```bash
$ yarn add webpack webpack-cli -D 
```
Entendimos las bases de webpack pero ahora vamos a crear un proyecto que nos va a permitir trabajar con todas las particularidades que nos brinda
webpack y preprarlo para mandarlo a produccion
+ CSS
+ Imágenes
+ fonts
+ optimización de código
El proyecto que realizaremos será un pequeño portafolio en el que podremos ver nuestra foto y nuestro nombre y redes sociales.

Lo clonamos de [aqui](https://github.com/gndx/js-portfolio.git) y hacemos uso de los assets que previamente nos prepararon

Luego de ello instalaremos webpack para configurar nuestro proyecto

utilizamos el comando para poder ver webpack en mod production

Correr
```bash
$ npx webpack --mode production
```

## Configuración de webpack.config.js
[Basic Setup](https://webpack.js.org/guides/getting-started/#basic-setup)

Se crea el archivo `webpack.config.js` en raiz y se escribe la siguiente configuración
```js
const path = require('path');

module.exports = {
  // Entry nos permite decir el punto de entrada de nuestra aplicación
  entry: './src/index.js',
  // Output nos permite decir hacia dónde va enviar lo que va a preparar webpacks
  output: {
    // path es donde estará la carpeta donde se guardará los archivos
    // Con path.resolve podemos decir dónde va estar la carpeta y la ubicación del mismo
    path: path.resolve(__dirname, 'dist'),
    // filename le pone el nombre al archivo final
    filename: 'main.js'
  },
  resolve: {
    // Aqui ponemos las extensiones que tendremos en nuestro proyecto para webpack los lea
    extensions: ['.js', '.jsx']
  },
}
```
En el archivo `package.json` se escribe en la seccion de `escript` 
```bash
"build": "webpack --mode production"
```
De esta forma forma en la linea de comando se ejecuta 
```bash
$ yarn run build
```


3. Loaders y Plugins en Webpack
## Babel Loader para JavaScript
Babel te ayuda a transpilar el código JavaScript, a un resultado el cual todos los navegadores lo puedan entender y ejecutar. Trae “extensiones” o plugins las cuales nos permiten tener características más allá del JavaScript común

+ Babel te permite hacer que tu código JavaScript sea compatible con todos los navegadores
+ Debes agregar a tu proyecto las siguientes dependencias
```bash
 $ yarn add babel-loader @babel/core @babel/preset-env @babel/plugin-transform-runtime -D
```
Crear el archivo de configuración de babel el cual tiene como nombre `.babelrc`
```bash
{
  "presets": [
    "@babel/preset-env"
  ],
  "plugins": [
    "@babel/plugin-transform-runtime"
  ]
}
```
En el archivo `webpack.config.js` agragar las siguientes lineas
```bash
module: {
        // REGLAS PARA TRABAJAR CON WEBPACK
        rules : [
            {
                test: /\.m?js$/, // LEE LOS ARCHIVOS CON EXTENSION .JS,
                exclude: /node_modules/, // IGNORA LOS MODULOS DE LA CARPETA
                use: {
                    loader: 'babel-loader'
                }
            }
        ]
    }
```

## HTML en Webpack
**HtmlWebpackPlugin**   
Es un plugin para inyectar javascript, css, favicons, y nos facilita la tarea de enlazar los bundles a nuestro template HTML.
```bash
yarn add html-webpack-plugin -D
```
En el archivo `webpack.config.js` se inserta el siguiente codigo para que funcione el plugin
```js
// ...
const HtmlWebpackPlugin = require('html-webpack-plugin')

// ...
plugins: [
        new HtmlWebpackPlugin({ // CONFIGURACIÓN DEL PLUGIN
            inject: true, // INYECTA EL BUNDLE AL TEMPLATE HTML
            template: './public/index.html', // LA RUTA AL TEMPLATE HTML
            filename: './index.html' // NOMBRE FINAL DEL ARCHIVO
        })
    ]
```
Se limina al linea del archivo `index.html` de la carpeta `public`
```js
<script type="module" src="../src//index.js"></script>
```
En el archivo `package.json` se añade una linea en script
```js
"dev": "webpack --mode development"
```

## Loaders para CSS y preprocesadores de CSS
Un **preprocesador CSS** es un programa que te permite generar CSS a partir de la syntax única del preprocesador. Existen varios preprocesadores
CSS de los cuales escoger, sin embargo, la mayoría de preprocesadores CSS añadirán algunas características que no existen en
CSS puro, como variable, mixins, selectores anidados, entre otros.
Estas características hacen la estructura de CSS más legible y fácil de mantener.

**Post procesadores** son herramientas que procesan el CSS y lo transforman en una nueva hoja de CSS que le permiten optimizar y
automatizar los estilos para los navegadores actuales.
```bash
$ yarn add mini-css-extract-plugin css-loader -D
```
+ `css-loader` ⇒ Loader para reconocer CSS
+ `mini-css-extract-plugin` ⇒ Extrae el CSS en archivos

Liminar la linea, del archivo `public/index.html`
```js
<link rel="stylesheet" href="../src/styles/main.css">
```

Importar los estilos en el archivo `/src/index.js` añadiendo al linea
```js
import './styles/main.css'
```

Agregar las configuraciones de webpack
```js
//...
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
module.exports = {
	...,
	module: {
    rules: [
      {
        test: /\.(css|styl)$/i,
        use: [
          MiniCssExtractPlugin.loader,
          "css-loader",
        ]
      }
    ]
  },
  plugins: [
		...
    new MiniCssExtractPlugin(),
  ]
}
```
Si deseamos posteriormente podemos agregar herramientas poderosas de CSS como ser:
+ pre procesadores
    + Sass
    + Less
    + Stylus
+ post procesadores
    + Post CSS

## Copia de archivos con Webpack
[CopyWebpackPlugin](https://webpack.js.org/plugins/copy-webpack-plugin/)   
+ Si tienes la necesidad de mover un archivo o directorio a tu proyecto final podemos usar un plugin llamado **“copy-webpack-plugin”**
+ Para instalarlo debemos ejecutar el comando
```bash
$ yarn add copy-webpack-plugin -D
```
En el archivo `webpack.config.js` insertar las siguientes lineas para que funcione
```js
// ...
const CopyPlugin = require('copy-webpack-plugin')
// ...
new CopyPlugin({ // CONFIGURACIÓN DEL COPY PLUGIN
    patterns: [
        {
            from: path.resolve(__dirname , "src" , 'assets/images'), // CARPETA A MOVER AL DIST
            to: "assets/images" // RUTA FINAL DEL DIST
        }
    ]
}),
```
Del archivo `src/templates/Template.js` editar 
```js
<img src="../src/assets/images/twitter.png" />
```
por
```js
<img src="assets/images/twitter.png" />
```
para que se llamen de manera correcta con el plugin.

## Loaders de imágenes
[Loading Images](https://webpack.js.org/guides/asset-management/#loading-images)

_Loader de imágenes_   
Este loader nos permite importar de forma dinámica en nuestros archivos JavaScript imágenes, el loader le genera un hash unico para cada imagen.
Algo parecido sucede con _ReactJS_ al importar imágenes

Se añaden estas lineas en el archivo `webpack.config.js` en la seccion de `rules`
```js
{
    test: /\.(png|svg|jpg|jpeg|gif)$/i,
    type: 'asset/resource',
},
```
Del archivo `src/templates/Template.js` editar para que los archivos de las imagenes se importen
```js
// ..
import github from '../assets/images/github.png';
import instagran from '../assets/images/instagram.png';
import twitter from '../assets/images/twitter.png';
```
y en donde se inserta la imagen, remplasarlo por la variable así
```js
<a href="https://twitter.com/gndx">
<img src="${github}" />
</a>
<a href="https://github.com/gndx">
<img src="${instagran}" />
</a>
<a href="https://instagram.com/gndx">
<img src="${twitter}" />
</a>
```

## Loaders de fuentes
+ [google-webfonts-helper](https://google-webfonts-helper.herokuapp.com/fonts/ubuntu?subsets=cyrillic,latin)
+ [Loading Fonts](https://webpack.js.org/guides/asset-management/#loading-fonts)

+ Cuando utilizamos fuentes externas una buena práctica es descargarlas a nuestro proyecto
  - Debido a que no hara un llamado a otros sitios
+ Por ello es importante usarlo dentro de webpack
+ Para esta tarea instalaras y usaras `file-loader` y `url-loader`

```js
yarn add url-loader file-loader -D
```
Se empieza eliminando la linea que llama a la fuente desde el CDN del archivo `src/styles/main.css`
```js
// SE ELIMINA
@import "https://fonts.googleapis.com/css?family=Ubuntu:300,400,500";
```
Se añade la configuración para que se importe la fuente en el mismo archivo
```css
@font-face {
	font-family: 'Ubuntu';
	src: url('../assets/fonts/ubuntu-regular.woff2') format('woff2'),
		url('../assets/fonts/ubuntu-regular.woff') format('woff');
	font-weight: 400;
	font-style: normal;
}
```
Modificar el archivo `webpack.config.js` para que se puedan importar/copiar los archivos de las fuentes a ocupar
```js
// PARA QUE LAS IMAGENES QUE SE IMPORTAN SE GUARDEN EN EL FORDER DE MANERA ADECUADA SE AGREGA ESTA LINEA EN output
assetModuleFilename: 'assets/images/[hash][ext][query]'
// EN EL APARTADO DE rules
{
  test: /\.(woff|woff2)$/, // REGLA PARA ARCHIVOS WOFF | WOFF2
  use: {
      loader: 'url-loader', // NOMBRE DEL LOADER
      options: {
          limit: false, // O LE PASAMOS UN NUMERO
          // Habilita o deshabilita la transformación de archivos en base64.
          mimetype: 'aplication/font-woff',
          // Especifica el tipo MIME con el que se alineará el archivo. 
          // Los MIME Types (Multipurpose Internet Mail Extensions)
          // son la manera standard de mandar contenido a través de la red.
          name: "[name].[ext]",
          // EL NOMBRE INICIAL DEL PROYECTO + SU EXTENSIÓN
          // PUEDES AGREGARLE [name]hola.[ext] y el output del archivo seria 
          // ubuntu-regularhola.woff
          outputPath: './assets/fonts/', 
          // EL DIRECTORIO DE SALIDA (SIN COMPLICACIONES)
          publicPath: './assets/fonts/',
          // EL DIRECTORIO PUBLICO (SIN COMPLICACIONES)
          esModule: false
      }
  }
}
```

## Optimización: hashes, compresión y minificación de archivos
+ [Optimization](https://webpack.js.org/configuration/optimization/)
+ [CompressionWebpackPlugin](https://webpack.js.org/plugins/compression-webpack-plugin/)
+ [HtmlMinimizerWebpackPlugin](https://webpack.js.org/plugins/html-minimizer-webpack-plugin/)
+ [CssMinimizerWebpackPlugin](https://webpack.js.org/plugins/css-minimizer-webpack-plugin/)
+ [TerserWebpackPlugin](https://webpack.js.org/plugins/terser-webpack-plugin/)

+ Los recursos que se guardan en memoria cache suceden cuando el navegador entra a un sitio por primera vez detecta los recursos y los guarda. Por ello la siguiente vez sera mucho más rápido porque estarán en memoria
  - La desventaja esta cuando sacamos una nueva versión, porque tendrán un mismo nombre evitando que se descargue los nuevos cambios, por lo tanto, el usuario no recibirá los nuevos cambios
  - Para que no haya conflictos con la cache una vez que tengamos nuestro proyecto en producción es importante darles un hash para cada nueva versión

**CssMinimizerPlugin**   
Es un plugin que nos permite minificar y optimizar los archivos CSS, por dentro del plugin utiliza
una herramienta llamada `cssnano`

```bash
$ yarn add css-minimizer-webpack-plugin -D
```
Se añade las lineas en el archivo `webpack.config.js` para poder optimizar
```js
// ...
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');
// SE AÑADE LA PARTE DE OPTIMIZACIÓN DEBAJO DE plugins
optimization: {
  minimize: true,
  minimizer: [
    new CssMinimizerPlugin(),
    new TerserPlugin(),
  ]
}
```
Para identificar cada `build` del proyecto se hace con `hash` que se implmenta de la siguiente manera

```js
// SE CAMBIA EN webpack.config.js
filename: "main.js",
// POR
filename: '[name].[contenthash].js',
// TAMBIEN SE CAMBIAI EL NOMNRE DE LAS FONTS DE ESTO
name: "[name].[ext]",
// A ESTO
name: "[name].[contenthash].[ext]",
// TAMBIEN SE AGRAGA EL HASS AL ARCHIVO MNIFICADO DEL CSS   
new MiniCssExtractPlugin(),
// A ESTO, SE MODIFICA PARA QUE SE GUARDE EN LA CARPETA assets
new MiniCssExtractPlugin({
      filename: 'assets/[name].[contenthash].css'
    }),
```


## Webpack Alias
_Alias_ nos permiten otorgar nombres paths específicos evitando los paths largos

_Aias_ **forma parte del objeto resolve** el cual nos permite configurar la forma en que webpack resolverá los módulos incorporados.
En nuestro camino, tenemos dos:

+ `resolve.alias` - para crear atajos que optimizan el tiempo de búsqueda e incorporación de módulos (commonJS o ES6)
+ `resolve.extensions` - para darle prioridad en resolución para con las extensiones donde si hay archivos nombrados igualmente, pero con diferentes extensiones, webpack resolverá conforme están listados.

En el archivo `webpack.config.js` en el modulo `resolve` se añade
```js
alias: {
  '@utils': path.resolve(__dirname, 'src/utils/'),
  '@templates': path.resolve(__dirname, 'src/templates/'),
  '@styles': path.resolve(__dirname, 'src/styles/'),
  '@images': path.resolve(__dirname, 'src/assets/images/'),
}
```
Y se tienen que hacer modificaciones a los archivos en los cuales se hacen los `imports`
`src/index.js`
```js
import Template from './templates/Template.js';
import './styles/main.css'
// A
import Template from '@templates/Template.js';
import '@styles/main.css'
```
`src/templates/Template.js`
```js
import getData from '../utils/getData.js';
import github from '../assets/images/github.png';
import instagran from '../assets/images/instagram.png';
import twitter from '../assets/images/twitter.png';
// A
import getData from '@utils/getData.js';
import github from '@images/github.png';
import instagran from '@images/instagram.png';
import twitter from '@images/twitter.png';
```


4. Deploy del proyecto
## Variables de entorno
+ [Environment Variables](https://webpack.js.org/guides/environment-variables/)
+ [EnvironmentPlugin](https://webpack.js.org/plugins/environment-plugin/)
+ [Random user API](https://randomuser.me/api)

+ Es importante considerar las variables de entorno va a ser un espacio seguro donde podemos guardar datos sensibles
  - Por ejemplo, subir llaves al repositorio no es buena idea cuando tienes un proyecto open source

```bash
$ yarn add dotenv-webpack -D
```
Crear dos archivos en raiz `.env` y `.env.example`   
En el archivo `.env` para este ejemplo se añade
```
API=https://randomuser.me/api/
```
En el archivo `.env.example` para este ejemplo se añade
```js
API=#
```
En el archivo `webpack.config.js` se añade
```js
const Dotenv = require('dotenv-webpack');
// Y EN LOS PLUGINS
plugins: [
  new Dotenv()
],
```
En el archivo `/src/utils/getData.js` se cambia
```js
const API = 'https://randomuser.me/api/';
// POR
const API = process.env.API;
```

## Webpack en modo desarrollo
Para crear un entorno de desarollo se crea el archivo `webpack.config.dev.js` en el cual se copia primero lo que esta en `webpack.config.js`
para después eliminar lo siguiente que no se ocupa en el modo de desarrollo

```js
// ...
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');
// ...
  optimization: {
    minimize: true,
    minimizer: [
      new CssMinimizerPlugin(),
      new TerserPlugin(),
    ]
  }
```
Se añade `webpack.config.dev.js` el modo de desarrollo despues de `entry`
```js
mode: 'development',
```
En el archivo `package.json` se añade la linea siguiente para poder ejecutar el webpack en modo development
```js
"dev": "webpack --config webpack.config.dev.js"
```

## Webpack en modo producción
+ [Mode](https://webpack.js.org/configuration/mode/)
+ [EnvironmentPlugin](https://webpack.js.org/plugins/environment-plugin/)


+ Actualmente tenemos el problema de tener varios archivos repetidos los cuales se fueron acumulando por compilaciones anteriores
+ Para ello puedes limpiar la carpeta cada vez que hacemos un build, usando clean-webpack-plugin
  - Cabe recalcar que esta característica es mucho más util para la configuración de producción

Se instala el plugin
```bash
$ yarn add clean-webpack-plugin -D
```

Se añade a `webpack.config.js` para que elimine los archivos que no son necesarios para producción como los _hashes_ anteriores. 
```js
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
// SE AÑADE EN LOS PLUGINS
plugins: [
...
  new CleanWebpackPlugin()
]
```
En el archivo `package.json` se cambia el _script build_ de esto 
```js
"build": "webpack --mode production",
// A 
"build": "webpack --mode production --config webpack.config.js",
```

## Webpack Watch
:link: [Watch and WatchOptions](https://webpack.js.org/configuration/watch/)

El modo watch hace que nuestro proyecto se compile de forma automática, que este al pendeiente los cambios realizados

Se dede de agregar a al configuración de `webpack.config.dev.js` en 
```js
module.exports = {
  //...
  watch: true,
};

```

## Deploy a Netlify
+ :link:[netlify](https://www.netlify.com/)
+ :octocat: [gitmogi](https://github.com/carloscuesta/gitmoji)
+ :octocat: [gitmoji-cli](https://github.com/carloscuesta/gitmoji-cli)

5. Herramientas de desarrollo complementarias
## Webpack Dev Server
+ :link: [DevServer](https://webpack.js.org/configuration/dev-server/)

**HTML5 History API** permite la manipulación de session history del navegador, es decir las páginas visitadas en el tab o el frame en la cual la página está cargada.

Para ver con webpack cambios en tiempo real en un navegador
```bash
$ yarn add webpack-dev-server -D
```
En el archivo `webpack.config.dev.js` se hace configuración de desarrollo debido a que esta característica solo nos ayudara a ver cambios al momento de desarrollar la aplicación.   
Despues de `plugins`

```js
devServer: {
    contentBase: path.join(__dirname, 'dist'),
    compress: true,
    historyApiFallback: true,
    port: 3006,
  },
```
Si en en la configuración de webpack se encuentra la configuración
```js
watch: true,
```
Se elimina para que no cause conflicto.   
En el archivo `package.json` se agrega la configuración de script
```
"start": "webpack serve --config webpack.config.dev.js"
```

## Webpack Bundle Analyzer
+ :link: [webpack-bundle-analyzer](https://www.npmjs.com/package/webpack-bundle-analyzer)
+ :link: [Analiza tus dependencias de forma gráfica con Webpack Bundle Analyzer](https://platzi.com/blog/analizar-dependencias-webpack-bundle-analyzer/)

Existe un plugin de Webpack que permite analizar qué dependencias componen nuestros bundles a detalle

`webpack-bundle-analyzer` despliega una gráfica interactiva con el resultado de nuestro bundle, qué dependencias contiene y cuánto pesan.

```bash
$ yarn add -D webpack-bundle-analyzer
```
En el archivo `webpack.config.dev.js` se instala el plugin
```js
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;
```
Y en la seccion de plugins se agrega
```js
new  BundleAnalyzerPlugin()
```
Ahora para ejecutar el plugin de nuestro bundle y analizar qué dependencias componen nuestros bundles a detalle
```bash
$ npx webpack --profile --json > stats.json
```
Para mostrar de forma grafica el bundle
```bash
$ npx webpack-bundle-analyzer stats.json
```

## Webpack DevTools
:link: [Devtool](https://webpack.js.org/configuration/devtool/)

**source map** _es un mapeo que se realiza entre el código original y el código transformado_, tanto para archivos JavaScript como para archivos CSS. De esta forma podremos debuggear tranquilamente nuestro código.

En la configuración de desarrollo `webpack.config.dev.js` despues de modo de desarrollo
```js
devtool: 'source-map',
```


6. Integración básica de React.js
## :rotating_light: Instalación y configuración de React :rotating_light:
Clonar el repo :octocat: [curso-webpack-react](https://github.com/platzi/curso-webpack-react)

:rotating_light: :file_folder: del proyecto `webpack-react-base` :eyes:

Isntalar react y react-dom
```bash
$ yarn add react react-dom
```

Se crea la estructura 
```bash
.
├── csr
│   ├── components
│   └── index.js
├── package.json
├── public
│   └── index.html
└── yarn.lock
```

## Configuración de Webpack 5 para React.js

```bash
$ yarn add @babel/core @babel/preset-env @babel/preset-react babel-loader -D
```
webpack
```bash
$ yarn add webpack webpack-cli webpack-dev-server -D
```
Se creal el archivo `.babelrc` en raiz con la configuración
```js
{
  "presets": [
    "@babel/preset-env",
    "@babel/preset-react"
  ],
}
```
Se crea el archivo `webpack.config.js`
```bash
const { resolve } = require('path');
const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
  resolve: {
    extensions: ['.js', '.jsx']
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        }
      }
    ]
  },
  devServer: {
    contentBase: path.join(__dirname, 'dist'),
    compress: true,
    port: 3006
  }
}
```

## Configuración de plugins y loaders para React
Para leer, modificar y cargar el archivo HTML que se encuentra en la carpeta `dist`
```bash
$ yarn add html-loader html-webpack-plugin -D
```

En el archivo `webpack.config.js` se añade el plugin
```js
//...
const HtmlWebpackPlugin = require('html-webpack-plugin');
//... EN EL MODULO SE AÑADE LA REGLA
{
  test: /\.html$/,
  use: [
    { loader: 'html-loader' }
  ]
}
// .. Y EN PLUGINS SE AÑADE
plugins: [
  new HtmlWebpackPlugin({
    template: './public/index.html',
    filename: './index.html'
  })
],
```
En el archivo `package.json` se agrega el script
```js
"start": "webpack serve",
"build": "webpack --mode production"
```

## Configuración de Webpack para CSS en React

Se instalan las dependencias y dependencias para sass
```bash
$ yarn add mini-css-extract-plugin css-loader style-loader sass sass-loader -D
```

En el archivo `webpack.config.js` se añaden los plugins
```js
//..
const MiniCssExtractPlugin = require('mini-css-extract-plugin')

//.. SE AÑADE EL MODULO LA REGLA PARA CSS SASS
{
    test: /\.s[ac]ss$/, // PARA ARCHIVOS SASS
    use: [
        'style-loader',
        'css-loader',
        'sass-loader'
    ]
}
// SE AÑADE EL PLUGIN QUE SE INSTANCIO AL INICIO
new MiniCssExtractPlugin({
    filename: '[name].css'
})
```
Se crea un archivo `styles/global.scss` en la cual se ponen los estilos de prueba
```css
$base-color: #c6538c;
$color: rgba(black, 0.88);

body {
  background-color: $base-color;
  color: $color;
}
```
Para despues añadirlos a la aplicación en `src/index,js`
```js
//..
import '../src/styles/global.scss';
```

## Optimización de Webpack para React

Se instalan las dependencias
```bash
$ yarn add css-minimizer-webpack-plugin terser-webpack-plugin clean-webpack-plugin -D
```

Se creal el `webpack.config.dev.js` para el modo en desarrollo y se hacen las modificaciones   
Se copia todo lo del otro archivo de webpack y se añade
```js
// resolve: {
//   extensions: ['.js', '.jsx']
// },
mode: 'development',
```
Se optimia el `webpack.config.js`
```js
// resolve: {
//   extensions: ['.js', '.jsx']
// },
mode: 'production',
// SE AÑADEN LOS PLUGINS INSTALADOS
const CssMinimizerWebpackPlugin = require('css-minimizer-webpack-plugin')
const TerserWebpackPlugin = require('terser-webpack-plugin')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')
//..
publicPath: "/",
//.. SE AÑADEN LOS ALIAS
// extensions: ['.js', '.jsx'],
alias: {
  '@components': path.resolve(__dirname, 'src/components/'),
  '@styles': path.resolve(__dirname, 'src/styles/')
}
// SE AÑADE AL PLUGIN EN plugins
new CleanWebpackPlugin(),
//.. SE AÑADE LA PARTE DE OPTIMIZACIÓN DESPUES DE LOS plugins
optimization: {
  minimize: true,
  minimizer: [
    new CssMinimizerPlugin(),
    new TerserPlugin(),
  ]
}
// SE ELIMINA
devServer: {
  contentBase: path.join(__dirname, 'dist'),
  compress: true,
  port: 3006
}
```
Se modifica el archivo `package.json` en lso scripts para que tomen en cuenta los archivos de modo prod y dev
```js
"start": "webpack serve --config webpack.config.dev.js",
"build": "webpack --config webpack.config.js"
```

## Deploy del proyecto con React.js


## EXTRA ESLINT con Webpack y React

Instalar de manera global Eslint
```bash
npm install -g eslint
```

Isntalar las dependencias
```
$ yarn add eslint babel-eslint eslint-config-airbnb eslint-plugin-import eslint-plugin-react eslint-plugin-jsx-a11y -D
```
Se creal el archivo `.eslintrc` con la configuración de :link: :octocat: [gist gndx/eslintrc](https://gist.github.com/gndx/17c1b5e6d443b9415679079ef9f58629)

## Prettier an opinionated code formatter. :link: [Prettier](https://prettier.io/)

+ :link: [Prettier npm](https://www.npmjs.com/package/prettier)
```bash
$ yarn add prettier eslint-plugin-prettier eslint-config-prettier -D
```

`.prettierrc`
```json
{
  "trailingComma": "es5",
  "semi": true,
  "singleQuote": true
}
```
Modificar el archivo `package.json` para poder ejecutar los comandos

`package.json`
```json
{
  "scripts": {
      "format": "prettier --write '{*.js,src/**/*.{js,jsx}}'",
      "lint": "eslint src/ --fix"
  },
}
```

## EXTRA Inatalar Husky 5

+ :link: [Husky home page](https://typicode.github.io/husky/#/)
+ :link: [Husky 5](https://blog.typicode.com/husky-5/)
+ :link: :octocat: [Husky 5](https://github.com/typicode/husky)
```bash
$ yarn add husky -D && npx husky init
```

Se crea la estructura de archivos
```bash
husky
├── _
│   └── husky.sh
└── pre-commit
```
En el  archivo `pre-commit` se pone la siguiente configuración
```bash
#!/bin/sh
. "$(dirname "$0")/_/husky.sh"

yarn run lint # ESTE ES EL SCRIPT QUE SE EJECUTA DESDE EL ARCHIVO package.json
```




























































































