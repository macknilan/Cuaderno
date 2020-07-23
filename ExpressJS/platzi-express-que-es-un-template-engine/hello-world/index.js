const express = require("express");
const app = express();

// RUTA CON EL METODO GET EN RAIZ /
app.get("/", function(req, res, next) {
  // res.send('hello world'); // MANDAR 
  // res.send({ hello:  "world" }); /* PARA SERVIR JSON */
  const my_data = {
    name: 'rodolfo',
    age: '40 años'
  }
  res.send(my_data); /* PARA SERVIR JSON */
});

const server = app.listen(8000, function() {
  console.log(`Listening http://localhost:${server.address().port}`);
});
