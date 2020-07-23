// SE IMPORTA LA SCHEMMA PARA QUE SE GUARDE EN EL MODELO ESTYABVLECIDO
const Model = require('./model');

// FUNCION PARA AGREGAR LOS MENSAJES QUE LLEGAN EN controller.js
function addUser(user) {
    const myUser = new Model(user);
    // SE GUARDA CON EL MODELO EXTENDIDO DE MOONGOSE
    return myUser.save();
}

// FUNCION PARA RETORNAR LA LISTA DE MENSAGES, SI ES QUE EXISTEN A controller.js
async function getUser() {
    const users = await Model.find();
    return users;
}

module.exports = {
    add: addUser,
    list: getUser,
    // updateText: updateText,
    // remove: removeMessage,
}
