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

// Template literals
let hello = "Hello";
let world = "World";
let epicPhrase = hello + ' ' + world;
console.log(epicPhrase)
let epicPhrase2 = `${hello} ${world}`
console.log(epicPhrase2)

// --------------------------------------------------------------------------------------
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


// CONST, PERMITE ESTABLECER UNA VARIABLE COMO UNA CONSTANTE
// DONDE EL VALOR DECLARADO NO PODRÁ CAMBIAR.

const a = "Soy constante";
a = "No soy constante" ; 
// AL EJECUTAR ARROJA ERROR PORQUE NO PUEDE CAMBIARSE UNA CONSTANTE LUEGO DE DECLARARSE.

console.log(a);

// --------------------------------------------------------------------------------------

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
    returnnew Promise((resolve, reject) => {
        if (true) {
            resolve('Hey!');
        } else {
            reject('Upss!');
        }
    });
};


helloPromise()
    .then(response => console.log('response -> ', response))
    .then(() => console.log('message -> Hello World!'))
    .catch(error => console.log('error -> ', error));

// --------------------------------------------------------------------------------------

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

// --------------------------------------------------------------------------------------

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

const obj = {
    name: 'oscar',
}

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

// --------------------------------------------------------------------------------------








