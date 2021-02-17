import router from './routes';

window.addEventListener('load', router); // PARA CUANDO CARGA POR PRIMERA VES LA PAGINA
window.addEventListener('hashchange', router); // ESCUCHAR LAS RUTAS A LAS CUALES EL USUARIO SE ESTA MOBIENDO
