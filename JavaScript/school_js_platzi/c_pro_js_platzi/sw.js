// Self HACE REFENCIA AL SERVICE WORKER ES COMO THIS A LOS OBJETOS
self.addEventListener('install', event => {
    // CREAMOS UN PRECACHE CON UNA LISTA DE RECURSOS QUE QUEREMOS QUE MANTENGA EN CACHE
    event.waitUntil(precache());
})
// CUANDO OCURRA UNA PETICIÓN QUEREMOS A IR AL CACHE PARA VER SI ENCONTRAMOS LA RESPUESTA
self.addEventListener('fetch', event => {
    // EXTRAEMOS LA PETICIÓN
    const request = event.request;
    // SOLO QUEREMOS HACER ALGO CON LAS PETICIONES QUE SON GET
    if (request.method !== "GET")
        return;

    // ACTUALIZAR EL CACHE
    event.waitUntil(updateCache(cache))
    // BUSCAMOS EN EL CACHE
    // event TIENE OTRA FUNCIÓN QUE SE LLAMÁ RESPONDER CON responseWith
    // VAMOS A RESPONDER CON UNA RESPUESTA CACHEADA
    event.respondWith(cachedResponse(request))
})
// ESCRIBIMOS LA FUNCIÓN DEL PRECACHE
async function precache() {
    // PARA TRABAJAR CON CACHE TENEMOS QUE TRABAJAR CON UNA PARTE
    // DE LA API DEL DOM QUE SE LLAMÁ CACHES, Y LO QUE HAY QUE HACER ES ABRIR UN CACHE EN ESPECIFICO
    // CREAMOS UNA INSTANCIA DE CACHE QUE LE VA A PERTENECER O SE VA A LLAMAR V1,
    // PODEMOS PONERLE COMO QUERAMOS PORQUE APENAS ESTAMOS HACIENDO UNA INSTANCIA,
    // ESTE CACHE REGRESA UNA PROMESA, POR LO CUAL HAY QUE ESPERARLA
    const cache = await caches.open("v1");

    // UNA VEZ TENEMOS LA INSTANCIA DE CACHE QUEREMOS AÑADIR VARIOS RECURSOS
    // AÑADIRMOS TODOS NUESTRO RECURSOS, LOS CUALES SON TODOS LO ARCHIVOS QUE HEMOS ESCRITO
    // TENEMOS QUE REGRESARLO PORQUE DEVUELVE UNA PROMESA
    return cache.addAll([
        // ES MUY IMPORTANTE ASIGNARNE ESTE REQUEST
        '/',
        'index.html',
        'styles.css',
        'MediaPlayer.js',
        'index.js',
        'plugins/AutoPause.js',
        'plugins/AutoPlay.js',
        'buckbunny.mp4'
    ]);
}
// VAMOS A PASARLE EL request
async function cachedResponse(request) {
    // COMENZAMOS ABRIENDO EL CACHE 
    const cache = await caches.open("v1");
    // DEBEMOS CHECAR SI EN EL CACHE TENEMOS LA CONTESTANCIÓN AL request
    // PARA HACER ESO VAMOS A GUARDALO EN EL response
    // ESTAMOS PREGUNTANDO AL CACHE
    // ¿YA TIENES UNA COPIA QUE LE corresponse AL request?
    const response = await cache.match(request)
    // COMO ES POSIBLE QUE ESTE RESPONSE SEA UNDEFINE, TENEMOS QUE CONTESTAR CON LO QUE NOS DE LA RED
    return response || fetch(request);
}
async function updateCache(request) {
    const cache = await caches.open("v1");
    const response = await fetch(request);
    return cache.put(request, response)
}