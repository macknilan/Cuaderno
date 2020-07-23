const bcrypt = require("bcrypt");
const chalk = require("chalk");
const MongoLib = require("../../lib/mongo");
const { config } = require("../../config");

// FUNCION PARA CONSTRUIR EL USR ADMIN CON EL PWD HASHEADO Y CON LAS CREDENCIALES DE .ENV
function buildAdminUser(password) {
  return {
    password,
    username: config.authAdminUsername,
    email: config.authAdminEmail,
  };
}

// SE BUSCA EN LA COLECCION  users EL username 
async function hasAdminUser(mongoDB) {
  const adminUser = await mongoDB.getAll("users", {
    username: config.authAdminUsername,
  });
  // SI RETORNA EL USR Y TIENE ALMENOS UN VALOR, EXISTE
  return adminUser && adminUser.length;
}
// FUNCION PARA CREAR EL USUARIO CON LA LIBRERIA bcrypt SE CREA EL PWD
async function createAdminUser(mongoDB) {
  const hashedPassword = await bcrypt.hash(config.authAdminPassword, 10);
  const userId = await mongoDB.create("users", buildAdminUser(hashedPassword));
  return userId;
}

// FUNCION ASINCRONA PRINCIPAL 
async function seedAdmin() {
  try {
    const mongoDB = new MongoLib();

    if (await hasAdminUser(mongoDB)) { // COMPROBAR SI EN BD TIENE UN USR ADMIN
      console.log(chalk.yellow("Admin user already exists"));
      return process.exit(1);
    }
    // SI EL USUARIO NO ESTA CREADO, SE CREA MOSTRANDO CON QUE ID SE CREO
    const adminUserId = await createAdminUser(mongoDB);
    console.log(chalk.green("Admin user created with id:", adminUserId));
    return process.exit(0);
  } catch (error) {
    console.log(chalk.red(error));
    process.exit(1);
  }
}

// SE TIENE QUE EJECUTAR LA FUNCION
seedAdmin();
