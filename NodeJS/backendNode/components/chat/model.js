const mongoose = require('mongoose');

// DE MONGOOSE IMPORTAMOS EL ESCHEMA
const Schema = mongoose.Schema;

// SE LE INDICA A MONGOOSE QUE CLASE DE ESCHEMA DESEAMOS PARA NUESTRO COMPONENTE
const mySchema = new Schema({
    users: [{
        type: Schema.ObjectId,
        ref: 'User',
    }]
});
// CUANDO SE TIENE EL SCHEMMA DEFINIDO, SE CREA EL MODELO EN MONGOOSE
// SE DEFINE EL NOMBRE DE LA TABLA Y EL SCHEMA
const model = mongoose.model('Chat', mySchema);

module.exports = model;
