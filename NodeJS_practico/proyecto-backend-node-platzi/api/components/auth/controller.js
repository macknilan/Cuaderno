const auth = require('../../../auth');
// auth ES EL PARAMETRO A BUSCAR EN LA BD
const bcrypt = require('bcrypt');
// SE IMPORTA LIBRERIA PARA ENCRIPTAR CONTRASEÑAS

const TABLA = 'auth';

module.exports = function(injectStore) {
    let store = injectStore
    if (!store) {
        store = require('../../../store/mysql');
    }
    
    // FUNCION PARA SABER QUE EL USUARIO ESTE REGISTRADO
    async function login(username, password) {
        const data = await store.query(TABLA, { username: username });
        // SE COMPARA password CON data.password QUE ESTA LAMACENADO EN LA BD
        return bcrypt.compare(password, data.password)
            .then(sonIguales => {
                if (sonIguales === true) {
                    // Generar token;
                    // console.log(data)
                    // return auth.sign(data)
                    return auth.sign({...data});
                } else {
                    throw new Error('Informacion invalida');
                }
            });
        /* console.log(data)
        return data; */
        // SI EL PASSWORD ENVIADO ES IGUAL AL PASS GUARDADO
        /* if (data.password === password) {
            // GENERAR TOKEN;
            return auth.sign(data);
        } else {
            throw new Error('Informacion invalida');
        } */
    }

    // FUNCION PARA CREAR LA LOS USUARIOS
    async function upsert(data) { 
        const authData = {
            // EL IDENTIFICADOR DE LOS DATOS  AUTORIZACIÓN SON LOS MISMOS QUE EL DE USUARIO
            id: data.id,
        }
        // SE TRABAJA DE FORMA SEPARADA Y CREAR LOS CAMPOS QUE SE NECESITAN
        //  PARA QUE SE ACTUALIZE LO QUE NECESITA
        if (data.username) {
            authData.username = data.username;
        }

        if (data.password) {
            // authData.password = data.password;
            // SE ENCRIPTA LA HASHEA CON 5 VECES QUE SE EJECUTE EL ALGORITMO(ENTRE 5 Y 10)
            authData.password = await bcrypt.hash(data.password, 5);
        }
        // isNew SE SETA PARA PODER GUARDAR EN MYSQL CUANDO NO CONTENGA data.id
        /* console.log(`authData`)
        console.log(authData) */
        return store.upsert(TABLA, authData);
    }

    return {
        upsert,
        login,
    }

}
