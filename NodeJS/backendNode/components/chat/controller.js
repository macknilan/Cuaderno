// SE IMPORTA STORE PARA ALMACENAR 
const store = require('./store');

function addChat(users) {
    //  SE COMPRUEBA SI HAY USUARIOS Y SI LOS USUARIOS SON UN ARRAY
    if (!users || !Array.isArray(users)) {
        return Promise.reject('Invalid user list');
    }
    const chat = {
        users: users,
    }
    return store.add(chat);
}

function listChats(UserId) {
    return store.list(userId);
}

module.exports = {
    addChat,
    listChats,
}
