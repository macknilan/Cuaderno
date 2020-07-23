


# Curso Básico de JavaScript

## Introducción a JavaScript
### ¿Qué es JavaScript?
    Leguaje interpretado, orientado a objetos, debilmente tipado y dinamico.
¿Realmente es un leguaje interpretado? **SI**  
Motor de JS es V8  
JS es Backwards es Compatible: La compatibilidad con versiones anteriores significa que cuando acepta como JS válida, no habrá un cambio futuro que haga que el código deje de funcionar.  

### ¿Por qué JavaScript?

JavaScript es uno de los 3 lenguajes que todos los desarrolladores web deben aprender:
    + HTML para definir el contenido de las páginas web
    + CSS para especificar el diseño de las páginas web
    + JavaScript para programar el comportamiento de las páginas web

Las páginas web no son el único lugar donde se usa JavaScript. Muchos programas de escritorio y servidor usan JavaScript. Node.js es el más conocido. Algunas bases de datos, como MongoDB y CouchDB, también usan JavaScript como su lenguaje de programación.

JS tiene a ser Desarrollo web, ya que tiene muchas framework que te ayudaran a desarrollar la aplicación web que deseas, pero también te sirve para desarrollar aplicaciones con React Native para android y ios, y electron para aplicaciones de escritorio para Windows y mac.

**WebAssembly**: es un nuevo tipo de código que puede ser ejecutado en navegadores modernos es un lenguaje de bajo nivel, similar al lenguaje ensamblador, con un formato binario compacto que se ejecuta con rendimiento casi nativo y provee un objetivo de compilación para lenguajes como C/C++ y Rust que les permite correr en la web. También está diseñado para correr a la par de JavaScript, permitiendo que ambos trabajen juntos.

### Elementos de un Lenguaje de Programación: Variables, Funciones y Sintaxis
Dos componentes principales:
    1. Data que guardamos en memoria
    2. Tareas(funciones) que haremos con esa data
```javascript
// ------------------ VALORES PRIMITIVOS 
40 <- valores

"Cadena de texto" <-- Cadena de texto

    ____
true    |
false   |<- boleanos
    ____|

        ____
null        |
undefined   |<- valores vacios, empty values
        ____|

// ------------------ VALORES OBJETOS
[1,2,3] <- Arrays
{ nombre:Rodolfo } <- Objeto

// ------------------ VALORES NO PRIMITIVOS 

typeof 40 -> "number"
typeof "Cadena de texto" -> "string"
typeof true -> "boolean"
typeof null -> "object"
typeof undefined -> "undefined"
typeof [1,2,3] -> "object"
typeof {nombre: Funano} -> "object"
```
### Variables
```javascript
/*
var es una palabra reservada en JS para poder guardar un valor en memoria.
El ";" nos permite indicar que termina una sentencia.
Las variales tienen dos estados: declarado e inicializado.
*/
var nombre = "Diego"; // VALOR DECLARADO E INICIADO.
var apellido; // VALOR DECLARADO.
apellido = "Perez"; // VALOR INICIADO.

var persona = {
    nombre: "Diego",
    edad: 30
}
```
### Funciones

Las funciones son un conjunto de sentencias, que utilizamos para realizar acciones con valores que guardamos en las variables.  
Funciones son como procedimientos o tares.  
Hay dos tipos de funciones, _DECLARATIVAS_ y de _EXPRESIÓN_.
Las funciones _declarativas_ se llaman así porque les declaramos un nombre a la función.  
Las funciones _expresivas_, también son conocidas como anónimas porque no les ponemos un nombre a la función, simplemente almacenamos la función dentro de una variable.  
Para llamar una función, se coloca el bombre de la función, seguido de "()". El "()" le dice a JS que hay mismo se llama la función.  
Dentro de "()", se indican los parámetros.  
```javascript
/*
    function() es una función anónima porque no tiene nombre.
*/
// DECLARATIVAS
function miFuncion1(){
    return;
}

// EXPRESION
var miFuncion2 = function(){
    return;
}

// DE EXPRESIÓN CON PARÁMETROS
var miFuncion3 = function(a,b){
    return a + b;
}

// LLAMANDO UNA FUNCIÓN.
miFuncion1();
miFuncion2();
miFuncion3(1,2);


// USO DE PARÁMETROS DE UNA FUNCIÓN.
var estudiante = "Diego"

holaEstudiante1(estudiante);
holaEstudiante2(estudiante);

functionholaEstudiante1(estudiante){
    console.log(`Hola ${estudiante}`);
}

functionholaEstudiante2(estudiante){
    console.log("Hola " + estudiante);
}

// USO DE PARÁMETRO DE UNA FUNCIÓN CON RETURN

var num1 = 10;
var num2 = 25;

console.log("Resultado: " + calcular(num1,num2));

functioncalcular(x,y){
    var resultado = x + y;
    return resultado;
}
```

