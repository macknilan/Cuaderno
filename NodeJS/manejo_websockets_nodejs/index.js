/* npm i express socket.io */
const express = require('express');
const app = express();
const server = require('http').Server(app);
const io = require('socket.io')(server);
const PORT = 8080;

app.use(express.static('public'));

io.on('connection', (socket) => {
    console.log('Nuevo cliente conectado');
    socket.emit('mensaje', 'Bienvenido');
})

setInterval( () => {
    io.emit('mensaje', 'Hola, les estoy saludando a todos');
}, 3000)

server.listen(PORT, () => {
    console.log(`Servidor iniciado en el puerot: http://localhost:${PORT}`);
})

