// ARCHIVO PARA CONECTAR LA BA CON MYSQL
const mysql = require('mysql');
// SE IMPORTA LA CONFIGURACIÓN PARA LA CONEXIÓN A LA BD
const config = require('../config');

const dbconf = {
    host: config.mysql.host,
    port: config.mysql.port,
    user: config.mysql.user,
    password: config.mysql.password,
    database: config.mysql.database,
};

let connection;
// FUNCION PARA MANEGAR LA CONEXION
function handleCon() {
    connection = mysql.createConnection(dbconf);

    connection.connect((err) => {
        if (err) {
            // AL MOMENTO DE HACER LA CONEXION SI HAY UN ERROR SE MUESTYRA CUAL ES EL ERROR
            console.error('[db err]', err);
            // SI SE DESCONECTA HACE LA PETICIÓN EN 2 SEGUNDOS
            setTimeout(handleCon, 2000);
        } else {
            // CUANDO SE CONECTA MANDA MENSAJE
            console.log('DB Connected!');
        }
    });
    // SI DURANTYE LA CONEXION HAY ERROR PROTOCOL_CONNECTION_LOST SE VUVLVA A CONECTYAR
    connection.on('error', err => {
        console.error('[db err]', err);
        if (err.code === 'PROTOCOL_CONNECTION_LOST') {
            handleCon();
        } else {
            throw err;
        }
    })
}

handleCon();

// SE REALIZA LA CONSULTA QUE TRAIGA TODO SOBRE LA TABLA
function list(table) {
    return new Promise( (resolve, reject) => {
        connection.query(`SELECT * FROM ${table}`, (err, data) => {
            if (err) return reject(err);
            resolve(data);
        })
    })
}
// FUNCION PARA TRAER UN USUARIO CON UN ID EN ESPECIFICO
function get(table, id) {
    return new Promise((resolve, reject) => {
        console.log("ID TO BE GET: ", id);
        console.log("IN TABLE TO GET: ", table);
        connection.query(`SELECT * FROM ${table} WHERE id=${id}`, (err, data) => {
            if (err) return reject(err);
            console.log("QUERY DONE: ", data);
            resolve(data);
        })
    })
}
// FUNCION PARA INSERTAR UN USUARIO
function insert(table, data) {
    return new Promise((resolve, reject)=>{
        console.log(`GOING TO MAKE AN INSERT INTO TABLE: ${table} with data: ${data}`)
        connection.query(`INSERT INTO ${table} SET ?`, data, (err, result) => {
            if(err) {
                console.error("### ERR ###: ",err)
                return reject(err)
            } else {
                resolve(result)
            }
        })
    })
}
// FUNCION PARA ACTUALIZAR UN USUARIO
function update(table, data) {
    return new Promise((resolve, reject)=>{
        console.log("DATA TO BE UPDATED: ",data);
        connection.query(`UPDATE ${table} SET ? WHERE id= ?`,[data, data.id],(err,result)=>{
            if(err) {
                console.error("UPDATE CANNOT BE DONE: ",err)
                return reject(err)
            } else {
                console.log("UPDATE DONE: ", result)
                resolve(result)
            }
        })
    })
}

// FUNCION PARA ACTUALIZAR MODIFICAR
// LA FUNCION  upsert VA VA A HACER LA DIFERENCIA QUE ENTRE UN INSERT Y UN UPDATE
// SI LA DATA TIENE IN data.id SERA UN UPDATE POR QUE ASI VIENEN DE
// ROUTER /api/components/user/network.js
const upsert = async (table, payload) =>
  new Promise((resolve, reject) => {
    console.log("DATA TO BE UPSERT: ", payload);
    connection.query(`INSERT INTO ${table} SET ? ON DUPLICATE KEY UPDATE ?`, [payload, payload], (error, data) => {
        console.log("UPSERT DATA: ", data);
        console.log("UPDATE TABLE: ", table);
        if (error) {
            return reject(error);
        }
        resolve(data);
    });
  });

// FUNCION ASINCRONA PARA SABER SI ESTA REGISTRADO EL USUARIO
// SE GUARDA LA LISTA PARA FILTRAR
function query(table, query) {
    return new Promise((resolve, reject) => {
        console.log("DATA TO BE QUERY: ", query);
        console.log("IN TABLE: ", table);
        connection.query(`SELECT * FROM ${table} WHERE ?`, query, (err, res) => {
            console.log('QUERY RESULT: ', res)
            if (err) return reject(err);
            resolve(res[0] || null);
        })
    })
}

module.exports = {
    list,
    get,
    upsert,
    query

};