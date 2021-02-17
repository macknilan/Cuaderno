const http = require('http'); // SE REQUIERE EL MODULO HTTP

// SELE PASA UNA FUNCION "router" PARA DEFINIR EL PUERTO DONDE SE VA A ESCUCHAR ES EL 3000 CON "linsten"
http.createServer(router).listen(3000);


// REQUEST, RESPONSE
function router(req, res) {
    console.log('Nueva petición!');
    console.log(req.url); // TRAER A LA URL A LA QUE ESTAN LLAMANDO

    switch (req.url) {
        case '/hola':
            let saludo = hola();
            res.writeHead(201, { 'Content-Type': 'text/plain' })
            res.write(saludo);
            res.end(); // SE TERMINA LA PETICIÓN
            break;
        
        default:
            res.write('Error 404: No se lo que quieres');
            res.end();
    }
    // ESCRIBIR EN LA CABECERA
    // res.writeHead(201, { 'Content-Type': 'text/plain' })

    // ESCRIBIR RESPUESTA AL USUARIO
    // res.write('Hola, ya se usar HTTP de NodeJS');

    // res.end();
}

function hola() {
    return 'Hola, que tal';
}
// ES BUENA PRACTICA DECIR EN QUE PUERTO ESTA ESCUCHANDO
console.log("Escuchando http en el puerto 3000");