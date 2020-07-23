// SE IMPORTA STORE PARA ALMACENAR 
const store = require('./store');
const socket = require('../../socket.js').socket; // SE IMPORTA EL OBJETO
// FUNCION PARA AÑADIR UN MENSAJE
function addMessage(chat, user, message, file) {
    return new Promise((resolve, reject) => {
        if (!chat || !user || !message) {
            console.error('[messageController] No hay chat, usuario o mensaje');
            return reject('Los datos son oncorrectos');
        }
        let fileUrl = '';
        if (file) {
            fileUrl = `http://localhost:3000/app/files/${file.filename}`
        }

        const fullMessage = {
            chat: chat,
            user: user,
            message: message,
            date: new Date(),
            file: fileUrl,
        }
        // SE ALMACENA EN store
        store.add(fullMessage);

        // SE ENVIAN LOSMENSAJES A SOCKET/ EMITIR LOS MESAJES
        socket.io.emit('message', fullMessage);

        resolve(fullMessage);
    });
}
// FUNCION PARA RETORNAR/TRAER LOS MENSAJES VIENEN DE network.js
// CON filterUser TRAE POR PARAMETRO EL VALOR DE USUARIO QUE SE QUIERE FILTRAR
// PARA MANDARLO A store
function getMessages(filterUser) {
    return new Promise((resolve, reject) => {
        resolve(store.list(filterUser));
    });
}
// FUNCION PARA ACTUALIZAR MENSAJE QUE COINCIDA CON EL id
// FUNCION QUE RECIBE DE controller.js EL id, message PROVENIENTES DE LA BD
// SE VERIFICA QUE CONTENGA VALORES LAS VARIABLES
function updateMessage(id, message) {
    return new Promise(async (resolve, reject) => {
        if (!id || !message) {
            reject('Invalid data')
            return false;
        }
        // EN `store.js` SE CREA EL METODO updateText PARA ACTUALIZAR EL MENSAJE
         const result = await store.updateText(id, message)
         resolve(result)
    })
}

function deleteMessage(id) {
    return new Promise((resolve, reject) => {
        if (!id) {
            reject('Id invalido');
            return false;
        }
        store.remove(id)
        .then(() => {
            resolve();
        })
        .catch(e => {
            reject(e);
        })
    })
}

module.exports = {
    addMessage,
    getMessages,
    updateMessage,
    deleteMessage,
};