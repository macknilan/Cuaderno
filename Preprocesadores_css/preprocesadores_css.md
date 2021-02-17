

# Curso de Preprocesadores CSS

## 1. Introducción
### 1. Bienvenida al curso
Tanto HTML como CSS no han evolucionado de la mejor manera y aunque sirven para proyectos pequeños, suelen se difíciles de mantener en proyectos grandes.

Para solventar sus debilidades han surgido los preprocesadores como PUG para HTML o Stylus, Less y Sass para CSS.

### 2. Conceptos básicos de CSS
CSS significa **Cascading Style Sheets** o su traducción al español **Hojas de Estilo en Cascada**.

Asignar reglas CSS a un documento HTML se puede hacer de varias formas:

+ Colocando las reglas en un documento *.css y relacionarlo al HTML usando la etiqueta
+ Colocando en el atributo style de cada elemento HTML las reglas para cada etiqueta
+ Colocando los estilos dentro de una etiqueta style dentro del head del documento.
Como su nombre lo dice siempre lee en cascada de arriba hacia abajo sobrescribiendo valores excepto los dados por el atributo style.

**Un estilo CSS está formado por: selector, declaración, propiedad y valor.**

selector
 |  --propiedad
 |  |
h1{color:blue;}
            |
            valor

### 3. Selectores de CSS
selector
 |  
 |  --------->declaracion
 |  |       |
h1{color:blue;}

```css
/* RESETEO DE ESTILOS SELECTOR UNIVERSAL */
*{
    margin: 0;
    padding: 0;
}
```
```css
/* SELECTOR DE ETIQUETA */
p {
    color: blue;
}
h1, h2, h3, h4, h5 {
    font-family:Arial, Helvetica;
    color:black;
}
```
```html
<!-- SELECTOR ANIDADO -->
<dody>
    <span>Soy solor negro</span>
    <p><span>Soy rojo</span></p>
</dody>

```
```css
/* SELECTOR ANIDADO */
span {
    color: black;
}
p span {
    color: red;
}
```
```html
<!-- SELECTOR DE ID NO SE DUPLICA -->
<dody>
    <span>Soy solor negro</span>
    <p id="verde"><span>Soy rojo</span></p>
</dody>

```
```css
/* SELECTOR DE ID NO SE DUPLICA */
span {
    color: blue;
}
#verde {
    color: green;
}
```
```html
<!-- SELECTOR DE CLASES -->
<dody>
    <span>Soy solor negro</span>
    <p class="verde"><span>Soy rojo</span></p>
</dody>

```
```css
/* SELECTOR DE CLASES */
span {
    color: blue;
}
.verde {
    color: green;
}
```
```html
<!-- SELECTOR DE HIJOS -->
<dody>
    <span>Soy solor rojo</span>
    <p><div><span>Soy verde</span></div></p>
</dody>

```
```css
/* SELECTOR DE HIJOS */
p > span {
    color: red;
}
.span {
    color: green;
}
```
```html
<!-- SELECTOR ADYACENTE -->
<dody>
    <h2>Soy color negro</h2>
    <h2>Soy rojo</h2>
</dody>

```
```css
/* SELECTOR ADYACENTE */
h2 {
    color: black;
}
h2 + h2 {
    color: green;
}
```
```html
<!-- SELECTOR DE ATRIBUTOS -->
<dody>
    <input type="number">
    <input type="email">
</dody>

```
```css
/* SELECTOR DE ATRIBUTOS */
input[type='number'] {
    border: black;
}
input[type='email'] {
    border: red;
}
```



Los selectores nos sirven para seleccionar los diferentes elementos en una página web y aplicar estilos

Existen los siguientes tipos de selectores:

+ Selector universal * Sirve para agregar estilos a todos los elementos de la página. Normalmente se utiliza para hacer + “reset” de estilos.
+ Selector etiqueta. Aplica estilos a todos los elementos de ese tipo (p, h1, header etc.)
+ Selector id. Aplica estilos a un elemento único con ese Id, se recomienda hacer buen uso de este selector.
+ Selector clase. Aplica estilos a todos los elementos con esa clase (el que más vas a usar).
+ Selector anidado. Aplica estilos a un elementos descendientes de otros elementos (no necesario que sea hijo directo).
+ Selector hijo >. Aplica estilos a los elementos que sean hijos directos de otros.
+ Selector adyacente +. Aplica estilos al elemento adyacente.
+ Selector de atributo input[type=“number”]. Aplica estilos al elemento con el atributo especificado.

