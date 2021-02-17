

# Curso de Sass

## 1. Preprocesador Sass
### 1. Introducción a los cursos de preprocesadores
pass
### 2. Introducción al Curso de Sass
pass
### 3. Diferencias entre Sass, Stylus y Less
Aunque hay muchos preprocesadores, en este curso nos vamos a concentrar en **Sass**, **Stylus** y **Less**.

**Less**, por ejemplo, es un preprocesador muy simple.
**Sass**, por otro lado, es una herramienta muy interesante gracias a su comunidad.
Finalmente, **Stylus** tiene la ventaja de que es muy completo e incluso complejo.

Elegir cuál es el mejor procesador depende de lo que queremos lograr con el proyecto. Algunas de las razones están relacionadas con el equipo y las necesidades que tenemos con el proyecto.


### 4. Compilación de código en archivos CSS
Una de las primeras cosas que tenemos que aprender cuando estamos trabajando con Preprocesadores es la compilación de código que se compilará en archivos de CSS. En Mac utilizamos Codekit, y para Windows/Linux/Mac podemos usar Preposs.

    NOTA: Se tiene que separa el codigo de `sass` del codigo `css`, por que los archivos `css` son los que se suben a producción _NO LOS DE SASS_

## 2. Instalación
### 1. Estructura de CSS
La primera ventaja que se nos ocurre es que podemos organizar nuestro Sass. Lo clave es que podemos separar nuestro código en archivos. Ya no tenemos que revisar un archivo muy amplio, sino que podemos hacer modificaciones a un solo archivo, lo que nos hace el trabajo mucho más fácil.


## 3. Variables
### 5. Variables
Las variables son una forma de almacenar la información que se desea reutilizar a lo largo de la hoja de estilo.

Se puede almacenar cosas como colores, pilas de fuentes o cualquier valor de CSS que que se desea reutilizar. Sass usa el símbolo `$` para hacer que algo sea una variable.
```sass
$font-stack: Helvetica, sans-serif
$primary-color: #333

body {
  font: 100%$font-stack
  color: $primary-color
}
```
**BEM** — Block Element Modifier o Modificador de Bloques de Elementos

Como su nombre indica, **BEM** distingue claramente 3 conceptos: el _Bloque_, el _Elemento_ y el _Modificador_.

Escapar una variable

Para escapar una variable se usa el comodín **#**

Esto es necesario en casos como, por ejemplo, cuando la variable está rodeada por comillas y de no ponerse el escape la variable pasaría como una cadena de caracteres

```sass
$size: 10;

div {
  content: "#{$size}"
}
```

### 6. Reto

### 7. Solución al reto
Si quieres importar un archivo SCSS o Sass pero no quieres que se compile como archivo CSS, utiliza un guión bajo como primer carácter del nombre del archivo. De esta manera, Sass no generará un archivo CSS para esa hoja de estilos, pero podrás utilizarla importándola dentro de otra hoja de estilos. Este tipo de archivos que no se compilan se denominan "hojas de estilos parciales" o simplemente "parciales" (en inglés, "partials").

Ejemplo de extructura de archivos sass
`styles.sass`
```sass
// Librerias, settings y variables
@import'lib/_variables.sass'

// Elementos base
@import'_tablas.sass'
@import'base/_botones.sass'
@import'base/_tipografia.sass'

// Components
@import'components/_grids.sass'

// Esto va de último
@import'components/_utilities.sass'
```
`_variables.sass`
```sass
/*---------- $COLORS -----------*/
// Branding colors

$color-brand: #ea83ee
$color-secondary: rgb(219, 216, 121)

$color-black: rgb(0,0,0)
$color-darkblack: #4d4d4d
$color-grey: #bfbfbf
$color-white: rgb(255,255,255)

// Texturas
$color-alert: rgb(252,228,207)
$color-error: rgb(218,79,73)
$color-info: rgb(66,104,221)
$color-success: rgb(91,183,91)


// Tipografía
$basefont: 'Quicksand', sans-serif
$basefontsize: 16px

$buttoncolor: $color-white
$buttonbackgroundcolor: $color-brand
```
`_tablas.sass`
```sass
tabletr:hover
  background-color: $color-secondary
```
index.html
```sass
<!DOCTYPE html>
<htmllang="en">
<head>
  <metacharset="UTF-8">
  <metaname="viewport"content="width=device-width, initial-scale=1.0">
  <metahttp-equiv="X-UA-Compatible"content="ie=edge">
  <linkrel="stylesheet"href="css/styles.css">
  <title>SASS</title>
</head>
<body>
  <h1>Platzi Styguide</h1>
  <section>
    <h2>Botones</h2>
    <inputtype="submit">
  </section>
  <section>
    <h2>Tipografía</h2>
    <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Adipisci nam dolor in quidem! Consectetur hic quam, veritatis aut, expedita aliquid beatae asperiores voluptas nobis vitae doloremque, sunt laboriosam id quo?</p>
  </section>
</body>
</html>
```

## 4. Anidaciones
### 8. Anidaciones
El comodín `&` se usa para hacer referencia al padre

```sass
.btn {  
  font-size: 15pt;
  &__icon {
    font-size: .6em;
  }
  &.btn--info {
    background-color: $color-info;
  }
}
```

## 5. Mixins
### 9. Mixins
Lo que hacen los mixins nos ayudan a reciclar declaraciones para evitar mucho trabajo.

Los mixins nos ayudan a reciclar declaraciones para evitar mucho trabajo. Para esto vamos a usar @mixin.

Cuando se define un mixin, los argumentos se definen como una serie de variables separadas por comas, y todo ello encerrado entre paréntesis.
```sass
@mixin max-width($width) {
  max-width: $max-width
  margin-left: auto
  margin-right: auto
}
```
En este caso le estamos definiendo un valor por defecto. Si deseamos cambiar ese valor, cuando lo llamemos se lo podemos cambiar de esta forma:
```css
@include max-width(1200px); // SE LE PUEDE PASAR UN VALOR COMO PARAMETRO Y SE RECIBE EN LA VARIABLE
```
### 10. Continuando con Mixins

### 11. Uso de la directiva `content` (`block` en Stylus)
:link: [Content Blocks](https://sass-lang.com/documentation/at-rules/mixin#content-blocks)

Una de las características que tienen los mixins es la directiva content. Esta nos permite incluir un bloque de contenido dentro de un mixin.
SASS
```sass
SCSS SYNTAX
@mixin hover {
  &:not([disabled]):hover {
    @content;
  }
}
.button {
  border: 1px solid black;
  @include hover {
    border-width: 2px;
  }
}
```
GENERA EN CSS
```css

CSS OUTPUT
.button {
  border: 1px solid black;
}
.button:not([disabled]):hover {
  border-width: 2px;
}
```
SASS
```sass
@mixin apply-to-ie6-only {
  * html {
    @content
  }
}

@include apply-to-ie6-only {
  #logo {
    background-image: url(/logo.gif);
  }
}
```
GENERA EN CSS
```css
* html #logo {
  background-image: url(/logo.gif);
}
```

### 12. Extend
Permiten que una declaración herede estilos declarados por otra regla o placeholder. Los extend se declaran con el símbolo de porcentaje `%`.
```sass
%btn {
    color: red;
    width: 50px;
}

.btn-info {
    @extend %btn;
    background: blue;
}
```

## 6. Funciones
### 13. Funciones

### 14. Directiva

### 15. Ejemplos de funciones

### 16. Reto

### 17. Reto - Solución


## 7. Controles de Flujo
### 18. Listas y directiva each

### 19. Ciclos FOR/EACH

### 20. Condicionales






























































































