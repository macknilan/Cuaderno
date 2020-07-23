


## 1. Introducción a Responsive Design

### 1. Bienvenidos al curso de Responsive Design
### 2. Conceptos elementales de Responsive Design
+ :bird: https://twitter.com/lukew
+ :link: [Media Queries](https://mediaqueri.es/)

Para abordar el campo del Responsive Design es necesario que tengas claridad sobre algunos conceptos básicos.

Por este motivo, durante esta clase aprenderás qué es el Responsive Design, cuáles son los lenguajes de programación que lo hacen posible, qué medidas son necesarias aplicar para lograr que tus proyectos se adapten a pantallas de diversas medidas y condiciones, cuáles son los principios del Responsive Design (mostly fluid, colocación de columnas, layout shifter, tiny tweaks, off canvas).

Son todas las técnicas que usamos para adaatar nuestras aplicaciones web a la mayor cantidad de pantallas.
Existen diferentes patrones, tu sitio web puede incluir diferentes patrones.

+ MostlyFluid
+ Colocación de columnas (Column Wrap)
+ Layout Shifter
+ Tiny Tweks
+ OffCanvas

**viewport**: Es el área visible del navegador.
**portait-andascape**. Vertical, Horizontal. Celular.

+ **Viewport**: área visible del navegador
+ **Portrait**: vertical
+ **Landscape**: horizontal
+ **Mobile first**: empezar un websit desde la menor resolución soportada
+ **Deskto first**: empezar un websit desde la mayor resolución soportada
_¿Cúal es mejor?: Técnicamente Mobile First_

Ejemplos de webs  
- Mostly fluid:
    + [alistapart](https://alistapart.com/)
    + [simplebits](http://simplebits.com/)
- Colocación de columnas:
    + [modernizr](https://modernizr.com/)
- Layout shifter:
    + [anderssonwise](https://www.anderssonwise.com/)
    + [responsive web design](https://alistapart.com/d/responsive-web-design/ex/ex-site-FINAL.html)
- Tiny tweaks:
    + [gingerwhale](http://gingerwhale.com/)
    + [futurefriendlyweb](http://futurefriendlyweb.com/)
- Off canvas:
    + [Debugging Asynchronous JavaScript with Chrome DevTools](https://www.html5rocks.com/en/tutorials/developertools/async-call-stack/)

### 3. Proyecto del curso: Portafolio Responsive

    :octocat: [Repositorio del Curso de Responsive Design Platzi](https://github.com/LeonidasEsteban/responsive-design-portafolio)

### 4. Developer tools para Responsive Design

    Herramientas de google chrome dev tools para desarrollo

### 5. Meta viewport
`<meta>` viewport es una etiqueta de metadatos que permitirá configurar el website para que sea visible en dispositivos de menor tamaño. Permite conservar la legibilidad de tu página web al variar el escalado de tus contenidos.
```html
<meta name=“viewport” content=“width=device-width, initial-scale=1.0”>
```
Un elemento de vista <meta> le da al navegador instrucciones sobre cómo controlar las dimensiones y la escala de la página.

La parte `width=device-width` establece el ancho de la página para seguir el ancho de pantalla del dispositivo (que variará dependiendo del dispositivo).

- Parámetro 1.
    + **width=X** fijo con un tamaño en X pixeles predeterminado.
    + **width=device-width**: Se ajusta respecto al tamaño del dispositivo en que se carga

- Parámetro 2.
    + **initial-scale**: Valores de 0-1 equivalente a (0-100%)

### 6. Medidas relativas útiles en Responsive Design
Las medidas son maleables, en la medida en que dependen de su fuente de origen o medida madre. Entre ellas se encuentran el **porcentaje** (longitud referente al tamaño de los elementos padre), los **em** (unidad relativa al tamaño de fuente especificada más cercano), los **rem** (unidad relativa al tamaño de fuente especificada en el ancestro más lejano, como html o body) y tamaños del viewport **vw/vh** (longitud relativa porcentual con respecto al viewport).

+ **Porcentaje**: longitud referente al tamaño de los elementos padre
+ **em**: unidad relativa al tamaño de fuente especificada más cercano
+ **rem**: unidad relativa al tamaño de fuente especificada en el ancestro más lejano (html o body)
+ **vw/vh**: unidad relativa porcentual con respecto al viewport

### 7. Media queries
El media queries es un módulo de css que hace posible al responsive design, éste existe desde el 2010 y se encarga de adaptar la representación del contenido a características del dispositivo.
```css
max-width = hasta
min-width = desde
```
```css
@media media type and (condicion){
}
```
Se componen de un media type y una o más condiciones que harán referencia al width, dependiendo de si es _Mobile Firs_ o _Desktops first_ hay una forma de trabajar. La idea es generar un rango de tamaños ej:`(480px-780px)`

ejemplo
```css
@media screen type and (max-width: 768px) { }
```
todas las pantallas con un ancho inferior o igual a 768px cumplen con esta funcion
```css
@media screen type and (max-width: 768px) and (min-width: 480px) { }
```
todas las pantallas con un ancho de 480px hasta 768px cumplen con esta funcion

Mobile Firts
```css
@media screen type and (max-width: 320px) { }
@media screen type and (max-width: 480px) { }
@media screen type and (max-width: 768px) { }
@media screen type and (max-width: 1024px) { }
```
**usa min-width (min-width = desde)**

Desktop Firts
```css
@media screen type and (min-width: 1024px) { }
@media screen type and (min-width: 768px) { }
@media screen type and (min-width: 480px) { }
@media screen type and (min-width: 320px) { }
```
**usa max-width (max-width = hasta)**

### 8. Formas de incluir media queries
*Primera forma:*  
Añadir esta linea de código en el <head> del archivo HTML
```html
<head>
    <linkrel="stylesheet"href="css/media.css"media="screen and (max-width:768px)"/>
</head>
```
**Segunda forma**:
Agregar la expresión del Media Querie al final del codigo css:

```css
@media screen and (max-width: 768px) {
[aqui se anaden los estilos css]
}
```
EJEMPLO:
```css
@media screen and (max-width: 768px) { 
    body { 
        border: 10px solid green; 
        Background-color: red;
        } 
    .ventana {
        border: 10px solid green; 
        Dorder-radius: 25px;
    
        }
    }
```
Tercera forma:
Abriendo unas etiquetas <styles> </styles> al final del head y dentro de ellas invocar los media queries.
```css
 <styles> 
@media screenand (max-width: 768px) { 
    body { 
        border: 10px solid green; 
        Background-color: red;
        } 
    .ventana {
        border: 10px solid green; 
        Dorder-radius: 25px;
    
        }
    }
</styles>
```
Medidas standard para el diseño responsivo en formato Desktop:

```css
@media screen and (max-width: 1024px) { 
[Estilos css para dispositivos cuyo ancho maximo son 1024px]
}

@media screen and (max-width: 768px) { 
[Estilos css para dispositivos cuyo ancho maximo son 768px]

}
@media screen and (max-width: 480px) { 
[Estilos css para dispositivos cuyo ancho maximo son 480px]

}
@media screen and (max-width: 320px) { 
[Estilos css para dispositivos cuyo ancho maximo son 320px]
```

### 9. Repositorio del curso
    :octocat: [Repositorio del Curso de Responsive Design Platzi](https://github.com/LeonidasEsteban/responsive-design-portafolio)

## 2. Ajustando el proyecto con media queries
### 10. Diseño elástico con max-width y flex-wrap
La propiedad Flexible Box, o flexbox, de CSS3 es un modo de diseño que permite colocar los elementos de una página para que se comporten de forma predecible cuando el diseño de la página debe acomodarse a diferentes tamaños de pantalla y diferentes dispositivos. Para muchas aplicaciones, el modelo “caja flexible” produce una mejora sobre el modelo “bloque” porque no utiliza la propiedad float, ni hace que los márgenes del contenedor flexible interfieran con los márgenes de sus contenidos.

**Max-width**  
La propiedad CSS establece el ancho máximo de un elemento. Evita que el valor utilizado de la propiedad sea mayor que el valor especificado por .max-width widthmax-width.
```css
#child {
  background: gold;
  max-width: 150px;
}
```
**Flex-Wrap**
Por defecto, todos los elementos flexibles intentarán encajar en una línea. Puede cambiar eso y permitir que los elementos se ajusten según sea necesario con esta propiedad.
```css
.container {
  flex-direction: row | row-reverse | column | column-reverse;
}
```
+ `nowrap`: (Predeterminado): todos los elementos flexibles estarán en una línea.
+ `wrap`: Los elementos flexibles se ajustarán en varias líneas, de arriba a abajo.
+ `wrap-reverse`: Los elementos flexibles se ajustarán en varias líneas de abajo hacia arriba.

### 11. Ajustando el Header
+ :link:[Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox)
+ :link: [Aligning Items in a Flex Container](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Aligning_Items_in_a_Flex_Container)
+ [Mastering Wrapping of Flex Items](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Mastering_Wrapping_of_Flex_Items)

+ **flex-grow** que le dicen a los items que puedan “crecer” si es necesario. Como lo fijamos en 1 todos los hijos del contenedor se distribuyen equitativamente el espacio que sobra.
+ **flex-shirnk** es lo contrario, le dice a los items que se encojan si es necesario.
+ **flex-basis** le define al item un tamaño antes de que el espacio restante del contenedor sea distribuido.

En **flex**, el primer parámetro se refiere a **flex-grow** el segundo a **flex-shrink** y el tercero a **flex-basis**. Se vería así (tal como lo usamos en esta clase)
```css
/* Keyword values */
flex: auto;
flex: initial;
flex: none;

/* One value, unitless number: flex-grow */
flex: 2;

/* One value, width/height: flex-basis */
flex: 10em;
flex: 30%;
flex: min-content;

/* Two values: flex-grow | flex-basis */
flex: 1 30px;

/* Two values: flex-grow | flex-shrink */
flex: 2 2;

/* Three values: flex-grow | flex-shrink | flex-basis */
flex: 2 2 10%;

/* Global values */
flex: inherit;
flex: initial;
flex: unset;
```
```css
.item {
  flex: none | [ <'flex-grow'> <'flex-shrink'>? || <'flex-basis'> ]
}
```

### 12. Ajustando nuestro portafolio


### 13. Ajustando la sección de eventos


### 14. Ajustando la sección de contacto y footer


### 15. CSS positions
`static`: es la propiedad por defecto.

+ `relative`: el objeto se mueve en base al lugar donde se encuentra originalmente.
+ `absolute`: el objeto se ubica de manera absoluta con el elemento más cercano que tenga posición relativa o con el body.
+ `fixed`: El elemento se muestra de manera fija en el viewport.
+ `sticky`: El elemento se queda de manera fija una vez que aparece en pantalla.

Aplicando cualquiera de estos `positions`, _se activan las propiedades de_ `top`, `bottom`, `left`, `right` y `z-index`.
### 16. Ajustando nuestra sección principal
Un elemento posicionado es un elemento cuyo valor computado de position es relative, absolute, fixed, o sticky. (En otras palabras, cualquiera excepto static).

Un elemento posicionado relativamente es un elemento cuyo valor computado de position es relative. Las propiedades top y bottom especifican el desplazamiento vertical desde su posición original; las propiedades left y right especifican su desplazamiento horizontal.

Un elemento posicionado absolutamente es un elemento cuyo valor computado de position es absolute o fixed. Las propiedades top, right, bottom, y left especifican el desplazamiento desde los bordes del bloque contenedor del elemento. (El bloque contenedor es el ancestro más cercano posicionado). Si el elemento tiene márgenes, se agregarán al desplazamiento.

Un elemento posicionado fijamente es un elemento cuyo valor de position computado es sticky. Es tratado como un elemento posicionado relativamente hasta que su bloque contenedor cruza un límite establecido (como por ejemplo dando a top cualquier valor distinto de auto), dentro de su flujo principal (o el contenedor dentro del cual se mueve), punto al cual es tratado como “fijo” hasta que alcance el borde opuesto de su bloque contenedor.

Para una mejor visualización del texto sobre la imagen se puede usar:
```css
text-shadow: 1px2px2px#000;
```
O aplicarle un filtro a la imagen:
```css
filter: opacity(80%) blur(1px);
```

## 3. Añadiendo características dedicadas a pantallas pequeñas
### 17. Videos HTML5
Para agregarle una miniatura al vídeo puedes usar el atributo poster
ejemplo:
```html
<video class="HTML-video" src="https://www.youtube.com/watch?v=LoKvxCSZw5w" width=" " height=" " controls autoplay poster="YOUR-IMAGE.jpg">
</video>
```
Para sacar el vídeo desde Youtube.

Deben dar click derecho dentro del vídeo y la primera opción que les dará sera Bucle este copiara una etiqueta para HTML que luego podremos agregar en nuestro proyecto
```html
<iframewidth="853" height="480" src="https://www.youtube.com/embed/LoKvxCSZw5w" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```
_Este es la etiqueta para el vídeo del F8 del canal de Leonidas._

Insertar contenido multimedia  
**Video HTML**:  
```html
<videosrc="http://v2v.cc/~j/theora_testsuite/320x240.ogg"controls>
  Tu navegador no implementa el elemento <code>video</code>.
</video>
```
Este es un ejemplo para insertar audio en tu documento HTML
```html
<audiosrc="/test/audio.ogg">
<p>Tu navegador no implementa el elemento audio.</p>
</audio>
```
Este código de ejemplo usa los atributos del elemento:
```
<audiosrc="audio.ogg"controlsautoplayloop>
<p>Tu navegador no implementa el elemento audio</p>
</audio>
• **controls **: muestra los controles estándar de HTML5 para audio en una página web.
• **autoplay** : hace que el audio se reproduzca automáticamente.
• **loop** : hace que el audio se repita automáticamente.
```
El atributo **preload** es usado en el elemento audio para almacenar temporalmente (**buffering**) archivos de gran tamaño. Este puede tomar uno de 3 valores:
```html
<audiosrc="audio.mp3"preload="auto"controls></audio>
```
El atributo **preload** es usado en el elemento audio para almacenar temporalmente (**buffering**) archivos de gran tamaño. Este puede tomar uno de 3 valores:

+ "**none**" no almacena temporalmente el archivo
+ "**auto**" almacena temporalmente el archivo multimedia
+ "**metadata**" almacena temporalmente sólo los metadatos del archivo

Se pueden especificar múltiples fuentes de archivos usando el elemento <source> con el fin de proporcionar vídeo o audio codificados en formatos diferentes para diferentes navegadores. Por ejemplo:
```html
<video controls>
  <source src="foo.ogg"type="video/ogg">
  <source src="foo.mp4"type="video/mp4">
  Tu navegador no implementa el elemento <code>video</code>.
</video>
```
Esto reproduce el archivo _Ogg_ en navegadores que admiten el formato _Ogg_. Si el navegador no admite _Ogg_, el navegador usará el archivo _MPEG-4_.

### 18. Video insertado
*Para calcular la proporción de nuestro vídeo*
```
height * 100 / width
```
Sirve para obtener la relación entre el Alto (H) y Ancho (W) del vídeo expresado en porcentajes, es otra manera de expresar esa relación.
Tal vez te suene la “relación de aspecto” de las pantallas que son 4:3, 16:9, etc. pues si aplicas esa fórmula a estas, obtienes lo mismo pero en porcentaje, por ejemplo:

Una pantalla de “16:9”, aplicando la fórmula da como porcentaje:  
9 * 100 / 16 = 56,25%  

Si vídeo del mide _560x315_, por lo que se su relación es 315 / 100 * 560 = 56,25%, es decir, es vídeo está grabado en “16:9”.

Recordar que es **height * 100 / width**

Relación 16:9
9 * 100 / 16 = 56.25

Relación 4:3
3 * 100 / 4 = 75

### 19. Fuentes de iconos
:link: [IcoMoon](https://icomoon.io/)
```css
//cualquier elemento que tenga una clase que comience con 'icon-'

[class^="icon-"]       'icon-menu'

//cualquier clase que en algun momento de su nombre tenga 'icon-'

[class*=" icon-"]       'buton icon-menu'
```
Wildcard selectors `(*, ^ , $)`
Estos selectores seleccionan elementos con atributos de tipo similar.

(`*`) Se utiliza para seleccionar esos elementos cuyo valor de atributo CONTENGA el string indicado
```css
[class*="span"] {
    ...
}
```
Se seleccionaría el elemento **strong** porque, en este caso, su clase contiene la palabra **span**
```html
<divclass="show-grid">
    <strong class="span6">Blah blah</strong>
</div>
```
(`^`) Se utiliza para seleccionar los elementos cuyo valor de atributo EMPIEZA por esa cadena de texto
```css
[class^="something"] {
    ...
}
```
```html
<div class="something-else-class"></div>
```
(`$`) Selecciona los elementos cuyo valor de atributo TERMINA por esa cadena de texto
```css
[class$="something"] { 
    ...
}
```
```html
<div class="you-are-something"></div>
```

### 20. Añadiendo un menú de hamburguesa

:link:[Responsive Navigation Bar Tutorial | HTML CSS JAVASCRIPT](https://www.youtube.com/watch?v=gXkqy0b4M5g&list=LLCNxdMoS_Gj0RDDsbj0oXSg&index=53&t=0s)

### 21. Posicionando el menú



## 4. Responsive Design y Javascript
### 22. Añadiendo Javascript para detección de eventos
```javascript
burgerButton.addEventListener('click', function() {
    menu.classList.toggle('is-active')
})
```
Le agregamos la función en el mismo evento. 
Con `menu.classList.toggle` lo que quiere decir es: si tienes la clase, borrala, si no la tiene agregala.


### 23. Media queries con JavaScript
:link: [Window.matchMedia()](https://developer.mozilla.org/en-US/docs/Web/API/Window/matchMedia)

The `Window` interface's `matchMedia()` method returns a new `MediaQueryList` object representing the parsed results of the specified media query string. The returned `MediaQueryList` can then be used to determine if the Document matches the media query, or to monitor a `document` to detect when it matches or stops matching the media query.
```javascript
if(ipad.matches)
  burgerButton.addEventListener('click', hideShow);
```
**EJEMPLO DE CODIGO NO PROVADO**
```javascript
const ipad = window.matchMedia('screen and (max-width: 767px)');
const menu = document.querySelector('.menu');                                

const burgerButton = document.querySelector('#burger-menu');
    // ESCUCHEMOS LOS CAMBIOS DENTRO DE ESE MEDIA QUERIE
    // LLAMAMOS A OTRA FUNCION QUE SE ACTIVA O DESACTIVA CUANDO MATCHES 
    // CAMBIA SU ESTADO
    ipad.addListener(validation);

    if(ipad.matches) {
        burgerButton.addEventListener('click', hideShow);
        menu.addEventListener('click', hideMenu);
    }

    // ESTE EVENTO QUE LE PASAMOS VIENE SIENDO EL MEDIA QUERIE
    functionvalidation (event) {
      console.log(event.matches);

      // ESTE IF CONDICIONA SI VIENE EN TRUE O FALSE, PARA QUE EL EVENTO DE CLICK SE MANDE O NO SE MANDE
      if (event.matches) {
        burgerButton.addEventListener('click', hideShow);
        menu.addEventListener('click', hideMenu);
      }
      // CUANDO NO SEA NECESARIO QUITE ELA ESCUCHA DEL EVENTO PARA SER MAS OPTIMOS
      else {
        burgerButton.removeEventListener('click', hideShow);
        menu.removeEventListener('click', hideMenu);
      }
    }
      functionhideShow () {
      menu.classList.contains('is-active') ? menu.classList.remove('is-active') : menu.classList.add('is-active'); 
    } 
    
    functionhideMenu () {
      menu.classList.remove('is-active');
```

### 24. Creando un servidor de archivos estáticos con Node
### 25. Remote Debugging en iOS
### 26. Remote Debugging en Android y puliendo últimos detalles

































































