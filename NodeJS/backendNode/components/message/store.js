// EN EL ARRAY ES DONDE SE GUARDAN TODOS LOS MENSAJES
// ACTUA COMO MOCK DE LA BD
// const list = [];

// SE IMPORTA LA SCHEMMA PARA QUE SE GUARDE EN EL MODELO ESTYABVLECIDO
const Model = require('./model');

// FUNCION PARA AGREGAR LOS MENSAJES QUE LLEGAN EN controller.js
function addMessage(message) {
    // SE AGREGAN LOS MENSAJES NUEVOS A LA LISTA PARA DESPUES AGREGAR A LOS MENSAJES
    // list.push(message);
    // SE INSTYANCIA LA VBUEVA CLASE DEL MODELO
    const myMessage = new Model(message);
    // SE GUARDA CON EL MODELO EXTENDIDO DE MOONGOSE
    myMessage.save();
}
// FUNCION PARA RETORNAR LA LISTA DE MENSAGES, SI ES QUE EXISTEN A controller.js
// CON LA MOD. EN `model.js` SE TIENE QUE HACER LA RELACIÓN DEL NO ID AL USUARIO "STRING/NOMBRE" AL QUE ESTA RELACIONADO
// Y SE MUESTRE TODA LA INFO DEL USUARIO
async function getMessage(filterUser) {
    return new Promise((resolve, reject) => {
        let filter = {} // SE DECLARA OBJETO FILTRO VACIO
        // SI filterUser ES DIFERENTE DE null DECLARADO EN network.js
        if (filterUser !== null) {
            filter = { user: filterUser }
        }
        Model.find(filter)
            // LO QUE HACE ES BUSCAR DENTRO DE CADA ELELEMTO QUE SE BUSQUE Y SE LE DICE QUE POPULE user
            .populate('user')
            // SE EJECUTA populate
            .exec((error, populated) => {
                if (error) {
                    reject(error);
                    return false;
                }
                // SE REGRESA EN EL resolve LA RELACIÓN ENCONTRADA
                resolve(populated);
            });
    });
}

async function updateText(id, message) {
    // Model.findOne SE ENCARGA DE BUSCAR UNA COINCIDENCIA POR PARTE DE MONGOOSE EN LA BD
    // BUSCANDO POR id
    const foundMessage = await Model.findOne({
        _id: id
    });
    // EL MENSAJE QUE SE ENCUENTRA SE LE PASA EL NUEVO VALOR A LO QUE ESTA ALMACENADO
    foundMessage.message = message;
    // Y SE ESPERA QUE SE GUARDE
    const newMessage = await foundMessage.save();
    // PARA RETORNAR EL VALOR
    return newMessage;
}

async function removeMessage(id) {
    return Model.deleteOne({
        _id: id
    });
}

module.exports = {
    add: addMessage,
    list: getMessage,
    updateText: updateText,
    remove: removeMessage,
}
