// SE IMPORTA STORE PARA ALMACENAR 
const store = require('./store');
// FUNCION PARA AÑADIR UN USUARIO
function addUser(name) {
    console.log(name);
    if (!name) {
        // SE DEBUELVE UNA PROMESA RECHAZADA
        return Promise.reject('Invalid name');
    }
    const user = {
        name: name,
    }
    // SE ALMACENA EN store/add: addUser,
    // SE DEBUELVE UNA PROMESA
    return store.add(user);
}

function getUser() {
    return new Promise((resolve, reject) => {
        resolve(store.list());
    });
}

module.exports = {
    addUser,
    getUser,
    // updateMessage,
    // deleteMessage,
};