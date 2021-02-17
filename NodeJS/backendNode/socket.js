// ARCHIVO QUE SE ENCARGA DE LEVANTAR EL INICIALIZAR EL SERVICIO DE SOCKETIO
// GENERAR UNA INSTANCIA, Y COMPARTIR SOCKETIO
const socketIO = require('socket.io');
// SE GUARDA COMO OBJETO PARA QUE GUARDE COMO REFERNCIA A SOCKET
const socket = {}

// 
function connect(server) {
    socket.io = socketIO(server);
    //  SE GENERA SERVER
}

//  SE EXPORTA LA UNCION DE CONECCIÓN
//  Y SOCKET QUE TIENE DENTRO LA INSTANCIA DE SOCKET.IO
module.exports = {
    connect,
    socket,
}








