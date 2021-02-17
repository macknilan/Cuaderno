


# Curso de ECMAScript 6+

## 1. Bienvenida al curso
### 1. Bienvenida al curso y qué es ECMAScript
:link: [Standard ECMA-262 ECMAScript 2019 Language Specification](https://www.ecma-international.org/publications/standards/Ecma-262.htm)

_ECMAScript_ es la especificación del lenguaje JavaScript propuesto por _ECMA_ Internacional, que es la institución encargada de los estándares, y JavaScript, es el lenguaje de programación que utiliza las especificaciones propuestas, que van siendo añadidas cada año a partir del 2015, cuando fue lanzado ES6.

1. 6th Edition - ECMAScript 2015
2. 7th Edition - ECMAScript 2016
3. 8th Edition - ECMAScript 2017
4. 9th Edition - ECMAScript 2018
5. 10th Edition - ECMAScript 2019

## 2. ¿Qué se implementó en ES6?
### 2. Default Params y Concatenación
Los parametros por defecto son los valores que le podemos pasar a una funcion por defecto. 

Se crea el archivo `index.js` en al ruta `ecmascript/src/es6/` 

```javascript
function newFunction(name, age, country) {
    var name = name || 'oscar';
    var age = age || '23';
    var country = country || 'MX';
    console.log(name, age, country);
}


// e6

function newFunction2(name = 'mack', age = 31, country = 'MX') {
    console.log(name, age, country)
}

newFunction();
newFunction2();

// TEMPLATE LITERALS
let hello = "Hello";
let world = "World";
let epicPhrase = hello + ' ' + world;
console.log(epicPhrase)
let epicPhrase2 = `${hello} ${world}`
console.log(epicPhrase2)
```

### 3. LET y CONST, Multilínea, Spread Operator y Desestructuración

+ :link: [La diferencia entre let y var en Javascript](https://platzi.com/blog/la-diferencia-entre-let-y-var/)
+ :linl: [Spread Operator MDN web docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)

+ **Var**: tiene un Scope de función
+ **Let/Const**: tienen un Scope de bloque

```javascript
// FORMA NORMAL SEPARACIONES DE LÍNEA.

// ANTES PARA REALIZAR MULTILÍNEAS SE USABA  backslash (alt+92) + n + "" CONTINUAR UNA LÍNEA
let Frase ="KANSClnclnsnspan pscapo apso  \n"// MULTILÍNEAS
+ "ljsndljnvsjd"

// CON LOS TEMPLATE LITERALS `` SE PUEDE SENCILLAMENTE REALIZAR UN ENTER PARA PASAR DE LÍNEA.
let Frase_es6 = `Lknlasknlncs
dksvñsnkvlksnnldkvsnd`;

console.log(Frase);
console.log(Frase_es6);

// --------------------------------------------------------------------------------------
// DESTRUCTURACIÓN DE ELEMENTOS:

let person ={
    'name':'mack',
    'age': 54,
    'country':'MX'
};

// SE ACCEDE DEL SIGUIENTE MODO
console.log(person.name, person.age, person.country);

// e6

// AHORA CON LA DESTRUCCIÓN DE ELEMENTOS, SUCEDE UNA ESPECIE DE RESUMEN
// DONDE SE EXTRAE UN FACTOR COMÚN DEL NOMBRE DEL OBJETO
let {name, age, country} = person;

// SE ACCEDE DEL SIGUIENTE MODO
console.log(name, age, country);

// --------------------------------------------------------------------------------------
// SPREAD OPERATOR: PERMITE EXPANDIR VARIOS ELEMENTOS.
// TENEMOS VARIOS ELEMENTOS EN ARREGLOS QUE QUEREMOS UNIR EN UN SOLO ELEMENTO PARA PRESENTARLOS.

let team1= ['mack','oscar','ricardo'];
let team2= ['valeria','yessica','camila'];

let conjunto_union=['rodolfo',...team1,...team2]
console.log(conjunto_union);


// --------------------------------------------------------------------------------------
// ASIGANCIONES MEDIANTE let SE PUEDEN INICILIZAR VARIABLES 
// CUYO SCOPE ESTÁ SOLO EN EL BLOQUE DE CÓDIGO EN EL QUE ESTÁ LLAMADA
// EN OTRAS PALABRAS, SOLO PUEDE EXISTIR LAS VARIABLES let DENTRO
// DE LAS LLAVES EN QUE SE LLAMAN. VAR SE SEGUIRÁ USANDO PARA
// VARIABLES GLOBALES Y LOCALES.

{
    var globalVar= "...";
}

{
    let globalLet= "***";
    console.log(globalLet); 
    // AL ESTAR DENTRO DE LAS LLAVES O EL BLOQUE DE CÓDIGO
    // CONSOLE SE EJECUTARÁ CON NORMALIDAD
}

// AL EJECUTAR ESTA ARROJA ERROR AL ESTAR FUERA DEL SCOPE DONDE FUE DECLARADA.
console.log(globalVar);
console.log(globalLet); 

// --------------------------------------------------------------------------------------

// CONST, PERMITE ESTABLECER UNA VARIABLE COMO UNA CONSTANTE
// DONDE EL VALOR DECLARADO NO PODRÁ CAMBIAR.

const a = "Soy constante";
a = "No soy constante" ; 
// AL EJECUTAR ARROJA ERROR PORQUE NO PUEDE CAMBIARSE UNA CONSTANTE LUEGO DE DECLARARSE.

console.log(a);
```

### 4. Arrow Functions, Promesas y Parámetros en objetos

```javascript
// PARAMETERS IN OBJECTS
let name = 'Oscar';
let age = 32;

const obj = {
    name: name,
    age: age
};
console.log('Before ES6 -> ', obj);

// es6
const objES6 = {
    name,
    age
};
console.log(`After ES6 -> `, objES6);

// ARROW FUNCTIONS
const names = [{
    name,
    age
}, {
    name: 'Yesica',
    age: 27
}];

let listOfNames = names.map(function(item) {
    console.log('Before ES6 -> ', item.name);
});

// es6
let listOfNamesES6 = names.map(item => console.log(`After ES6 -> ${item.name}`));

 // Promises
const helloPromise = () => {
    return new Promise((resolve, reject) => {
        if (true) {
            resolve('Hey!');
        } else {
            reject('Upss!');
        }
    });
};

hello Promise()
    .then(response => console.log('response -> ', response))
    .then(() => console.log('message -> Hello World!'))
    .catch(error => console.log('error -> ', error));
```

### 5. Clases, Módulos y Generadores
+ :link: [Import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
+ :link: [Export](https://developer.mozilla.org/en-US/docs/web/javascript/reference/statements/export)

```javascript
// Classes
classCalculator {
    constructor() {
        this.valueA = 0;
        this.valueB = 0;
    }

    sum(valueA, valueB) {
        this.valueA = valueA;
        this.valueB = valueB;
        returnthis.valueA + this.valueB;
    }
}

const calc = new Calculator();
console.log('Calc Result -> ', calc.sum(2, 3));

// Modules
import { hello } from './class4-module.js';
console.log('Hello Module -> ', hello());

// Generators
function* helloWorld() {
    if (true) {
        yield 'Hello, ';
    }

    if (true) {
        yield 'World!';
    }
}
const generatorHello = helloWorld();
console.log('generatorHello first call -> ', generatorHello.next().value);
console.log('generatorHello second call -> ', generatorHello.next().value);
console.log('generatorHello third call -> ', generatorHello.next().value);

// class4-module.js
const hello = () => {
  return'Hello World!';
};

export default hello;
```

## 3. ¿Qué se implemento en ES7?
### 6. ¿Qué se implemento en ES7?

**7th Edition - ECMAScript 2016**

```javascript
let numbers = [1, 2, 3, 7, 8];

if (numbers.includes(9)) {
  console.log('Si se encuentra el valor 7');
} else {
  console.log('No se encuentra.')
}

let base = 4;
let exponent = 4;
let result = base ** exponent;

console.log(result);
```


## 4. ¿Qué se implemento en ES8?
### 7. ¿Qué se implemento en ES8?
**8th Edition - ECMAScript 2017**

```javascript
const data = {
    frontend: 'Oscar',
    backend: 'ISabel',
    design: 'Ana',
}

const entries = Object.entries(data);
console.log(entries);
console.log(entries.length);

const data = {
    frontend: 'Oscar',
    backend: 'ISabel',
    design: 'Ana',
}

const values = Object.values(data);
console.log(values)
console.log(values.length)


const string = 'hello';
console.log(string.padStart(7, 'hi'));  // hidello
console.log(string.padEnd(12, ' -----')) // hello  -----
console.log('food'.padEnd(12, '  -----')) // foo   -----

// Trailing commas

const obj = {
    name: 'oscar',
}
```

### 8. Async Await

```javascript
const helloWorld = () => {
    return new Promise((resolve, reject) => {
        (true) ? setTimeout(() => resolve('Hello World'), 3000) : reject(new Error('Test Error'))
    })
};

const helloAsync = async () => {
    const hello = await helloWorld();
    console.log(hello);
};

helloAsync();

const anotherFunction = async () => {
    try {
        const hello = await helloWorld();
        console.log(hello);
    } catch (error) {
        console.log(error);
    }
};

anotherFunction();
```

## 5. Actualidad y próximos pasos de ECMAScript
### 9. ¿Qué se implemento en ES9?
**9th Edition - ECMAScript 2018**
Operador de reposo

```javascript
const obj = {
    name: 'oscar',
    age: 32,
    country: 'MX'
};

let { name, ...all } = obj;
console.log(name, all);
// oscar { age:32, countr: 'MX' }

let { country, ...all } = obj;
console.log(all);
// { name:'oscar', age:32 }
```
Objeto de propagación
```javascript
const obj = {
    name: 'Oscar',
    age: 32
}
const obj1 = {
    ...obj,
    country: 'MX'
}
console.log(obj1);
// {name: "Oscar", age: 32, country: "MX"}
```
Promise finally

```javascript
const helloWorld = () => {
    return new Promise((resolve, reject) => {
        (true) ? setTimeout(() => resolve('Hello World'), 3000) : reject(new Error('Test Error'))
    });
};

helloWorld()
    .then(response => console.log(response))
    .catch(error => console.log(error))
    .finally(() => console.log('Finalizo'))
```

Expresiones regulares

```javascript
// año/mes/día
const regexData = /([0-9]{4})-([0-9]{2})-([0-9]{2})/
const match = regexData.exec('2018-04-20');
const year = match[1]
const month = match[2]
const day = match[3]

console.log(year, month, day);
```

### 10. ¿Qué se implemento en ES10?
**10th Edition - ECMAScript 2019**

```javascript
let array = [1, 2, 3, [1, 2, 3, [1, 2, 3]]];

console.log(array.flat(0));
// [1, 2, 3, Array(4)]

let array = [1, 2, 3, 4, 5];

console.log(array.flatMap(value => [value, value * 2]));
// [1, 2, 2, 4, 3, 6, 4, 8, 5, 10]


let hello = '        hello world';
console.log(hello);
console.log(hello.trimStart()); // ELIMINAR LOS ESPACIOS EN BLANCP
//         hello world
// hello world


let hello = 'hello World       ';
console.log(hello);
console.log(hello.trimEnd());
// hello World       
// hello World

try {

} catch {
    error // Optional Catch Binding
}


let entries = [
    ["name", "oscar"],
    ["age", 32]
];
console.log(Object.fromEntries(entries)); // NOS DEBUELVE UN ARREGLO
// {name: "oscar", age: 32}

let mySymbl = `My Symbol`;
let symbol = Symbol(mySymbl);
console.log(symbol.description);
// My Symbol
```

### 11. TC39 y Cierre del curso

:link: [TC39 - Specifying JavaScript](https://tc39.es/)





































