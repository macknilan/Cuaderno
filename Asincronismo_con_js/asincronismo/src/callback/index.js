function sum(num1, num2) {
    return num1 + num2;
}

function calc(num1, num2, callback) {
    return callback(num1, num2);
}

console.log(calc(2, 7, sum));
// ------------------------------------------


function date(callback) {
    console.log(new Date);

    setTimeout(()=>{ 
        // ESTE CODIGO SE EJECUTA DESPUES DE UN TIEMPO ESPECIFICADO
        let date = new Date;
        // SE EJECUTA LA FUNCION QUE NUESTRA FUNCION DATE RECIBE COMOPARAMETRO
        callback(date); 
    },3000);
}

// ESTA SERA LA FUNCION MANDADA A LLAMAR COMO CALLBACK
function printDate(dateNow){
    console.log(dateNow);
}

date(printDate);


