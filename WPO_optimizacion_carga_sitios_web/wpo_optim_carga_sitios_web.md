
# Curso de WPO: Optimización de Carga de Sitios Web

## 1. Google Page Speed Insights
### 1. Bienvenida al curso

En este curso vamos a trabajar sobre el portafolio creado en los cursos de Desarrollo Web y Responsive Design para que su optimización se encuentre arriba de 90/100.

### 2. Repositorio del curso
:octocat: <a href="https://github.com/LeonidasEsteban/curso-pagespeed-insights/commits/master" target="_blank">curso-pagespeed-insights</a>

### 3. Deploy del Portafolio a Github Pages

¿Como crear un GitHub Gages?

+ Crear un repositorio en GitHub
+ Subir la web estática al repositorio
+ Ir a **Settings / Options**
+ Buscar abajo el apartado **GitHub Pages**
+ En **Source**, elegir la rama donde se cargará la págian estatica (master branch)
+ Seguir el enlace para acceder a la web estática.

### 4. Google PageSpeed Insights

+ :link: [Mejora la velocidad de tus páginas web en todos los dispositivos](https://developers.google.com/speed/pagespeed/insights/?hl=es)
+ :link: [Get the web's modern capabilities on your own sites and apps with useful guidance and analysis from web.dev.](https://web.dev/)

_Google PageSpeed Insights_ es una excelente herramienta para medir el rendimiento de una página web, ya que no solo nos mide el rendimiento de la misma, sino que nos marca aquellos puntos críticos que nos está haciendo disminuir dicho rendimiento y nos ofrece sugerencias para mejorarlo.


### 5. Eliminando bloqueos de visualización, fuentes

La primera optimización que vamos a realizar a nuestro sitio tiene que ver con eliminar cualquier carga que afecte al renderizado de nuestro sitio. Específicamente tiene que encontrarse libre el Above the fold, la primera parte visible para el usuario sin necesidad de hacer scroll.

El _render blocking_ o el _bloqueo de visualización de Javascript_ Render se refiere a cargar (_loading_), esto quiere decir que si algún elemento es marcado como render-blocking, significa que impide que el contenido cargue tan rápido como podría o debería.

+ **Above the fold**
    + Es la parte visible de la pagina que se carga inicialmente, es decir, cuando entramos a la webpage.

+ **Bloqueo de visualización** 
    + Un bloqueo de visualización se puede dar cuando ponemos a cargar inicialmente en el _Above in the fold_ (pagina visible cargada inicialmente) un archivo relativamente pesado. Para ello, podemos mover aquellos archivos de carga hacia la etiqueta footer como sugerencia.

### 6. Comprimiendo Hojas de estilo
+ [CSS Compressor](https://csscompressor.com/)
+ [CSS Minifier](https://cssminifier.com/)

Una buena practica para optimizar la carga de nuestro sitio web es comprimir las hojas de estilos, de esta forma nos ahorramos bastantes recursos (y tiempo) de carga. Una pagina que nos ayuda con esto se llama CSS Compressor.

+ Otras maneras de las que puedes comprimir las hojas de estilos con:
    * pre-procesador
    * postCSS
    * webpack
    * websites

### 7. Critical CSS o Critical Path CSS
Para eliminar el bloqueo de la visualización solamente nos queda hacer Critical Path CSS.

Al momento de cargar un sitio este se encontrará sin estilos hasta el momento de cargar el CSS por completo generando que la visualización del sitio sea mala, para solucionar esto solamente debemos escribir el CSS necesario para el _Above the fold_ dentro de nuestro HTML. Haremos uso del sitio [Critical Path CSS Generator](https://jonassebastianohlsson.com/criticalpathcssgenerator/)

_Critical CSS_ es método para optimizar la velocidad de carga de las páginas web, en el cual lo que se hace es _dividir la carga del CSS en dos etapas_.

La primera sección de CSS a ser cargada corresponde a la parte superior de la web, es decir, lo primero que ve el usuario.

Para identificar cual es el Critical CSS se copia todo el código de CSS en siguiente :link: [Critical Path CSS Generator](https://jonassebastianohlsson.com/criticalpathcssgenerator/) y luego el resultado del _scraping_ del archivo se copia dentro de un tag `<style>` en la sección `<head>` de nuestro código.

El CSS restante (no crítico) se llama posteriormente, al final del `<body>` por medio de un tag `<link>` como usualmente se hacía antes de iniciar la optimización del sitio

### 8. Optimizando Imágenes

Para tener nuestro sitio totalmente optimizado solamente nos queda optimizar nuestras imágenes. Algunas veces estaremos renderizando una imagen con un tamaño mucho mayor del que tenemos en el sitio, por ello es buena práctica redimensionar nuestras imágenes al tamaño que mostramos en nuestro sitio, usaremos el servicio de :link:[ResizeImage](https://resizeimage.net/).

No basta solamente con redimensionar nuestras imágenes, también debemos comprimirlas y de preferencia tenerlas en formato PNG para evitar perdidas en la calidad de imagen, para esto usaremos el servicio :link: [Tiny PNG](https://tinypng.com/).

+ :link: [Optimizilla](https://imagecompressor.com/es/)
+ :link: [Squoosh](https://squoosh.app/)
+ :link: [Image Resizer](https://imageresizer.com/)

### 9. Ejercicio de optimización

Continuidad de optimización de las imagenes faltantes.

### 10. Imágenes y densidad de pixel

Existen pantallas con mayor densidad de pixeles, o también conocido como pantalla retina. Actualmente las imágenes de nuestro sitio se ven con baja cantidad de pixeles en las pantallas con densidad de 2x o superior, solucionaremos esto sencillamente con el atributo `srcset` y redimensionando las imágenes para que tengan el doble de tamaño, recuerda que también debemos comprimir estas imágenes para no afectar nuestra optimización.

Como incluir varias imagenes dependiendo su resolución.
```html
<img src="imagen.png" srcset="imagen.png, imagen@2x.png 2x">
```












































































































































