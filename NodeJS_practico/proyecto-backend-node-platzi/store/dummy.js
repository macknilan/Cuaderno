// 
const db = {
    "user": [
        {id: '1', name: "Mack"}
    ],
};

async function list(tabla) {
    // EN CASO DE QUE tabla NO VENGA CON DATA QUE MANDE UN ARRAY BACIO
    return db[tabla] || [];
}

async function get(tabla, id) {
    let col = await list(tabla);
    return col.filter(item => item.id === id)[0] || null;
}
// PARA ACTUALIZAR/INSERTAR
async function upsert(tabla, data) {
    if (!db[tabla]) {
        db[tabla] = []
    }
    db[tabla].push(data)
    // SE MUESTRA COMO SE GUARDA
    console.log(db);
}

async function remove(tabla, id) {
    return true;
}

// FUNCION ASINCRONA PARA SABER SI ESTA REGISTRADO EL USUARIO
// SE GUARDA LA LISTA PARA FILTRAR
async function query(tabla, q) {
    console.log(tabla)
    let col = await list(tabla);
    console.log(col)
    let keys = Object.keys(q); // q -> username
    let key = keys[0];
    
    return col.filter(item => item[key] === q[key])[0] || null;
}

module.exports =  {
    list,
    get,
    upsert,
    remove,
    query,
}
