// ARCHIVO QUE SE ENCARGA DE LA CONECCIÓN A LA BD DE MONGODB
// SE IMPORTA LA DB DE MONGOOSE PARA GUARDAR EN LA DB
const db = require('mongoose');
// QUE MOONGOOSE UTILIZE LAS PROMESAS DE FORMA MAS SIMPLE(BUENA PRACTICA)
// url = 'mongodb+srv://db_usr_rodolfo:___________________________________________/test'
db.Promise = global.Promise;
async function connect(url) {
    await db.connect(url, {
        useNewUrlParser: true, // PARA ELIMINAR PROBLEMAS DE CO,PATYIBILIDAD EN CSO DE EL SERVISOR SEA MÁS NUEVO O MAS ANTIGUO
        useUnifiedTopology: true, // RECOMENDACIÓN DE MOOGOOSE
    });
    console.log('[db] CONECTYADA CON EXITO')
}

module.exports = connect;