+ La prioridad de un selector se determina por la suma de su contenido:
    * ID = 100
    * Clase = 10
    * Etiqueta = 1
A mayor la suma, mayor prioridad.

`!important` es un valor especial tiene un valor de un millón, nunca lo uses a menos que sea tu única opción como cuando no tienes acceso al código fuente.

## 2. Evolución de las Tecnologías de Front-End
### 4. Introducción a los Preprocesadores
**Un preprocesador es** una herramienta que nos permite escribir pseudocódigo de forma modular, más fácil de rehusar, leer, y mantener. pseudocódigo que después será convertido a CSS o HTML estándar que el navegador entiende.

Gracias a los preprocesadores podemos extender las características de CSS y HTML al nivel de otros lenguajes de programación, permitiéndonos usar características como variables, funciones y mixins.

**Variable**: pedazo de momoria reservado para almacenar un valor, correspondiente a un tipo de dato. Es donde se guardan (y se recuperan) datos que se autilizan en un programa.

**Función**: Las funciones tieien la posibilidad de tener parametros o argumentos que son variables que modifican su comportamiento.

Mixins: Es una clase cuya finalidad es ofreser uan funcionalidad que pueda ser re-utilizada en otras clases pero que no está pensada para usarse de forma autónoma. 

+ Te sava tiempo y dinero al tener la opción de reusar código
+ Tener cun código más sencillo de mantener y editar
+ Modularizar nuestros proyectos de una forma lógica y sencilla

### 5. Metodologías para estructurar código
Las metodologías para estructurar código son sistemas preestablecidos, formales y bien documentados, que te ayudan a escribir y organizar código mantenible y escalable en sistemas grandes y complejos.

- Ventajas
    * Evita la redundancia al momento de crear componentes escalables y reutilizables.
    * Evitar el mal uso de propiedades como `!important`
    * Solucionar problemas de manejo en sistemas grandes y complejos

