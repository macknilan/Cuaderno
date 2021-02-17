// app EMPIEZA UN PROCESO BACKGROUND POR DEFECTO, PERO SE TIENEN QUE ESPECIFICAR QUE SEA CUANDO YA ESTA LISTA, NO ANTES
import { app, BrowserWindow } = require('electron');

// VENTANA PRINCIPAL PARA TODA LA APLICACION
let mainWindow;

// PARA CUANDO ESTE LISTO ELECTRON CON app, CON NODE SE ESCUCHA EL EVENTO PARA CUANDO ESTE LISTO CON ready Y CREE LA VENTANA
app.on('ready', createWindow);

// FUNCION QUE PARA CREAR LA VENTANA
function createWindow() {
    mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
    });
    // PARA QUE LA PAGINA ESTE DENTRO DE LA VENTA
    mainWindow.loadFile('index.html');
}