### ¿Cuándo utilizar una función declarativa y una expresiva?
Cuando hablamos de funciones en JavaScript, tenemos dos tipos de funciones: Funciones Declarativas (function declaration / function statement) y Expresiones de función (function expression / funciones anónimas).

**Funciones Declarativas:** En las funciones declarativas, utilizamos la palabra reservada function al inicio para poder declarar la función:
```javascript
function saludar(nombre) {
    console.log(`Hola ${nombre}`);
}

saludar('Diego');
```
**Expresión de función:** En la expresión de función, la declaración se inicia con la palabra reservada var, donde se generará una variable que guardará un función anónima.
```javascript
var nombre = function(nombre){
    console.log(`Hola ${nombre}`)
}

nombre(‘Diego’);
```
A las funciones declarativas se les aplica `hoisting`, y a la expresión de función, no. Ya que el `hoisting` solo se aplica en las palabras reservadas `var` y `function`.

Lo que quiere decir que con las funciones declarativas, podemos mandar llamar la función antes de que ésta sea declarada, y con la expresión de función, no, tendríamos que declararla primero, y después mandarla llamar.

## Bases de JavaScript
### Scope
**variables globales:** Pueden ser accedidas desde un scope local o global. las variables globales son definidas fuera de las funciones _(Scope global)_

_**Scope local:**_Son aquellas variables definidas dentro del cuerpo de la función, estas son solo accedidas desde _dentro de la misma función._

**Scope Global:** variables que pueden ser accedidas y procesadas por cualquier función dentro del código.

### Hoisting
En JavaScript, las declaraciones (por ejemplo, de variables o funciones) se mueven al principio de su scope o ámbito. Este comportamiento se conoce como hoisting y es muy importante tenerlo en cuenta a la hora de programar para prevenir posibles errores.

+ Las funciones siempre se mueven arriba del scope. Por lo tanto, podemos elegir donde declararlas y usarlas.  
+ La declaración de las variables se mueven arriba del scope, pero no la asignación. Antes de usar una variable, habrá que crearla y asignarla.

### Coerción
+ Coerción implícita: Es cuando el lenguaje nos ayuda y cambia de un tipo de valor a otro tipo de valor.
+ Coerción explícita : Es cuando nosotros obligamos a un valor de un tipo a cambiar a otro tipo.
```javascript
// EJEMPLOS DE COERCIÓN:

var a = 4 + "7"; // CONVIERTE A 4 EN UN STRING Y LO CONCATENA CON EL "7", POR ESTO REGRESA UN STRING DE VALOR "47"

4 * "7"; // CONVIERTE AL "7" EN UN NÚMERO Y REALIZA LA OPERACIÓN, POR ESTO DEVUELVE 28

var a = 20;
var b = a + ""; // AQUÍ CONCATENAMOS PARA CONVERTIR LA VARIABLE A STRING (COERCIÓN IMPLÍCITA)
console.log(b); 

var c = String(a); // AQUÍ OBLIGAMOS A LA VARIABLE A CONVERTIRSE EN STRING (COERCIÓN EXPLÍCITA)
console.log(c);

vard = Number(c); // AQUÍ OBLIGAMOS A LA VARIABLE A CONVERTIRSE EN NÚMERO (COERCIÓN EXPLÍCITA)
console.log(d);
```