:link: [stateofcss.com](https://2019.stateofcss.com/technologies/pre-post-processors/)

+ Metodologías para estructurar tu HTML+CSS (con naming conventions):
    - BEM (Bloque, elemento, modificador)
    - BEMIT (BEM + Triángulo invertido)
    - ABEM (Atomic BEM)
    - ITCSS (CSS de triángulo invertido)
    - SMACSS
    - ACSS (Atomic CSS)
    - OOCSS (CSS orientado a objetos)
    - AMCSS (Atribute Model CSS)
    - SUIT CSS naming conventions

### 6. Introducción a BEM
:link:[BEM Offical Pagg](http://getbem.com/)

**BEM** es la metodología que vamos a usar a lo largo del curso. El objetivo de **BEM** es dividir lógicamente las piezas de las que se compone una web.

**BEM** establece que debemos usar clases para nuestro selectores, clases que se dividen en:

+ **Bloques**. Los bloques son nuestros contenedores más grandes que a su vez contienen elementos u otros bloques.
+ **Elementos**. Los elementos siempre forman parte de un bloque, normalmente son los botones, textos, imágenes etc.
+ **Modificadores**. Los modificadores se usan para establecer estilos diferentes a un mismo bloque o elemento.
```css
.bloque {}
.bloque__elemento {}
.bloque--modificador {}
```
```css
.galeria {}
.galeria__foto {}
.galeria__foto--circular {}
```
+ Ventajas
    * Menos repeticiones
    * Independencia absoluta
    * Mejoria en la herencia múltiple

### 7. Guías para creación y mantenimiento de código
La meta de tener una guía de código es hacer que luzca como si una sola persona lo haya escrito para que sea entendible por todo el equipo.

Para nuestro proyecto PlatziGames vamos a tener una guía en la que definimos:

+ Ser consistentes con la indentación.
+ Consistencia con espacios, corchetes, puntos y comas.
+ Consistencia de números, de selectores y divisiones.
+ Agrupaciones de propiedades.
+ Uso de ID’s y clases.

### 8. Instalación de herramientas de compilación
+ :octocat: [platzi-games-pug-publico](https://github.com/daywalkerhn/platzi-games-pug-publico)
+ :dog2: [Pug – robust, elegant, feature rich template engine for Node.js](https://pugjs.org/api/getting-started.html)
+ :link:[Prepros compiles your files, transpiles your JavaScript, reloads your browsers and makes it really easy to develop & test your websites so you can focus on making them perfect](https://prepros.io/)



## 3. Preprocesadores para HTML
### 9. Introducción a Pug
Instalar Prepos en debian, descargarlo de la pagina oficial.
```bash
$ sudo dpkg -i Prepros-7.2.15.deb
```
pug es
>The general rendering process of Pug is simple. pug.compile() will compile the Pug source code into a JavaScript function that takes a data object (called “locals”) as an argument. Call that resultant function with your data, and voilà!, it will return a string of HTML rendered with your data.

### 10. Sintaxis
Utilizar pug sin prepros y por terminal debes:

Instalarlo
```bash
npm i pug-cli -g
```
Compilar
```bash
pug -w --pretty landing.pug
# O TAMBIEN
pug nombreArchivo.pug --pretty
pug nombreArchivo.pug -w --pretty
pug nombreArchivo.pug -o rutaSalida/archivoSalida.html -w --pretty
```
pug
```pug
doctype html
html
    head
        meta(charset="UTF-8")
        link(rel="stylesheet", href="css/ejercicio-pug.css")
    body
        header
            h1 PlatziGames
            a.boton Registro
```
html
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="css/ejercicio-pug.css">
  </head>
  <body>
    <header>
      <h1>PlatziGames</h1><a class="boton">Registro</a>
    </header>
  </body>
</html>
```

### 11. Interpolación
Intermpolación es cómo anidar elementos dentro de otros en PUG y cómo trabajar con textos de múltiples lineas.
```pug
doctype html
html
    head
        meta(charset="UTF-8")
        link(rel="stylesheet", href="css/ejercicio-pug.css")
    body
        header
            h1 PlatziGames
            a.boton Registro
        section.intro
            //- INTERPOLACION SOLO TIENE UN HIJO
            .intro__imagen: img(src="images/imagen.png") 
            //- INTERPOLACION MÁS DE IM HIJO
            .intro__contenido
                h2 Titulo Principal
                p
                    | Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
                    | Amet voluptate nemo a quidem nostrum incidunt saepe nobis 
                    | vero eaque. Quam repellat maiores, hic quidem quasi veniam 
                    | animi soluta magni voluptates.
                    span Proin sit amet tellus nec nisl bibendum ornare nec at augue. Integer semper feugiat varius.
                a.boton Leer mas
```

### 12. Variables
Las variables no vienen de forma nativa en HTML pero con PUG podemos usarlas. En ellas almacenamos datos y los reutilizarlos en todo nuestro archivo HTML evitándonos tener que escribir lo mismo una y otra vez.

**NOTA: SE DECLARAN AL PRINCIPIO DEL HTML**

Cuando renderizamos las variables, tenemos que colocar un igual, el cual debe esta pegado al nombre de la etiqueta. 

Ejemplo:
```pug
//- SE DECLARA
-var titulo = "Titulo Principal"
```
donde se quiere poner el valor de la variale
```pug
//- SE USA
h2= titulo
//- TAMBIEN
h2 #{titulo}
```
Variables con arreglo
```pug
//- SE DECLARA
-var titulos = ["Titulo Principal", "Subtitulo 1", "Subtitulo 2", "Subtitulo 3"]
//- SE USA
h2 #{titulos[0]}
//- SE USA
h2 #{titulos[0][1]}
```

### 13. Condicionales y Loops
Un **condicional** nos permite evaluar cierta condición y bifurcar entre dos caminos dependiendo de si se cumple o no.

Un **loop** es un fragmento de código que va a ejecutar de forma repetitiva hasta que cumpla una condición.
1. Se declara la variable(al unicio del código HTML)
```
-var usuario = "David"
```
2. En el código **pug** donde se desea usar la condicional
```pug
if usuario
    a Hola #{usuario}
else
    a.boton Registro
```

### 14. Mixins
Su finalidad es ofrecer una funcionalidad que pueda ser reutilizada en otras clases pero que no está pensada para usarse de forma autónoma. Nos permite crear bloques reusables de código que cambian su resultado dependiendo del parámetro que enviemos.

Con los mixin logramos escribir menos código, produciendo un código más claro, más expresivo y sobre todo más fácil de mantener.

Primera forma de hacer in `mixin`

Se declara la el mixin
```pug
mixin caja
    .caja
        .caja__imagen: img(src="images/imagen.png")
        .caja__contenido
            h3 #{titulos[1]}
            p Lorem ipsum dolor sit amet
```
Para ocuparlo...
```pug
    main.contenido
        +caja
        +caja
        +caja
```
Cuando en el `mixin` se necesita poner variables se le pasan como parametros
```pug
-var titulo = "Titulo Principal"
-var titulos = ["Titulo Principal", "Subtitulo 1", "Subtitulo 2", "Subtitulo 3"]
-var usuario = "David"
mixin caja(imagen,titulo,contenido)
    .caja
        .caja__imagen: img(src="images/"+imagen)
        .caja__contenido
            h3=titulo
            p=contenido
```
Para ocuparlo...
```pug
main.contenido
    +caja('imagen.png',titulos[1],' Lorem ipsum dolor sit amet.')
    +caja('imagen.png',titulos[2],' Lorem ipsum dolor sit amet.')
    +caja('imagen.png',titulos[3],' Lorem ipsum dolor sit amet.')
```

### 15. Includes y Extends
**Pug funciona como un generador de plantillas**, dos de sus principales características para lograrlo son Includes y Extends.

+ Los **includes** sirven para incluir un archivo de extensión *.pug dentro de otro.
    + :link: [Includes](https://pugjs.org/language/includes.html)
+ Los **extends** te permiten adicionar bloques de código a una página. 
    + :link: [Template Inheritance](https://pugjs.org/language/inheritance.html)

Includes
```pug
//- LO QUE CONTIENEN EL INCLUDE
//- head.pug
head
    meta(charset="UTF-8")
    link(rel="stylesheet", href="css/ejercicio-pug.css")
```
```pug
//- COMO SE MANDA A LLAMAR AL INCLUDE  
include componentes/head.pug
```

Extend
Archivo `plantila.pug`
```pug
-var titulo = "Titulo Principal"
-var titulos = ["Titulo Principal", "Subtitulo 1", "Subtitulo 2", "Subtitulo 3"]
-var usuario = "David"
mixin caja(imagen,titulo,contenido)
    .caja
        .caja__imagen: img(src="images/"+imagen)
        .caja__contenido
            h3=titulo
            p=contenido
doctype html
html
    include head.pug
    body
        header
            h1 PlatziGames
            if usuario
                a Hola #{usuario}
            else
                a.boton Registro
        block contenidos
        //- TOLO QUE SIGUE ESTA AL MISMO NIVEL QUE header
```

En el archi que se le manda a llamar
```pug
extend componentes/plantilla.pug
block contenidos
//- CODIGO RESTANTE
```

### 16. Finalizando ejercicio de Landing Page

## 4. Less
### 16. Introducción a Less

Less es un preprocesador para CSS que nos permite trabajar hojas de estilo con funcionalidades de un lenguaje de programación.

+ :octocat: [platzi-games-less-publico](https://github.com/daywalkerhn/platzi-games-less-publico)
    * Clase No1. :link:[clase-1-nesting-imports](https://github.com/daywalkerhn/platzi-games-less-publico/tree/clase-1-nesting-imports)

:link:[Less Offical Page](http://lesscss.org/)

:link: [zeplin](https://zeplin.io/)  
Herramienta de diseño para frontend colaborativa

### 17. Anidamiento e imports
:link:[Features In-Depth](http://lesscss.org/features/#features-overview-feature)

Para hacer un "import" en les
```less
@import "globales.less";
@import "intros.less";
```
Ejemplo de anidamiento "_nesting_"en _less_
```less
.block {
  &__element { }
  &--modifier { }
}
```
:link:[Anidamiento de clases](https://stackoverflow.com/questions/5117133/less-css-nesting-classes)
The `&` character has the function of a `this` keyword, actually. It is possible to write:
```less
.class1 {
    &.class2 {}
}
```
and the CSS that will be generated will look like this:
```less
.class1.class2 {}
```
### 18. Variables
En las variables almacenamos datos que se puede reutilizar en todas nuestras hojas de estilos. Así evitamos tener que escribir lo mismo una y otra vez cuando se realiza algún cambio, ya que sólo vamos a modificar el valor de la variable y se aplicará a todos los lugares donde sea usada.

Comúnmente almacenamos en variables las guías de estilo de nuestro sitio, como pueden ser los colores y fuentes.

Ejemplo de declaración de varialbes y uso en el mismo archivo
```less
// globales.less
@color-primario: #333333;
@color-claro: #FFFFFF;
@color-secundario: #8841da;
@color-variacion: #012179;
@Fuente1:'Lato', sans-serif;
@Fuente2: 'Oswald', sans-serif;

*{
    box-sizing: border-box;
}
body {
    margin: 0;
    font-family: @Fuente1;
    color: @color-primario;
}

h1,h2,h3 {
    font-family: @Fuente2;
    text-transform: uppercase;
    margin: 0;
}
```
Uso de las variables en otro archivo.
```less
// articulos.less
.articulo--principal {
    max-width: 660px;
    margin: 0 auto;
    h2 {
        margin: 40px 0 40px 0;
        font-size: 50px;
        text-align: center;
    }
    h3 {
        color: @color-secundario;
    }
}
```
### 19. Funciones
La diferencia entre mixins y funciones es que las funciones por general hacen cálculos y regresan un resultado que es usado como valor de alguna propiedad.

**Las funciones en Less ya están prediseñadas.**
Ejemplo de una clase en less
```less
&-titulo {
    color: fade(@color-claro, 50%); 
}
```
Ejemplo de una clase en less
```less
body {
    margin: 0;
    font-family: @Fuente1;
    color: @color-oscuro;
    font-size: @fuente-base;
    //2.1 aca
    line-height: @fuente-base + 10%; // FUNCION MATEMATICA DE LA @fuente-base LE SUMA EL 10% EN line-height DEL EL VALOR DE @fuente-base
}
```
### 20. Mixins
Su finalidad es ofrecer una funcionalidad que pueda ser reutilizada en otras clases pero que no está pensada para usarse de forma autónoma. Nos permite crear bloques reusables de código que cambian su resultado dependiendo del parámetro que enviemos.

Con los mixins logramos escribir menos código, produciendo un código más claro, más expresivo y sobre todo más fácil de mantener.

Se declaran y se usan el mixin `.sombra-caja` y `.Oswald`

ejemplo
```less
// globales.less
@color-primario: #333333;
@color-claro: #FFFFFF;
@color-secundario: #8841da;
@color-variacion: #012179;
@Fuente1:'Lato', sans-serif;
@Fuente2: 'Oswald', sans-serif;
@fuente-base: 18px;

.sombra-caja {
    box-shadow: 0px 5px 15px 0px fade(@color-primario, 50%); 
}

.Oswald {
    font-family: @Fuente2;
    text-transform: uppercase;
    font-weight: 700;
}

*{
    box-sizing: border-box;
}
body {
    margin: 0;
    font-family: @Fuente1;
    color: @color-primario;
    line-height: @fuente-base + 10%;
}

h1,h2,h3 {
    margin: 0;
    .Oswald;
}
```
Se ocupan los mixin delcarados arriba en otro archivo 
```less
.contenedor--cajas {
    width: 1400px;
    margin: 0 auto;
    display: flex;
    justify-content: space-evenly;
}
.caja {
    max-width: 430px;
    .sombra-caja;  // MIXIN
    &__contenido {
        padding: 25px;
        background-color: @color-claro;
    }
    span {
        color: @color-secundario;
        .Oswald;
    }
    a {
        text-decoration: none;
        color: @color-variacion;
        .Oswald; // MIXIN
    }
}
```

### 21. Finalizando ejercicio de página de artículos
Carpeta "platzi-games-less-publico-clase.6-finalizando"

Se declaro otro `mixin`
```less
// TOMA EL VALOR POR PARAMETRO QUE LE PASEMOS POR @font-size QUE ES EL VALOR DE TAMAÑO DE LA FUENTE QUE SE DESEA
.fuente(@font-size){
    font-size: @font-size;
    line-height: @font-size + 10%;
}
```
## 5. Sass
### 22. Introducción a Sass
Sass (Syntactically Awesome StyleSheets) es una extensión de CSS que añade características muy potentes y elegantes a este lenguaje de estilos.

Sass es basado en Ruby a diferencia de Less y Stylus que se basan en Javascript.

:octocat:[Repositorio del las clases](https://github.com/daywalkerhn/platzi-games-sass-publico)

Sass nos permite usar variables , reglas anidadas , mixins y funciones.  
La razón de que en SASS usemos la extensión ‘.scss’ es porque esta nos permite usar una sintaxis muy parecida a css.  

La otra opción es usar SASS con la extensión `.sass` la única diferencia es que con esta extensión podremos omitir las llaves `{}` y los punto y coma `:` después de cada valor, esta sintaxis interpretará los atributos y valores por medio de la identación.

### 23. Variables
En las variables almacenamos datos que se puede reutilizar en todas nuestras hojas de estilos. Así evitamos tener que escribir lo mismo una y otra vez cuando se realiza algún cambio, ya que sólo vamos a modificar el valor de la variable y se aplicará a todos los lugares donde sea usada.

Comúnmente almacenamos en variables las guías de estilo de nuestro sitio, como pueden ser los colores y fuentes.

Ejemplo de declarar variables en sass
```sass
$Fuente1: 'Lato', sans-serif;
$Fuente2: 'Oswald', sans-serif;
$color-primario: #333333;
$color-claro: #FFFFFF;
$color-secundario: #8841DA;
$color-variacion: #3f579a;
```
Uso de variables
```sass
body {
    margin: 0;
    font-family: $Fuente1;
}
```

### 24. Imports y Extends
+ **Import** nos permite escribir código modular separando en diferentes archivos para después importarlos todos en uno solo y tener una base código mucho más ordenada.
+ **Extends** sirve para insertar los estilos de un selector en otro.

Ejemplo de Imports. Primero se debe de poner el archivo primcipal que lleva las variables y las utilizan los otros archivos.
```sass
@import "componentes/globales.scss";
@import "componentes/perfiles.scss";
@import "componentes/estadisticas.scss";
@import "componentes/ubicaciones.scss";
```

Ejemplo de Extends
```sass
.perfil {
    width: 50%;
    padding-top: 50px;
    color: $color-claro;
    background-color:$color-secundario;
    &__avatar {
        display: block;
        margin: 0 auto;
        border-radius: 50em;
    }
    &__nombre {
        text-transform: uppercase;
        text-align: center;
        font-size: 20px;
        font-family: $Fuente2;
    }
    &__titulo {
        text-transform: uppercase;
        text-align: center;
        font-weight: 700;
        font-size: 12px;
    }
    &__boton {
        display: block;
        width: 100px;
        height: 40px;
        margin: 15px auto;
        padding-top: 15px;
        border-radius: 20px;
        text-decoration: none;
        text-transform: uppercase;
        text-align: center;
        font-family: $Fuente2;
        color: $color-claro;
    }
}
.perfil__minibio {
    margin: 0 auto;
    padding-top: 20px;
    h2 {
        @extend .perfil__nombre;
    }
    h3 {
        @extend .perfil__titulo;
    }
}
```

### 25. Mixins
Su finalidad es ofrecer una funcionalidad que pueda ser reutilizada en otras clases pero que no está pensada para usarse de forma autónoma. Nos permite crear bloques reusables de código que cambian su resultado dependiendo del parámetro que enviemos.

Con los mixin logramos escribir menos código, produciendo un código más claro, más expresivo y sobre todo más fácil de mantener.

>Si quieres importar un archivo SCSS o Sass pero no quieres que se compile como archivo CSS, utiliza un guión bajo como primer carácter del nombre del archivo. De esta manera, Sass no generará un archivo CSS para esa hoja de estilos, pero podrás utilizarla importándola dentro de otra hoja de estilos. Este tipo de archivos que no se compilan se denominan "hojas de estilos parciales" o simplemente "parciales" (en inglés, "partials").

`_globales.scss`
```sass
$Fuente1: 'Lato', sans-serif;
$Fuente2: 'Oswald', sans-serif;
$color-primario: #333333;
$color-claro: #FFFFFF;
$color-secundario: #8841DA;
$color-variacion: #3f579a;

@mixin caja {
    border-radius: 20px;
    box-shadow: 0px 20px 33px 0px rgba(0,0,0,0.50);
    color: $color-primario;
    background-color: $color-claro;
}

* {
    box-sizing: border-box;
}
body {
    margin: 0;
    font-family: $Fuente1;
}
main {
    display: flex;
    width: 100%;
    height: 100vh;
}
```

Ejemplo de como se ocupa un mixin  `_estadistica.scss`
```sass
.estadistica--perfil {
    display: flex;
    width: 50%;
    height: 90px;
    padding-top: 15px;
    margin: 0 auto;
    justify-content: space-around;
    @include caja;

    h3 {
        font-weight: 600;
        font-size: 20px;
        text-align: center;
        text-transform: uppercase;
        font-family: $Fuente2;
    }
    span {
        font-size: 12px;
        text-align: center;
        text-transform: uppercase;
        font-family: $Fuente2;
    }
}
```

### 26. Funciones
La diferencia entre mixins y funciones es que las funciones por general hacen cálculos y regresan un resultado que es usado como valor de alguna propiedad.

Se declara las funciones en el archivo `_globales.scss` con `@function` y retorna el valor con `@return`
```sass
$Fuente1: 'Lato', sans-serif;
$Fuente2: 'Oswald', sans-serif;
$color-primario: #333333;
$color-claro: #FFFFFF;
$color-secundario: #8841DA;
$color-variacion: #3f579a;

@mixin caja {
    border-radius: 20px;
    box-shadow: 0px 20px 33px 0px rgba(0,0,0,0.50);
    color: $color-primario;
    background-color: $color-claro;
}
@function get-opacity($color,$nivel) {
    @return rgba($color,$nivel);
}
* {
    box-sizing: border-box;
}
body {
    margin: 0;
    font-family: $Fuente1;
}
main {
    display: flex;
    width: 100%;
    height: 100vh;
}
```

En el archivo `_ubicaciones.scss` se manda a llamar la funcion `get-opacity`
```sass
.ubicacion--perfil {
    width: 50%;
    height: 90px;
    margin: 30px auto 0 auto;
    padding: 20px 0 0 50px;
    @include caja;

    i {
        display: block;
        float: left;
        padding-right: 10px;
        font-size: 40px;
        color: $color-variacion;
    }
    h2 {
        text-transform: uppercase;
        font-weight: 600;
        font-size: 20px;
        font-family: $Fuente2;
    }
    h3 {
        text-transform: uppercase;
        font-size: 12px;
        font-family: $Fuente2;
        color: get-opacity($color-primario, .50);
    }
}
```

### 27. Condicionales y Loops
+ Un **condicional** nos permite evaluar cierta condición y bifurcar entre dos caminos dependiendo de si se cumple o no.
+ Un **loop** es un fragmento de código que va a ejecutar de forma repetitiva hasta que cumpla una condición.

Se crea la función con `@each` **NOTA**: Revisar como funciona más a detalle

Se crea el loop en `@mixin titulos`

`_globales.scss`
```sass
$Fuente1: 'Lato', sans-serif;
$Fuente2: 'Oswald', sans-serif;
$color-primario: #333333;
$color-claro: #FFFFFF;
$color-secundario: #8841DA;
$color-variacion: #3f579a;

@mixin caja {
    border-radius: 20px;
    box-shadow: 0px 20px 33px 0px rgba(0,0,0,0.50);
    color: $color-primario;
    background-color: $color-claro;
}
@mixin titulos($fuente){
    @if $fuente==$Fuente1 {
        font-family: $Fuente1;
    } @else {
        font-family: $Fuente2;
        text-transform: uppercase;
    }
}
@function get-opacity($color,$nivel) {
    @return rgba($color,$nivel);
}
@each $header, $size in (h1: 30px, h2: 25px, h3: 20px){
    #{$header} {
        font-size: $size;
        margin: 0;
    }
}
* {
    box-sizing: border-box;
}
body {
    margin: 0;
    @include titulos($Fuente1);
}
main {
    display: flex;
    width: 100%;
    height: 100vh;
}
```

### 28. Finalizando ejercicio de perfil de usuario


## 6. Stylus
### 28. Introducción a Stylus
+ :link:[Stylus Home Page](https://stylus-lang.com/)
+ :octocat: [platzi-games-stylus-publico](https://github.com/daywalkerhn/platzi-games-stylus-publico)

Es el preprocesador CSS más reciente de los tres. Fue creado por TJ Holowaychuk (ex programador de Node.js) y escrito en JADE y Node.js.

Stylus no ocupa corchetes ni tampoco punto y coma

### 29. Variables
En las variables almacenamos datos que se puede reutilizar en todas nuestras hojas de estilos. Así evitamos tener que escribir lo mismo una y otra vez cuando se realiza algún cambio, ya que sólo vamos a modificar el valor de la variable y se aplicará a todos los lugares donde sea usada.

Comúnmente almacenamos en variables las guías de estilo de nuestro sitio, como pueden ser los colores y fuentes.

Declaración de variables
```Stylus
Fuente1 = 'Lato', sans-serif
Fuente2 = 'Oswald', sans-serif
color-primario = #333333
color-secundario = #8841DA
color-claro = #FFFFFF
```
Uso de las variables
```Stylus
body
    margin: 0
    font-family: Fuente1
    color: color-primario
```

### 30. Mixins
Su finalidad es ofrecer una funcionalidad que pueda ser reutilizada en otras clases pero que no está pensada para usarse de forma autónoma. Nos permite crear bloques reusables de código que cambian su resultado dependiendo del parámetro que enviemos.

Con los mixins logramos escribir menos código, produciendo un código más claro, más expresivo y sobre todo más fácil de mantener.

Declaración de un mixin en el archivo `ejercicio-sylus.styl`
```Stylus
contenedor()
    display: flex
    width: 90%
    margin: 0 auto
    padding: 30px 0

caja-sombra()
    background-color: color-claro
    box-shadow: 0px 20px 33px 0px rgba(0,0,0,0.20)
```
Uso de un mixin en el mismo archivo `ejercicio-sylus.styl`

```Stylus
.encabezado--con-filtros
    contenedor()
    h2 
        margin-top: 10px
        text-transform: uppercase
        font-weight: 500
        font-size: 50px
        font-family: Fuente2
    .filtros
        width: 250px
        height: 75px
        padding: 20px
        margin-left: auto
        caja-sombra()
        span 
            text-transform: uppercase
            font-family: Fuente2
        a
            margin-left: 20px
            font-size: 25px
            color: color-primario
```

### 31. Funciones
La diferencia entre mixins y funciones es que las funciones por general hacen cálculos y regresan un resultado que es usado como valor de alguna propiedad.

:link: [Stylus BUILT-IN FUNCTIONS](https://stylus-lang.com/docs/bifs.html)

Es la forma de importar en stylus
```Stylus
@import "componentes/globales.styl"
@import "componentes/buscadores.styl"
@import "componentes/filtros.styl"
@import "componentes/cajas.styl"
@import "componentes/estadisticas.styl"
```

Declaración en el archivo `globales.styl` de una funcion **opacidad** en stylus con una funcion pre-diseñana en stylus
```Stylus
opacidad(color, cantidad)
    alpha(color,cantidad)
```
Uso de la funcion **opacidad** declarada en el archivo `estadisticas.styl`
```Stylus
.estadistica--articulos
    height: 70px
    padding: 20px
    border-top: 1px solid color-primario
    ul
        display: flex
        margin: 0
        padding: 0
        justify-content: space-evenly
        li  
            list-style: none
            color: opacidad(color-primario, .30)
        span 
            margin-left: 10px
```

### 32. Condicionales y Loops

Un **condicional** nos permite evaluar cierta condición y bifurcar entre dos caminos dependiendo de si se cumple o no.

Un **loop** es un fragmento de código que va a ejecutar de forma repetitiva hasta que cumpla una condición.

Declaración de un **loop** y **condicional** en el archivo `globales.sty`
```Stylus
<!-- DECLARACION DE UN for PARA LOS h1 h2 h3 DE TODA LA PAGINA SE LE RESTA EL %5 -->
for header in 3 2 1
    h{header}
        font-size: 35px - (5*header)
        margin: 0

<!-- SE DECLARA LA CONDICIONAL titulos POR PARAMETRO SE LE PASA EL VALOR DE FUENTE, SI ES Fuente1 SE QUEDA IGUAL Y SI ES Fuente2 SE CAMBIA A MAYUSCULAS TODO EL TEXTO -->
titulos(fuente)
    if fuente == Fuente1
        font-family: Fuente1
    else 
        font-family: Fuente2
        font-weight: 600
        text-transform: uppercase
```

## 7. Desarrollo del proyecto Platzi Games
### 33. Introducción al proyecto

### 34. Plantillas modulares con PUG: Header

### 35. Plantillas modulares con PUG: Footer

### 36. Grid System con Sass

### 37. Mixins para manejo de fuentes responsivas

### 38. Funciones para media queries

### 39. Finalizando el proyecto



































































































