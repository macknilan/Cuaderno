# WebPack

## MyNotes

+ :link: [Offical webpage Webpack](https://webpack.js.org/)

+ Webpack se define como un empaquetador de módulos estaticos para aplicaciones JavaScript modernas.
    - Gestión de dependencias
    - Ejecución de tareas
    - Conversión de formatos
    - Servidor de desarrollo
    - Carga y uso de módulos

![webpack bundle your...](imgs/webpack_bundle_your_01.png)


#### Webpack Config
```js
const path = require('path');

module.export = {
    entry: '',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: '[name].js'
    },
    resolve: {
        extensions: []
    },
    module: {
        rules: []
    },
    plugins: []
}
```
#### Múltiples archivos de configuración
```js
const path = require('path');

module.export = {
    // PROD
    mode: 'production',
    devtool: 'source-map',
    optimization: {
        ...
    },
    // DEVELOP
    mode: 'production',
    devtool: 'eval-source-map',
}
```
#### Babel
> Es una herramienta que nos permite transformar nuestro código Javascript JS6 a Javascript que cualquier navegador soporte

#### Hot Reload

```js
module.export = {
    ...
    devServer: {
        contentBase: path.join(__dirname, 'dist'),
        compress: true,
        port: 9000
    }
}
```
























































