### Valores: Truthy y Falsy
+ :link:[Truthy](https://developer.mozilla.org/es/docs/Glossary/Truthy)
+ :link:[Falsy](https://developer.mozilla.org/es/docs/Glossary/Falsy)

```javascript
// EJEMPLOS EN LOS QUE BOOLEAN DEVUELVE FALSO:
Boolean(0); // false
Boolean(null); // false
Boolean(NaN); // false
Boolean(undefined); // false
Boolean(false); // false
Boolean(""); // false

// EJEMPLOS EN LOS QUE BOOLEAN DEVUELVE VERDADERO:
Boolean(1); // true para 1 o cualquier número diferente de cero (0)
Boolean("a"); // true para cualquier caracter o espacio en blanco en el string
Boolean([]); // true aunque el array esté vacío
Boolean({}); // true aunque el objeto esté vacío
Boolean(function(){}); // Cualquier función es verdadera también
```
### Operadores: Asignación, Comparación y Aritméticos.
:link:[Expressions and operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators)

```javascrit
// OPERADORES BINARIOS:
3 + 2 // SUMA
50 - 10 //  RESTA
10 * 20 // MULTIPLICACIÓN
20 / 2 // DIVISIÓN

"Diego " + "De Granda" // CONCATENACIÓN DE STRINGS

// OPERADORES UNITARIOS:
!false // NEGACIÓN DE LA NEGACIÓN = TRUE

// OPERADORES DE ASIGNACIÓN:
var a = 1; // ASIGNAMOS UN VALOR A LA VARIABLE

// OPERADORES PARA COMPARAR:
3 == "3"; // COMPARA LOS VALORES Y DEVUELVE "TRUE" EN ESTE CASO

3 === "3"; // COMPARA Y VALIDA LOS TIPOS Y VALORES. DEVUELVE "FALSO" EN ESTE CASO

5 < 3 // COMPARA Y VALIDA SI EL 5 ES MENOR A 3
5 > 3 // COMPARA Y VALIDA SI EL 5 ES MAYOR A 3
5 <= 6 // COMPARA Y VALIDA SI EL 5 ES MENOR O IGUAL AL 6
5 >= 6 // COMPARA Y VALIDA SI EL 5 ES MAYOR O IGUAL AL 6

a && b // VALIDA SI AMBAS VARIABLES SON VERDADERAS PARA QUE SE CUMPLA LA CONDICIÓN
a || b // AQUÍ SE CUMPLE LA CONDICIÓN SI ALGUNA DE LAS DOS VARIABLES ES VERDADERA

var edad = 40
edad++ // INCREMENTA EL VALOR EN 1

edad += 2 // INCREMENTA EL VALOR POR 2
```


## Condicionales
### Condicionales: If, Else, else if
:link:[Operador condicional (ternario)](https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Operadores/Conditional_Operator)
```javascript
var piedra = 0
var tijera = 1 
var papel = 2

function play (eleccion) {
    let computer = Math.floor(Math.random() * 3);
    console.log(computer)
    if (eleccion === computer) {
        console.log ("Empate");
    } else if ((eleccion === 0) && (computer === 1)) {
        console.log("Ganaste");
    } else if ((eleccion === 1) && (computer === 2)) {
        console.log("Ganaste");
    } else if ((eleccion === 2) && (computer === 0)) {
        console.log ("Ganaste")
    } else {
        console.log("Perdiste")
    }
};

play(papel);
```

### Switch
```javascript
var movimientos = ["piedra", "papel", "tijeras"];

function juego(eleccion) {
    random = movimientos[Math.floor(Math.random() * movimientos.length)];
    console.log("La PC eligió --> " + random);
    console.log("Tú elegiste --> " + eleccion);

    switch (eleccion) {
        case"piedra":
            switch (random) {
                case"piedra":
                    console.log("Empate");
                    break;
                case"papel":
                    console.log("Perdiste");
                    break;
                case"tijeras":
                    console.log("Ganaste");
                    break;
            }
            break;
        case"papel":
            switch (random) {
                case"piedra":
                    console.log("Ganaste");
                    break;
                case"papel":
                    console.log("Empate");
                    break;
                case"tijeras":
                    console.log("Perdiste");
                    break;
            }
            break;
        case"tijeras":
            switch (random) {
                case"piedra":
                    console.log("Perdiste");
                    break;
                case"papel":
                    console.log("Ganaste");
                    break;
                case"tijeras":
                    console.log("Empate");
                    break;
            }
            break;
    }
}

console.log(juego("tijeras"));
```

## Arrays
### Arrays
```javascript
// FORMA SINTAXICA DE GENERAR UN ARRAY
var frutas = ["Manzana", "Plátano", "Cereza", "Fresa"];
console.log(frutas);
console.log(frutas.length); // PARA VER TAMAÑO DEL ARRAY
console.log(frutas[0]); // CONSULTAR UN ELEMENTO DEL ARRAY EN POSICIÓN ESPECIFICA

// METODOS QUE NOS AYUDAN A MUTAR UN ARRAY
// AGREGAR MÁS FRUTAS AL FINAL DE NUESTRO ARRAY
var masFrutas = frutas.push("Uvas");
// ELIMINAR ULTIMO ELEMENTO DEL ARRAY
var ultimo = frutas.pop("Uvas");
// AGREGAR AL INICIO DE NUESTRO ARRAY
var nuevaLongitud = frutas.unshift("Uvas");
// BORRAR PRIMER ELEMENTO DEL ARRAY
var borrarFruta = frutas.shift("Manzana");
// NOS AYUDA A SABER LA POSICIÓN DEL ELEMENTO QUE LE PASEMOS AL ARRAY
var posicion = frutas.indexOf("Cereza");
```

## Loops
### Loops:For y For..of
Los bucles pueden ejecutar un bloque de código varias veces. JavaScript admite diferentes tipos de bucles:

+ `for` recorre un bloque de código varias veces
+ `for/in` recorre las propiedades de un objeto
+ `for/of` recorre los valores de un objeto iterable
+ `while` recorre un bloque de código mientras se cumple una condición específica
+ `do/while` también recorre un bloque de código mientras se cumple una condición específica

**For**
```javascript
// NUESTRO ARREY TIENE 4 ELEMENTOS
var estudiantes = [ "Soter", "Maria", "Sergio"];

// HACER LA TAREA DEL LOOP, LO EJECUTARA DE FORMA MANUAL. TRABAJAR LA FUNCIÓN PARA QUE HAGA LA TAREA
functionsaludarEstudiantes (estudiante){
    console.log(`Hola, ${estudiante}`);
}
// CUÁL SERÍA EL LOOP?
// ESTE SERÍA EL LOOP
// MIENTRAS LA VARIABLE I SEA MENOR A MENOR A LA LONGITUD DE ESTUDIANTES I SE VA A AUMENTAR CON +1 
for(var i = 0; i < estudiantes.length; i++){
    // SI SE CUMPLE LA CONDICIÓN MANDA A LLAMAR LOS SALUDOS
    saludarEstudiantes(estudiantes[i]);
}
```
**For of**
```javascript
var estudiantes = [ "Soter", "Maria", "Sergio"];
functionsaludarEstudiantes (estudiante){
    console.log(`Hola, ${estudiante}`);
}
// TENEMOS UN ARRAY DE ESTUDIANTES Y VAMOS A MANDAR  LLAMAR A CADA ESTUDIANTE DEL ARREY DE ESTUDIANTES
for(var estudiante of estudiantes){
    // MANDAMOS A LLAMAR NUESTRA FUNCIÓN
    saludarEstudiantes(estudiante);
}
```

### Loops:While
```javascript
var estudiantes = ["Maria", "Sergio", "Rosa", "Daniel"];

function saludarEstudiante(estudiante) {
    console.log(`Hola ${estudiante}`);
}

var i = 0;

// DO-WHILE
do {
    saludarEstudiante(estudiantes[i]);
    i++;
} while (i < estudiantes.length)

// WHILE
while (estudiantes.length > 0) {
    var estudiante = estudiantes.shift();
    saludarEstudiante(estudiante);
}
```

## Objects
### Objects
Ejemplo de Objeto:
```javascript
var miAuto = {
    marca: "Toyota",
    modelo: "Corolla",
    año: 2020
}
```
Acceder a una propiedad del objeto:
```javascript
miAuto.marca 
// "Toyota"
```
**Se pueden agregar propiedades que van a ser una función, se les llama métodos de objetos.**
```javascript
var miAuto = {
    marca: "Toyota",
    modelo: "Corolla",
    año: 2020, 
    detallesDelAuto: function () {
        console.log(`Auto ${this.modelo}${this.año}`);
}
// miAuto.detallesDelAuto();
// Auto Corolla 2020
```
### Objects: Función constructora
```javascript
var brands = ['Toyota', 'Mazda', 'Renault']
var cars = []

function Car(brand, model, year) { // <- FUNCION CONSTRUCTORA
    this.brand = brand
    this.model = model
    this.year = year
}

for (var i = 0; i < 30; i++)
    cars.push(new Car(brands[Math.floor(i/10)], `Serie ${i % 10}`, 1999 + i % 10)) // <- FUNCION CONSTRUCTORA

console.log(cars)
```

## Métodos de Arrays
### Métodos de recorridos de Arrays
+ **.filter** : Filtrar solo los elementos que deseamos (según ciertos criterios) y devolverlos en un nuevo array.
+ **.map** : Crea un nuevo array con los resultados de la llamada a la función indicada aplicados a cada uno de sus elementos.
```javascript
var articulos = [
    {nombre:'Bici',costo:800000},
    {nombre:'Tv',costo:2000000},
    {nombre:'Radio',costo:350000},
    {nombre:'Movil',costo:3000000},
    {nombre:'Cuaderno',costo:50000},
    {nombre:'PC',costo:1900000},
    {nombre:'Mouse',costo:30000},
    {nombre:'Escoba',costo:10000}
];
var filtraArticulos = articulosComprados.filter(function(articulo){
    return articulo.costo <= 500000;
});
var mapearArticulos = articulosComprados.map(function(articulo){
    return articulo.nombre;
});
var mapeaFiltro = filtraArticulos.map(function(articulo){
    return articulo.nombre;
});
console.log(`Los articulos comprados son ${mapearArticulos} y los que tienen un valor menor a 500 mil son ${ apeaFiltro}.`);
```
```javascript
const articulos = [
  { nombre: 'Bici', costo: 800000 },
  { nombre: 'Tv', costo: 2000000 },
  { nombre: 'Radio', costo: 350000 },
  { nombre: 'Movil', costo: 3000000 },
  { nombre: 'Cuaderno', costo: 50000 },
  { nombre: 'PC', costo: 1900000 },
  { nombre: 'Mouse', costo: 30000 },
  { nombre: 'Escoba', costo: 10000 }
];

let articulosFitrados = articulos.filter( ({costo}) => costo < 500000 );
console.log(articulosFitrados);

let nombreFitrados = articulos.map( ({nombre}) => nombre);
console.log(nombreFitrados);
```

### Métodos de recorridos de Arrays 2

```javascript
var articulos = [
    { nombre: "Bici", costo: 3000 },
    { nombre: "TV", costo: 2500 },
    { nombre: "Libro", costo: 320 },
    { nombre: "Celular", costo: 10000 },
    { nombre: "Laptop", costo: 20000 },
    { nombre: "Teclado", costo: 500 },
    { nombre: "Audifonos", costo: 1700 },
];

//filter Genera un nuevo array
var articulosFiltrados = articulos.filter(function(articulo){
    return articulo.costo <= 500; //articulos con precio menor a 500 pesos
});

//map Ayuda a mapear ciertos elementos de los articulos, es necesario generar nuevo array
var nombreArticulos = articulos.map(function(articulo){
    return articulo.nombre;
});

//find Ayuda a encontrar algo dentro del array articulos
var encuentraArticulo = articulos.find(function(articulo){
    return articulo.nombre === "Laptop";
});

//forEach No es necesario generar nuevo array, se utiliza para realizar un recorrido de un array principal
articulos.forEach(function(articulo){
    console.log(articulo.nombre);
});

//some Se genera nuevo array, regresa un condición en Boolean
var articulosBaratos = articulos.some(function(articulo){
    return articulo.costo <= 700;
});
```
**Otra forma**

```javascript
const articulos = [
  { nombre: 'Bici', costo: 800000 },
  { nombre: 'Tv', costo: 2000000 },
  { nombre: 'Radio', costo: 350000 },
  { nombre: 'Movil', costo: 3000000 },
  { nombre: 'Cuaderno', costo: 50000 },
  { nombre: 'PC', costo: 1900000 },
  { nombre: 'Mouse', costo: 30000 },
  { nombre: 'Escoba', costo: 10000 }
];

let articulosFitrados = articulos.filter( ( {costo} ) => costo < 500000 ); // filtra todos los valores semejantes
console.log(articulosFitrados);

let nombreFitrados = articulos.map( ( {nombre} ) => nombre);
console.log(nombreFitrados);

let buscarArticulo = articulos.find( ( {nombre} ) => nombre === 'Cuaderno' ); // Devuelve el primer valor que encuentra
console.log(buscarArticulo);

let printArticulos = articulos.forEach( ( {nombre, costo} ) => console.log(nombre, costo)); // Itera el array como un for of

let exitenEsosArticulos = articulos.some( ( {costo} ) => costo <= 500000 ); // Devuelve Verdader cuando si existen o falso cuando no
console.log(exitenEsosArticulos);
```

























































































