


# Curso de PostCSS
NOTA

---
CSS Next Obsoleto  
Entonces que pasara?  
Existe alternativas?.  
Al cabo que ni queria  

Y muchas preguntas me surgieron pero la causa es muy interesante.

El motivo:  
    + El colaborador Principal ""MoOx"" nos explica porque se dejo el proyecto.
    + El colaborador principal practicamente se canso del proyecto y la visión de PostCSS.

Trato de dejar el proyecto a otros colaboradores, ha pedido ayuda por twitter pero no respondieron.

Pero un colaborador activo hizo un fork y comenzo [postcss-preset-env](https://preset-env.cssdb.org/) y posiblemente mejor que **cssnext**.

### Es en serio?
Si, puedes ver el post completo:  
:link: [Deprecating-cssnext](https://moox.io/blog/deprecating-cssnext/)

Cómo Migrar a `postcss-preset-env` ?  
1. Primero instalaremos el postcss-cli en el entorno de trabajo y no global.
```bash
  npm install postcss-cli --save-dev
```
2. Para ejecutar el comando en el entorno de trabajo ejecutamos:
```bash
npx postcss-cli --version
```
[Documentación PostCSS CLI](https://github.com/postcss/postcss-cli)

3. Instalar `postcss-preset-env`
```bash
npm install postcss-preset-env --save-dev
```
Por defecto tendremos algunos plugins:
    1. autoprefixer
    2. insertBefore / insertAfter
    3. browers

[ver mas…](https://github.com/csstools/postcss-preset-env#options)

4. Creamos el Archivo de Configuración
postcss.config.js y agregamos:
```bash
  module.exports = {
      plugins: [
          require("postcss-preset-env")({
            autoprefixer: {
              grid: true
            },
            browsers: [
              "last 1 version",
              "> 1%",
              "not dead"
            ],
            stage: 1,
            features: {
                'nesting-rules': true
            }
          })
      ]
  }
```
Esta configuración nos ayudara para continuar elcurso de Curso de PostCSS.

Puedes probar más: Opciones [postcss-preset-env](https://github.com/csstools/postcss-preset-env#options)

5. Ejecutamos:
```bash
npx postcss src/css/home.css -o dist/css/home.css -w 
```
Sobre los comandos:

+ La primera ruta indica el archivo base en PostCSS
+ `-o` indica la salida
+ La segunda ruta es donde se guardara el archivo transformado
+ `[ -w | --watch]` revisa los cambios.

---


## 1. Introducción

### 1. Bienvenida al Curso de PostCSS
PostCSS es una herramienta para manipular archivos CSS usando JavaScript.

### 2. Instalación y uso del cliente de PostCSS
Se puede  PostCSS diferentes formas, por ejemplo con webpack, gulp, etc. En esta clase vamos a instalar PostCSS usando el cliente de PostCSS.

Para instalar PostCSS primero debes tener instalado `node.js` en tu equipo porque vamos a estar trabajando con **NPM**.

:octocat: [PostCSS CLI](https://github.com/postcss/postcss-cli)
```bash
npm i -g|-D postcss-cli
# -g ES GLOBAL -D LOCAL EN LA CARPETA DONDE ESTA EL init DE NPM
```
:octocat: [platzi-video-postcss](https://github.com/LeonidasEsteban/platzi-video-postcss)

instalar PostCSS de varias maneras
1. npm i -D postcss-cli
2. npm i postcss-cli --save
2. npm i postcss-cli --save-dev

Se agrega entonces la dependencia. Podemos ver la versión en el package.json file.
```npm
    "dependencies": {
      "postcss-cli": "^6.1.2"
    }
```
Para invocar esta dependendencia local desde el terminal usamos npx postcss segido del comando que necesitemos:
```npm
npx postcss --version # IMPRIME VERSIÓN INSTALADA | ACTUALMENTE V6.1.2
#
npx postcss --help # IMPRIME COMANDOS
```
1. Para transformar un archivo en ser ejecuta el siguiente comando:
```npm
npx postcss src/css/home.css -o dist/css/home.css
```
1. La primera ruta indica el archivo base en PostCSS
2. `-o` indica la salida
3. La segunda ruta es donde se guardara el archivo transformado

2. Transformar un ves que se realice un cambio:
```npm
npx postcss src/css/home.css -o dist/css/home.css -w
```
`[ -w | --watch]` revisa los cambios

3. Uso de Plugins de PostCSS:
```npm
npx postcss src/css/home.css -o dist/css/home.css -w -u
```
`[ -u | --use]` uso de plugins de PostCSS

4. Cambiar la ruta en nuestro index.html al archivo transformado.
```html
<link rel="stylesheet" href="dist/css/home.css" />
```

## 3. Instalando y usando plugins en PostCSS
### 2. NextCSS - El futuro de CSS
+ :link:[PostCSS](https://postcss.org/)
+ :link: [postcss-cssnext features](https://cssnext.github.io/features/) -> :link: [postcss-preset-env ](http://preset-env.cssdb.org/)

PostCSS es una herramienta para transformar CSS con JS y todo lo que hará es transpilar un archivo legible para multiples browsers a partir de los parámetros de los plugins que instalemos.

Referencia plugins.  
:link: [PostCSS.parts](https://www.postcss.parts/)

Podemos también generar nuestros plugins personales.

:octocat: [Git Repo autoprefixer](https://github.com/postcss/autoprefixer)
El primero que usaremos es _autoprefixer_. Este es el plugin más popular y existe desde antes de postCSS.
Lo que este plugin hace es agregar prefijos como `-webkit-` o `-moz-` por ejemplo a las propiedades de CSS siempre que sea necesario y los navegadores no soporten esa propiedad.

Para instalar:
```bash
npm i --save autoprefixer
```
Se agrega entonces la dependencia. Podemos ver la versión en el package.json file.
```json
  "dependencies": {
    "autoprefixer": "^9.4.9",
    "
```
Para utilizarlo hay dos formas.
1. De forma básica o por defecto a través del terminal con el comando -u después de -w:
```bash
npx postcss src/css/home.css -o dist/css/home.css -w -u autoprefixer
```
2. De forma custom generando un archivo postcss.config.js en el root de nuestro proyecto.  
Carga por defecto
```javascript
    module.exports = {
        plugins: [
            require('autoprefixer')
        ]
    }
```
carga avanzada agregando prefijos para propiedades específicas de CSS:
```javascript
        module.exports = {
            plugins: [
                require('autoprefixer')({
                    grid: true
                })
            ]
        }
```


```bash
npx postcss src/css/home.css -o dist/css/home.css -w -u autoprefixer
```
1. `npx postcss`: linea de comando para llamar la funcionalidad de _postcss_
2. `src/css/home.css`: Archivo de entrada de _postcss_ (entry point)
3. `-o (–output)`: Flag usado para decirles _postcss_ a donde enviar el archivo transformado
4. `dist/css/home.css`: Archivo final que entrega _postcss_(output). si no están creadas las carpetas, las crea.
5. `-w (–watch)`: Flag usado para decirle a _postcss_ que se quede escuchando los cambios en los archivos
6. `-u(–use)`: Flag usado para decirle a _postcss_ que plugin vamos usar.
7. `autoprefixer`: Plugin mas usado en _postcss_. Usado para agregar prefijos para algunas reglas de css que soportan los navegadores antiguos pero con prefijos.


### 4. Instalando CSSNext
:octocat: (MoOx/postcss-cssnext)[https://github.com/MoOx/postcss-cssnext]

:octocat: `postcss-cssnext` has been deprecated in favor of `postcss-preset-env -> <a href="https://moox.io/blog/deprecating-cssnext/" target="_blank">Deprecating cssnext</a>

Para instalar CSSNext  
```bash
npm install -D postcss-preset-env
```
El creador de CSSNext ha anunciado que ya no va a seguir con el desarrollo del plugin y ahora se encuentra obsoleto.

:link: <a href="https://moox.io/blog/deprecating-cssnext/ target="_blank"">deprecating-cssnext</a>

Recomienda usar `postcss-preset-env`. en su lugar.

Entiendo que para usar este nuevo plugin la única diferencia para el resto del curso sería instalar el plugin y agregarlo al `postcss.config.js`?
```javascript
module.exports = {
  plugins: [
    require("postcss-preset-env.")
  ]
}
```

### 5. Los nuevos módulos de CSS
Vamos a entrar a mi parte favorita de este curso y la razón más importante para incluir PostCSS + CSSNext a tu Stack.

CSS ya no es un conjunto de propiedades para crear nuestros estilos, ya no es más un paquete que recibe un único nombre y se optó por algo mucho mejor para que estas nuevas características sean adoptadas por los navegadores más rápidamente, a estos los llamamos módulos.

Una ventaja de los módulos es que no necesariamente tienen que estar completos para ser implementados en el browser, pueden ir por niveles de la especificación y así garantizar constantes mejoras y nuevas características.

Te haré un resumen de los módulos a tratar en este curso y que gracias a CSSNext podemos hacerlo compatibles hoy mismo.

+ **CSS Custom Properties for Cascading Variables Module Level 1**
    Esta es una característica que nos permitirá traer a CSS algo que extraños mucho de los lenguaje de programación, las variables. Así podemos guardar por ejemplo el color hexadecimal preciso que necesitamos y darle un nombre que recordemos como –elVerdePerfecto.
<a href="https://www.w3.org/TR/css-variables" target="_blank">https://www.w3.org/TR/css-variables</a>

+ **Media Queries Level 4**
    Los media queries son nuestros mejores amigos para cambiar el CSS de algunos elementos dependiendo de las condiciones del navegador, es decir, en Responsive Design. Ahora podremos nombrar un media query como si fuera una variable para ser más fácil de reutilizar y rangos de media queries para una mejor sintaxis.
<a href="https://drafts.csswg.org/mediaqueries/" target="_blank">https://drafts.csswg.org/mediaqueries/</a>

+ **CSS Images Module Level 3**
    Con image-set() vamos a poder elegir una determinada image de background dependiendo de la densidad de pixel que tenga el monitor
<a href="https://drafts.csswg.org/css-images-3/#image-set-notation" target="_blank">https://drafts.csswg.org/css-images-3/#image-set-notation</a>

+ **CSS Color Module Level 4**
    Ya conocemos los hexadecimales, rgb() rgba() y ahora con la función color() vamos a poder seguir creando variaciones a la forma de asignar colores.
<a href="https://drafts.csswg.org/css-color/#modifying-colors" target="_blank">https://drafts.csswg.org/css-color/#modifying-colors</a>

+ **CSS Fonts Module Level 4**
    La forma de agregar tipografias también viene con mejoras y mi favorita se llama “System UI”. Con System UI podemos asignar un fallback que tomará la fuente predefinida de tu sistema operativo, en el caso de mac "San Francisco"
<a href="https://drafts.csswg.org/css-fonts-4/#valdef-font-family-system-ui" target="_blank">https://drafts.csswg.org/css-fonts-4/#valdef-font-family-system-ui</a>

+ **CSS Extensions - Custom Selectors**
    CSS quiere permitirte agrupar un selector o conjunto de selectores en algo más fácil de recordar como es el caso de las variables, estas se podrán anidar

+ **Selectors Level 4**
    Aprenderemos a usar psedu clases como :any-link() :not() :matches()
<a href="https://drafts.csswg.org/selectors-4/#matches" target="_blank">https://drafts.csswg.org/selectors-4/#matches</a>

+ **Nesting**
    Este es mi favorito, es una propuesta que nos permitirá usar mi cualidad favorita de los preprocesadores, evitar repetir un selector previamente escrito, es dificil de explicar así que dejaré un pequeño ejemplo

CSS actual
```css
.mi .selector .css {
    color: orange;
}
```
CSS Nesting
```css
.mi  {
    color: red;
    & .selector {
        color: blue;
        & .css {
            color: orange;
        }
    }
}
```
Mientras que con nuestros selectores tradicionales tenemos que escribir en profundidad tanto como sea necesario con nesting (_indentado en español_) vamos a poder escribir los selectores una sola vez e ir agregándoles estilos independientemente.
<a href="http://tabatkins.github.io/specs/css-nesting/ target="_blank"">http://tabatkins.github.io/specs/css-nesting/</a>

El conjunto de todo esto nos da un mejor CSS, uno que día a día se irá agregando en los navegadores y hará que no sea necesario hacerlo compatible con cssnext, cuando ese día llegue solo tienes que desactivarlo y como verás en las próximas clases podrás hacerlo independientemente por cada característica.

Ahora que sabes que es una buena idea escribir código que en un futuro será el estándar continúa con el curso que espero te deje impresionado clase a clase.

### 6. Variables

Las variables en CSS se pueden definir con 2 guiones medios `(–) --variable`: "contenido de la variable" y usarse con la palabra reservada `var`, de la siguiente manera propiedad: `var(--variable);`

Así se definen variables
```css
:root {
  /* Variables */
  --darkColor: #15192a;
  --lightColor: white;
  --warningColor: red;
}
```
Así se llaman las variables
```css
.btn.warning {
  background: var(--warningColor);
}
```
**Mixins**  
Para hacer un mixin en CSS necesitas crear una variable CSS con todas las propiedades de CSS que quieras agregar y plicarlo con @apply, de la siguiente forma:
```css
:root {
  /* Mixins */
  --button: {
    border: 1px solid var(--lightColor);
    border-radius: 5px;
    background: var(--darckColor);
    color: var(--lightColor);
    padding: .5em2em;
    text-transform: uppercase;
    cursor: pointer;
    font-size: 14px;
    border-bottom: 5px solid var(--lightColor)
  };
}
```
Aplicación de estilos
```css
.btn {
  @apply --button;
}
```

### 7. Operaciones matemáticas con CSS - CALC
Sirve para realizar operaciones matemáticas con medidas estáticas `px` sólo tenemos que hacer uso de la función `alc()`es importante que se ponga.

Además es posible anidar llamadas a calc() dentro de otras llamadas calc().
```css
calc(expresión)
```
- Las operaciones que permite calc son:
    + + Suma
    + - Resta
    + * Multiplicación. Al menos uno de los argumentos debe ser un `<número>`.
    + / División. El divisor debe ser un `<número>`.

### 8. Media Queries
+ `@custom-media`: Es la manera de personalizar o asignar un alias a los media query. Ejemplos de como asignarlo:
    - @custom-media —extra-small (width < 480px);
    - @custom-media --small screen and (width < 768px);
    - @custom-media —medium screen and (width >= 768px);
    - @custom-media —large screen and (width >= 1024px);
    - Al momento de usar el media query lo haríamos asi: @media (—extra-small){ propiedades css }

Para que @custom-media funcione debemos instalar postcss-custom-media. Para ello escribimos en la consola:
```bash
npm install postcss-custom-media --save-dev
```
Luego vamos a `postcss.config.js` y agregamos el plugin, y queda asi:
```css
plugins: [
        
        require('postcss-apply'),
        require('postcss-custom-media')({
            preserve: false,
        }),
        require('postcss-preset-env')({
            autoprefixer: {
                grid: true,
                flexbox: false,
            },
            preserve: false, 
            //Valor por defecto de "true". Se asemeja a customProperties en cssnext.
            //cambiar a false para notar el cambio.
            calc: false,
        })
        
    ]
```
`postcss-preset-env` permite el uso de custom-media sin embargo, es aceptado en el `stage 1` de este plugin. Por defecto, si no especificamos el stage, `postcss-preset-env` tendrá por defecto el `stage 2`

Para poder especificar el stage debemos tener el código del `postcss.config.js` de la siguiente manera:
```css
module.exports = {
    plugins: [
        require('postcss-preset-env')({
            stage: 0,
            autoprefixer: {
                grid: true,
            },
            preserve: false,
        }),
        require('postcss-apply'),
    ]
}
```

### 9. Imágenes retina con Post CSS - Image-set
Trabajando para Retina display. Si queremos poner multiples densidades, copiamos la misma sintaxis.

```css
background-image: image-set(url("/src/images/platzi-video.png") 1x, 
                            url("/src/images/platzi-video-2x.png") 2x,
                            url("/src/images/platzi-video-3x.png") 300dpi);
```


### 10. Colores
Instalar la dependencia para qeu se pueda ocupar
```css
npm install postcss-color-hwb
```
`postcss.config.js`
```css
module.exports = {
  plugins: [
    ...
    require('postcss-apply')
  ]
}
```

```css
background: color(black alpha(50%) contrast(50%)); 

hwb(hue [0-360], whiteness [0%-100%], blackness [0%-100%], opacidad);
/* background: hwb(hue, whiteness, blackness, opacity); */
background: hwb(240, 35%, 0%, 1); 

background: gray(50); /* 0-255 */
```

### 11. Fuentes
:link: [System Font Stack](https://css-tricks.com/snippets/css/system-font-stack/)

Toma la fuente por defecto del sistema operativo.
```css
font-family: system-ui;
```

### 12. Selectores personalizados
Para que te funcionen los selectores personalizados primer debes instalar la dependencia con la siguiente comando
```bash
npx install postcss-custom-selectors --save-dev
```
luego agregar al archivo de configuración `postcss.config.js` de la siguiente forma
```javascript
require('postcss-custom-selectors')
```
Visualización completa del archivo de configuración
```javascript
module.exports = {
    plugins:[
        require(‘autoprefixer’)({
        grid:true,
            }),
            require('postcss-preset-env')({
                calc:false
            }),
            require('postcss-apply'),
            require('postcss-custom-media')({
                preserve: false,
            }),
            require('postcss-custom-selectors')
    ]
}
```
La forma correcta es:
```css
@custom-selector :--checkeable .checkbox-label, .radio-label;
```


```css
@custom-selector :--checkable .checkbox-label, .radio-label;
@custom-selector :--highlight :hover, :active;

:--checkable {
    cursor: pointer;
    user-select: none;
    padding: 3px 7px;
}

:--checkable:--highlight {
    background: red;
    color: white;
}
```

### 13. Pseudo Clases
`:any-link:` Nos permite seleccionar cualquier enlace dentro de un selector.
```css
.myPlaylist :any-link:hover {
  transform: scale(1.1);
}
```
`:matches:` Nos permite seleccionar las coincidencias dentro de un selector.
```css
.myPlaylist-item:matches(:last-child, :nth-child(3), :first-child){
  background: color(red l(70%));
}
```
​`:not:` Nos permite seleccionar lo que no coincida con las propiedades que le pase.
```css
.myPlaylist-item:not(:last-child, :nth-child(3), :first-child){
  background: color(blue l(70%));
}
```

## 14. Indentado (nesting)
```css
.featuring {
  height: 100%;

  & a { 
    color: white;
    &:hover {
      text-decoration: underline;
    }
  }

  @nest .myPlaylist & {
    border: 5px dashed pink;
  }

  @media (width < 768px) {
    height: 150px;
  }
}
```
Se transforma en esto:
```css
.featuring {
  height: 100%;
}

.featuring a {
  color: white;
}

.featuring a:hover {
  text-decoration: underline;
}

.myPlaylist .myPlaylist-item
  border: 5px dashed pink;
}

@media screen and (max-width: 767px) {
  .featuring {
    height: 150px;
  }
```
Para los que usen `postcss-preset-env` el _postcss_ no les va a transpilar el nesting a su `home.css` para produccion, para solucionarlo en los plugins agregan un stage:
```css
require('postcss-preset-env')({
  preserve: false,
  stage: 1,  // Linea Agregada
}),
```

## 3. Plugins de PostCSS
### 15. Modulariza tu código con postcss-Imports

### 16. Auto font-face con FontMagician

### 17. Validar CSS con Stylelint

### 18. Agrupar Media Queries con mqpacker

### 19. Optimiza CSS para producción con CSSNano


























































