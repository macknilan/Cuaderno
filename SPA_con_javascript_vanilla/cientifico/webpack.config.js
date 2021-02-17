const path = require('path'); // NOS PERMITE ACCEDER A DONDE ESTÁMOS EN LAS CARPETAS. YA SEA EN LOCAL O EN LA NUBE.
const HtmlWebpackPlugin = require('html-webpack-plugin'); // ARCHIVO NECESARIO PARA TRABAJAR CON HTML.
const CopyWebpackPlugin = require('copy-webpack-plugin') // COMPLEMENTO DE WEBPACK PARA COM COPIAR LOS ESTILOS AL COMPILADO QUE SE ESTA GENERANDO


module.exports = {  // AQUÍ SE ENCUENTRA TODA LA CONFIGURACIÓN DE LO QUE VA A SUCEDER. MODULO PARA EXPORTAR.
    entry: './src/index.js', // PUNTO DE ENTRADA CON SU DIRECCIÓN.AQUÍ VIVE EL CÓDIGO INICIAL Y DE AQUÍ PARTE AL DESARROLLO
    output: { // DONDE SE ENVÍA EL PROYECTO ESTRUCTURADO Y COMPILADO LISTO PARA PRODUCCIÓN.
        path: path.resolve(__dirname, 'dist'),  // CREAMOS EL LUGAR DÓNDE SE EXPORTARÁ EL PROYECTO.
        filename: 'main.js'// ESTE ES EL NOMBRE DEL ARCHIVO FINAL PARA PRODUCCIÓN.
    },
    resolve: {
        extensions: ['.js'], // EXTENSIONES QUE VAMOS A UTILIZAR.
    },
    module: { // SE CREA UN MODULO CON LAS REGLAS NECESARIAS QUE VAMOS A UTILIZAR.
        rules: [    // REGLAS
            {   //  ESTRUCTURA DE BABEL
                test: /\.js?$/, // NOS PERMITE IDENTIFICAR LOS ARCHIVOS SEGÚN SE ENCUENTRAN EN NUESTRO ENTORNO. (REGEX)
                exclude: /node_modules/,    // EXCLUIMOS LA CARPETA DE NODE MODULES
                use: {
                    loader: 'babel-loader',    // UTILIZAR UN LOADER COMO CONFIGURACIÓN ESTABLECIDA.
                }
            }
        ]
    },
    plugins: [  // ESTABLECEMOS LOS PLUGINS QUE VAMOS A UTILIZAR
        new HtmlWebpackPlugin(    // PERMITE TRABAJAR CON LOS ARCHIVOS HTML
            {
                inject: true,   // CÓMO VAMOS A INYECTAR UN VALOR A UN ARCHIVO HTML.
                template: './public/index.html',    // DIRECCIÓN DONDE SE ENCUENTRA EL TEMPLATE PRINCIPAL
                filename: './index.html'// EL NOMBRE QUE TENDRÁ EL ARCHIVO
            }
        ),
        new CopyWebpackPlugin([{
            from:'./src/styles/styles.css',
            to: '' // NO LA REQUIERE
        }])
    ]
}