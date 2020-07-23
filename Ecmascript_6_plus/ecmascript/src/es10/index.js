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
    error
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