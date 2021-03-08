

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
+ [google-webfonts-helper](http://google-webfonts-helper.herokuapp.com/fonts/ubuntu?subsets=cyrillic,latin)
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

```
```

```
```

## Webpack Alias


4. Deploy del proyecto
## Variables de entorno

## Webpack en modo desarrollo

## Webpack en modo producción

## Webpack Watch

## Deploy a Netlify

5. Herramientas de desarrollo complementarias
## Webpack Dev Server

## Webpack Bundle Analyzer

## Webpack DevTools


6. Integración básica de React.js
## Instalación y configuración de React

## Configuración de Webpack 5 para React.js

## Configuración de plugins y loaders para React

## Configuración de Webpack para CSS en React

## Optimización de Webpack para React

## Deploy del proyecto con React.js









































































































