'use strict'

const Hapi = require('@hapi/hapi');
// SE IMPORTA EL PLUGING PARA SERVIR LOS ARCHIVOS ESTATICOS
const inert = require('@hapi/inert');
// SE IMPORTA VISION PARA RENDESIZAR LOS TEMPLATES
const Vision = require('@hapi/vision');
// SE IMPORTA path QUE PARTE DE NODE
const path = require('path');
// SE EIMPORTA HANDLEBARS
const handlebars = require('handlebars');


// SE CREA EL SERVIDOR COMO OBJETO 
const server = Hapi.Server({
    // EL PUERTO SE ESTABLECE COMO PARAMETRO CON LA VARIALBLE DE ENTORNO PORT Y SI NO CON EL PUERTO 3000
    port: process.env.PORT || 3000,
    // CORRE EN EL LOCALHOST
    host: 'localhost',
    // SE DECLRAR LA VARIABLE/OBJETO PARA DECLRAR LA RUTA A LA CARPETA DE ARCHIVOS ESTATICOS
    routes: {
        files: {
            relativeTo: path.join(__dirname, 'public')
        }
    }
})
// CONFIGURACIÓN DE LAS RUTAS
const initRoutes = async () =>{
    // DEFINICIÓN DE RUTAS SE INDICA EL MÉTODO HTTP, URL Y CONTROLADOR/handler DE RUTA
    // SE DECLARAN DESPUÉS DEL PLUGIN YA QUE LAS RUTAS HACEN USO DEL MISOM PARA DEVOLVER ARCHIVOS ESTATICOS
    // RUTA HOME
    server.route({
        method: 'GET',
        path: '/',
        handler: (req, h) => {
            // METODO h REGRESA LA VISTA index EN EL LAYOUT CON EL VALOR EN EL OBJETO
            return h.view('index', {
                title: 'home'
            })
        }
    })
    // RUTA REGISTER GET
    server.route({
        method: 'GET',
        path: '/register',
        handler: (req, h) => {
            return h.view('register', {
                title: 'Registro'
            })
        }
    })
    // RUTA REGISTER POST
    server.route({
        method: 'POST',
        path: '/create-user',
        handler: (req, h) => {
            // PROPIEDAD DONDE SE RECIBEN LOS DATOS
            console.log(req.payload)
            return 'USUARIO CREADO EXITOSAMENTE'
        }
    })
    // RUTA PARA SERVIR ARCHIVOS ESTÁTICOS ASOCIADOS (IMG/CSS/JS)
    server.route({
        method: 'GET',
        path: '/{param*}',
        handler: {
            directory: {
                path: '.',
                index: ['index.html']
            }
        }
    })
}
// CONFIGURACION DE PANTILLAS
const initViews = async ()=>{
    server.views({
        // EL ENGINE ES hbs: handlebars
        engines: {
          hbs: handlebars
        },
        // SE BUSCA APARTIR DEL DIRECTORIO ACTUAL
        relativeTo: __dirname,
        // LAS VISTAS SE ENCUENTRAN EN VIEWS(DIRECTORIO)
        path: 'views',
        // SE HABILITA LAYOUT PARA NO REPETIR PEDASOS DE HTML EN TODAS LAS VISTAS
        layout: true,
        // LOS LAYOUTS SE ENCUENTRAN EN VIEW(DIRECTORIO) ESTABLECEMOS LA DIFERENCIA
        layoutPath: 'views'
    })
}
// FUNCION INICIAL
const main = async () =>{
    try {
        // REGISTRAR LOS PLUGINS QUE HAPI VA A NECESITAR PARA SERVIR ARCHIVOS ESTATICOS
        await server.register(require('@hapi/inert'));
        // SE REGISTRA VISION
        await server.register(Vision)
        // ES EL METODO QUE INICIA EL SERVIDOR
        await server.start()
        // SE INICIA LAS RUTAS
        await initRoutes()
        // SE INICIA LAS VISTAS
        await initViews()

    } catch {
        console.error(error)
        // SALIR DE NODEJS CON UN CÓDIGO DE ERROR (1), 0 ES UN CODIGO DE EXITO
        console.exit(1)
    } finally{
        console.log(`Servidor lanzado en ${server.info.uri}`)
    }
}
// SE INICIALIZA EL PROCESO
main()
