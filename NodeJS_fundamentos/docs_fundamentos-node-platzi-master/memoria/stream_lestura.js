const fs = require('fs');
const stream = require('stream');
const util = require('util');

let data = '';

let readableStream = fs.createReadStream(__dirname + '/input.txt');
readableStream.setEncoding('UTF8');

readableStream.on('data', function (chunk) {
    data += chunk;
});

readableStream.on('end', function() {
    console.log(data);
});