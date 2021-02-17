const mongoose = require('mongoose');

// DE MONGOOSE IMPORTAMOS EL ESCHEMA
const Schema = mongoose.Schema;

// SE LE INDICA A MONGOOSE QUE CLASE DE ESCHEMA DESEAMOS PARA NUESTRO COMPONENTE
const mySchema = new Schema({
    // A user SELE ASIGNA EL TIPO ESPECIAL DE MONGO "Object ID",  SE ESPERA QUE RECIBA COMO USUARIO EL id Y NO string
    chat: {
        type: Schema.ObjectId,
        ref: 'Chat',
    },
    user: {
        type: Schema.ObjectId,
        ref: 'User',
    },
    message: {
        type: String,
        required: true,
    },
    date: Date,
    file: String,
});
// CUANDO SE TIENE EL SCHEMMA DEFINIDO, SE CREA EL MODELO EN MONGOOSE
// SE DEFINE EL NOMBRE DE LA TABLA Y EL SCHEMA
const model = mongoose.model('Message', mySchema);

module.exports = model;
