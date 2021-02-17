module.exports = {
    api: {
        port: process.env.API_PORT || 3000,
    },
    jwt: {
        secret: process.env.JWT_SECRET || 'nota-secret!!!'
        // SE OBTIENEN COMO VARIABLE DE ENTORNO SI NO nota-secret!!!
    },
    mysql: {
        host: process.env.MYSQL_HOST || '127.0.0.1',
        port: process.env.MYSQL_PORT || '3306',
        user: process.env.MYSQL_USER || 'nodejs_platzi_2020',
        password: process.env.MYSQL_PASS || 'curso practico nodejs',
        database: process.env.MYSQL_DB || 'nodejsplatzi2020',
    },
}