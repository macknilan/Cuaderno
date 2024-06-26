# Curso de Introducción al Desarrollo Backend FastAPI

## Fundamentos del desarrollo web

### 2. Yin y Yang de una aplicación: frontend y backend

### 3. Framework vs. librería

**Framework**: Será la base sobre la cual podrás construir y desarrollar tu proyecto, incluye todas las herramientas necesarias para completarlo (incluye librerías, estándares y reglas). Conjunto de librerías, reglas y estándares para construir un producto digital.

**Librería**: Solo aborda una utilidad especifica, pudiendo agregar más de una en tu proyecto. Eso si, asegúrate que no interfieran con el código de otra librería.

### 4. Cómo se conecta el frontend con el backend: API y JSON

La unión entre el Frontend y el Backend se hace a través de una _API_: Application Programming Interface.

Una _API_ es una sección del backend que permite que el frontend pueda comunicarse con él a través de mensajes bidireccionales (de ida y vuelta).

Tenemos dos grandes estándares para crear las \_API_s:

- **SOAP** (_Simple Objetct Access Protocol_): Mueve la información a través de un lenguaje XML (_Extensible Markup Language_). Es similar al HTML, es un lenguaje demarcado. _SOAP_ es un protocolo que ha quedado en el olvido.
- **REST** (_Representational State Transfer_): Utiliza otro lenguaje JSON (Javascript Objet Notation). Un JSON no es más que un diccionario de Python. Los diccionarios de Python son lo mismo que los objetos de JS.

a. **API**: Application Programming Interface
b. **SOAP**: Simple Object Access Protocol
c. **REST**: Representational State Transfer
d. **XML**: Extensible Markup Language
e. **JSON**: JavaScript Object Notation

### 5. El lenguaje que habla Internet: HTTP

🔗 [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

### 6. ¿Cómo es el flujo de desarrollo de una aplicación web?

📕 [Flujo de desarrollo de una aplicación web](../files/como_es_el_flujo_de_desarrollo_de_una_aplicacion_web.pdf) ↗️

### 7. El hogar de tu código: el servidor

1. **IaaS**: Infraestructura como servicio. Es el tipo de servicio que nos permite indicarle al proveedor del servidor las especificaciones que requerimos en nuestro proyecto (RAM, SSD, CPU). Las más populares de este tipo son: AWS, Azure y Digital Ocean
2. **PaaS**: Plataforma como servicio. Es el tipo de servicio que nos permite indicarle al proveedor del servidor que se encargue de realizar todas las actualizaciones que requerimos en nuestra app. Solo nos permite elegir que cosas particulares requiere nuestro proyecto a nivel general a través de una interfaz. Las más populares de este tipo son: Firebase, Heroku y Google App Engine
3. **SaaS**: Software como servicio. Esta opción nos permite utilizar una aplicación de un proveedor para hacer funcionar nuestro proyecto. Las más populares de este tipo son: Slack, WordPress y Google Docs

📕 [Infraestructura Iaas, PaaS, SaaS](../files/el_hogar_de_tu_codigo_el_servidor.pdf) ↗️

## Diseño de una API

### 8. Proyecto: diseño y bosquejo de una API

CRUD Create Read Update Delete.

- Framework
  - FastApi
  - Django → REST
  - Flask

El lugar al que las APIs envían las peticiones y donde vive el recurso, se llama endpoint.

Endpoint / Route / Path

```html
<http://example.com/api/twet>
```

### 9. Proyecto: diseñando los endpoints de los Tweets

Aquí se simplifica la creación de los endpoints, sin embargo hay que saber que cada sigla del CRUD tiene una representación en el mundo de las APIs y se llaman verbos http que sencillamente indican en la petición que se realiza al servidor que se quiere hacer.

Aquí la transformación de CRUD a los verbos HTTP

- _Create_: `POST`
- _Read_: `GET`
- _Update_: `PUT`
- _Delete_: `Delete`

🔗 [HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) ↗️

Seria buena practica mejor definir los endpoints de la siguiente manera

- _Create_ a tweet: `/tweets/ : POST`
- _Read_ all tweets: `/tweets/ : GET`
- _Read_ a tweet: `/tweets/{id}/ : GET`
- _Update_ a tweet: `/tweets/{id} : PUT`
- _Delete_ a tweet: `/tweets/{id}/ : DELETE`

PD: La simplificación no tiene nada de malo pero esta simplemente es una forma mas profesional para hacerlo

### 10. Proyecto: diseñando los endpoints para los usuarios

📕 [Endpoints usuarios](../files/proyecto_creando_los_endpoints_para_los_usuarios.pdf) ↗️

### 11. Qué lenguaje y framework escoger para

📕 [Que lenguaje y frameworks escojer para backend](../files/que_lenguaje_y_framework_escoger_para_backend.pdf) ↗️
