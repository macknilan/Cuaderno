// EL CAMPO _id SI NO ES AGREGADO POR NOSOTROS DE FORMA EXPLÍCITA, MONGODB LO AGREGA POR NOSOTROS COMO UN ObjectId
// SE IMPORTA LA LIBRERIA DEL DRIVER PARA LA CONEXION
const { MongoClient, ObjectId } = require("mongodb");
// ARCHIVO DE CONFIGURACION
const { config } = require("../config");

// SE IMPORTAN LAS VARIABLES DE CONEXION DEL ARCHIVO DE config/index.js
const USER = encodeURIComponent(config.dbUser);
const PASSWORD = encodeURIComponent(config.dbPassword);
const DB_NAME = config.dbName;

// const MONGO_URI = `mongodb://${USER}:${PASSWORD}@${config.dbHost}:${config.dbPort}/?authSource=${DB_NAME}`; // prettier-ignore

// CONFIGURACIÓN PARA CONEXION CON MONGODB ATLAS CON LA LIGA Conect your application
const MONGO_URI = `mongodb+srv://${USER}:${PASSWORD}@${config.dbHost}/${DB_NAME}?retryWrites=true&w=majority`; // prettier-ignore

// SE CREA LA CLASE MongoLib CON SU METODO connect() PARA CONECTAR CADA VES QUE SE HACE UNA PETICION HTTP
class MongoLib {
  constructor() {
    console.log(`'MONGO_URI -> ${MONGO_URI}`)
    this.client = new MongoClient(MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true });
    this.dbName = DB_NAME;
  }

  connect() {
    return new Promise((resolve, reject) => {
      this.client.connect(error => {
        if (error) {
          reject(error);
        }

        console.log("Connected succesfully to mongo");
        resolve(this.client.db(this.dbName));
      });
    });
  }
  // LISTAR TODOS LOS PRODUCTOS
  getAll(collection, query) {
    return this.connect().then(db => {
      return db
        .collection(collection)
        .find(query) // REGRESA EL RESULTADO DEL QUERY PERSONALIZADO QUE SE OCUPARA PARA LOS TAGS
        .toArray(); // SE CONVIERTE A ARRELGO PARA QUE SE PUEDA MANIPULAR
    });
  }
  // LISTAR SOLO UN PRODUCTO IDENTIFICADO POR ID
  get(collection, id) {
    return this.connect().then(db => {
      // REGRESA EL RESULTADO DEL QUERY PARA SOLO ENCONTRAR UN PRODUCTO POR MEDIO DE id
      return db.collection(collection).findOne({ _id: ObjectId(id) });
    });
  }
  // CREAR NUEVO PRODUCTO
  create(collection, data) {
    return this.connect()
      .then(db => {
        // REGRESA EL RESULTADO DEL insertOne
        return db.collection(collection).insertOne(data);
      })
      .then(result => result.insertedId);
  }
 // ACTUALIZAR NUEVO PRODUCTO IDENTIFICADO POR EL id
  update(collection, id, data) {
    return this.connect()
      .then(db => {
        return db
          .collection(collection)
          // REGRESA EL RESULTADO DE updateOne 
          .updateOne({ _id: ObjectId(id) }, { $set: data }, { upsert: true });
      })
      .then(result => result.upsertedId || id);
  }
 // ELIMINAR NUEVO PRODUCTO
  delete(collection, id) {
    return this.connect()
      .then(db => {
        // REGRESA EL RESULTADO DE deleteOne
        return db.collection(collection).deleteOne({ _id: ObjectId(id) });
      })
      .then(() => id);
  }
}

module.exports = MongoLib;
