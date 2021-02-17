// ARCHIVO DE CONFIGURACION PARA TRAER LAS VARIABLES DE ENTORNO A LA APP
require("dotenv").config();

const config = {
  // VARIABLE QUE INDICA SI ESTA EN PRODUCCION O DESARROLLO
  dev: process.env.NODE_ENV !== "production",
  port: process.env.PORT,
  dbUser: process.env.DB_USER,
  dbPassword: process.env.DB_PASSWORD,
  dbHost: process.env.DB_HOST,
  dbPort: process.env.DB_PORT,
  dbName: process.env.DB_NAME,
  sentryDns: process.env.SENTRY_DNS,
  sentryId: process.env.SENTRY_ID,
  authAdminUsername: process.env.AUTH_ADMIN_USERNAME,
  authAdminPassword: process.env.AUTH_ADMIN_PASSWORD,
  authAdminEmail: process.env.AUTH_ADMIN_EMAIL,
  authJwtSecret: process.env.AUTH_JWT_SECRET
};

module.exports = { config };
