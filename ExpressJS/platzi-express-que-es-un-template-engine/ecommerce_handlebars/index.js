const express = require("express");
const consolidate = require('consolidate');
const path = require("path");
const app = express();

// SE IMPORTA DE LOS PRODUCTOS DEL FOLSER products
const productsRouter = require('./routes/products');

// SE IMPORTA handlebars Y SE ESTABLECE COMO hbs
app.engine('hbs', consolidate.handlebars);

// SE ESTABLECE LA RUTA D ELAS VISTAS
app.set("views", path.join(__dirname, 'views'));

// SE ESTABLECE QUE LA VISTAS SEAN CON EL MOTOR DE TEMPLATES SEA handlebars
app.set("view engine", 'hbs');

app.get("/", function(req, res) {
    res.render('index', { hello: "hola", world: "mundo" })
});

const server = app.listen(8000, function() {
  console.log(`Listening http://localhost: ${server.address().port}`);
});

