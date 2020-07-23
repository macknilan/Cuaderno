const { createServer } = require('http');

const port = 3000;

function router(req, res) {
    switch  (req.url) {
        case '/':
            res.end('<h1>HOLA req.url /</h1>');
            break
        default:
            res.write('404 ! URL NO EXISTE');
    }
}

const server = createServer(router);

server.listen(port, (err) => {
    if (err) {
        console.log('COULD NOS STABLISH A CONNECTION TO THE SERVER');
        console.error(err.message);
    }
    console.info(`> Ready ON http://localhost: ${port}`);
});
