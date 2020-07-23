let XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest;
// let API = 'https://rickandmortyapi.com/api/character/';

const fetchData = (url_api) => {

    return new Promise((resolve, reject) => {

        const xhttp = new XMLHttpRequest();
        xhttp.open('GET', url_api, true); // EL VALOR DE true ES ACTIVAR EL ASINCRONISMO EN XMLHttpRequest POR DEFAULT ESTA ACTIVADO
        xhttp.onreadystatechange = (() => {
            if (xhttp.readyState === 4) { // VELIDACIÓN DE CONEXION EXITOSA
                (xhttp.status === 200) ? resolve(JSON.parse(xhttp.responseText)) : reject(new Error('Error', url_api))
            }
        });
        xhttp.send();
    });
}
module.exports = fetchData;