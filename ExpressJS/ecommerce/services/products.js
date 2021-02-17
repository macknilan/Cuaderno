const productsMocks = require("../utils/mocks/products");
const MongoLib = require("../lib/mongo");

// SE CREA LA CALSE ProductsService CON LOS METODOS PARA REALIZAR LAS PETICIONES HTTP
class ProductsService {
  constructor() {
    // SE ESTABLECE QUE LA collection/tabla SEA products
    this.collection = "products";
    this.mongoDB = new MongoLib();
  }

  async getProducts({ tags }) {
    // SE ARMA EL QUERY EN FORMATO MONGO DB DE QUE SI LOS TAGS EXISTEN
    const query = tags && { tags: { $in: tags } };
    // SE ENVIA EL QUERY A LA CLASE MongoLib QUE SE IMPORTA DEL ARCHIVO lib/mongo.getAll
    const products = await this.mongoDB.getAll(this.collection, query);
    
    // SI LOS PRODUCTOS NO EXISTEN DEVUELVE UN ARREGLO VACIO
    return products || []; 
  }
  // LISTAR SOLO UN PRODUCTO IDENTIFICADO POR ID
  async getProduct({ productId }) {
    // SE ENVIA EL QUERY A LA CLASE MongoLib QUE SE IMPORTA DEL ARCHIVO lib/mongo.get
    const product = await this.mongoDB.get(this.collection, productId);
    return product || {};
  }
  // CREAR NUEVO PRODUCTO
  async createProduct({ product }) {
    // SE ENVIA EL QUERY A LA CLASE MongoLib QUE SE IMPORTA DEL ARCHIVO lib/mongo.create
    const createProductId = await this.mongoDB.create(this.collection, product);

    return createProductId;
  }
  // ACTUALIZAR NUEVO PRODUCTO IDENTIFICADO POR EL id
  async updateProduct({ productId, product }) {
    // SE ENVIA EL QUERY A LA CLASE MongoLib QUE SE IMPORTA DEL ARCHIVO lib/mongo.update
    const updateProductId = await this.mongoDB.update(
      this.collection,
      productId,
      product
    );

    return updateProductId;
  }
  // ELIMINAR NUEVO PRODUCTO
  async deleteProduct({ productId }) {
    // SE ENVIA EL QUERY A LA CLASE MongoLib QUE SE IMPORTA DEL ARCHIVO lib/mongo.delete
    const deletedProductId = await this.mongoDB.delete(
      this.collection,
      productId
    );

    return deletedProductId;
  }
}

module.exports = ProductsService;
