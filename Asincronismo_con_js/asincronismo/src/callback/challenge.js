

let XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest;
let API = 'https://rickandmortyapi.com/api/character/';

function fetchData(url_api, callback) {
    let xhttp = new XMLHttpRequest();
    xhttp.open('GET', url_api, true); // EL VALOR DE true ES ACTIVAR EL ASINCRONISMO EN XMLHttpRequest POR DEFAULT ESTA ACTIVADO
    xhttp.onreadystatechange = function (event) {
        if(xhttp.readyState === 4) { // VELIDACIÓN DE CONEXION EXITOSA
            if(xhttp.status === 200) { // VELIDACIÓN DE LA CONECCIÓN FUE ACEPTADA
                callback(null, JSON.parse(xhttp.responseText)) // DENTRO DE NODE EL 1ER VALOR ES EL ERROR, Y EL SEGUNDO ES LA INFO DEL RESULTADO DEL API
            } else {
                const error = new Error('Error' + url_api);
                return callback(error, null)
            }
        }
    }
    xhttp.send();
}

fetchData(API, function(error1, data1) {
    if (error1) return console.error(error1);
    fetchData(API + data1.results[0].id, function (error2, data2) {
        if (error2) return console.error(error2);
            fetchData(data2.origin.url, function (error3, data3) {
                if (error3) return console.error(error3);
                    console.log(data1.info.count)
                    console.log(data2.name)
                    console.log(data3.dimension)
            });
    })
});




























