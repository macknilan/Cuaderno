console.log('Hello, TypeScript');

// Boolean
let muted: boolean = true;
muted = false;

// Números
let age = 6;
let numerador: number = 42;
let denominador: number = age;
let resultado = numerador / denominador;

// String
let nombre: string = 'Richard';
let saludo = `Me llamo ${nombre}`;

// Arreglos
let people: string[] = [];
people = ['Isabel', 'Nicole', 'Raul'];
// people.push("9000")

let peopleAndNumbers: Array<string | number> = [];
peopleAndNumbers.push('Ricardo');
peopleAndNumbers.push(9001);

// Enum
enum Color {
  Rojo = 'Rojo',
  Verde = 'Verde',
  Azul = 'Azul',
  Amarillo = 'Amarillo',
}

let colorFavorito: Color = Color.Amarillo;
console.log(`Mi color favorito es ${colorFavorito}`);

// Any
let comodin: any = 'Joker';
comodin = { type: 'Wildcard' };

// Object
let someObject: object = { type: 'Wildcard' };

// FUNCIONES
function add(a: number, b: number): number {
  return a + b;
}

const sum = add(4, 6);

function createAdder(a: number): (number) => number {
  return function(b: number) {
    return b + a;
  };
}

const addFour = createAdder(4);
const fourPlus6 = addFour(6);

function fullName(firstName: string, lastName: string = 'Smith'): string {
  return `${firstName} ${lastName}`;
}

const richard = fullName('Agente');
console.log(richard);

// INTERFACES
enum Color {
  Rojo = "Rojo",
  Verde = "Verde"
};

interface Rectangulo {
  height: number,
  width: number
  color?: Color
}

let rect: Rectangulo = {
  height: 4,
  width: 3,
  // color: Color.Verde
}

function area(r: Rectangulo) {
  return r.height * r.width;
}

const areaReact = area(rect);
rect.toString = function () {
  return this.color ? `Un rectangulo ${this.color}` : `Un rectangulo`;
}

console.log(rect.toString());