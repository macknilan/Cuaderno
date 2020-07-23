const fs = require('fs');
const stream = require('stream');
const util = require('util');

let data = '';

let readableStream = fs.createReadStream(__dirname + '/input.txt');
readableStream.setEncoding('UTF8');

// readableStream.on('data', function (chunk) {
//     data += chunk;
// });

// readableStream.on('end', function() {
//     console.log(data);
// });

// SE ESCRIBE DIRECTAMENTE ESCRIBIENTO EN EL stdout DEL SISTEMA
// process.stdout.write('hola')
// process.stdout.write('que')
// process.stdout.write('tal')

// CREA UN STREAM DE TRANSFORMACIÓN DOBLE DE ESCRITURA/LECTURA
const Transform = stream.Transform;

// TRANSFORMACIÓN A MAYUSCULAS
function Mayus() {
    Transform.call(this);
}

util.inherits(Mayus, Transform);

// SE CREA EL PROTOTIPO PARA PASAR A MAYUSCULAS EL chunk 
Mayus.prototype._transform = function(chunk, codif, cb) {
    chunkMayus = chunk.toString().toUpperCase();
    this.push(chunkMayus);
    cb();
}
// SE INSTANCIA PARA PODER OCUPAR EL PROTOTIPO
let mayus = new Mayus();

// pipe LA FUNCION QUE SE UTILIZA PARA MANDARLA DE UN LUGAR A OTRO
// SE LE PASA A readableStream LA INSTANCIA DEL PROTOTIPO "mayus" Y DESPUES SE MANDA A SALIDA ESTANDAR stdout
readableStream
    .pipe(mayus)
    .pipe(process.stdout);