
```bash

     :PJ5                                                                                           
      !@&^~!                                                                                        
     Y&@@&G@B~:.                                                                                    
    .&@@&B?^GG@@&?^                                                                                 
  J#&@@@@&#B~:PG&BY~.!?^                                                                            
.Y&@@@BPPY~^:.  .:.:~JG#B7                                                                          
@5G:!#~ ^?!YPP5Y~~^~?                                                                               
#5@GJ#@B&#&B^.    ^~J                 ~^^^^^^^~~~:  :Y#&                           7P&Y             
.@@@@&@B#Y  .     !~Y                 :#@@~^^~~J@G  .Y@@                           ^&@5             
 7@@@#@G~:.7J.      Y                  7@&      ..    @@                            ?@5             
  &&@&@?:7G^.       J:                 ?@&    :^     .@@        ..         ...      ?@5             
  !B?@@G:G~ .?J  Y? ??                 ?@@??J5@?     .@@.    !GP75&#.    ?B?7J#B    ?@5  ~#&PJ!     
   GJB@@G!5B&?Y. .^ .Y                 ?@&...:#!     .@@.    ?7   B@!    @@!.  ^    ?@5 7G?.        
    BY@@@#^#Y!       :?                ?@&           .@@.    .~77!&@~    .Y&@@B~    ?@&5&@Y         
    .Y#@@@G?^?!!7:   .P~               J@&           .@@.   P@B   B@!   ^^   ^&@^   J@G  J@&!       
      YB@@@@@7J&@#G   !#~             !B&#Y7:       .Y&&57. !&&5?!Y&#Y. !&GJ??BJ   !#&#?^ .G@#J!    
       ?P#@@@~ ?@@G~.   ^~.                                                ..                       
        ~5P@@@#JP@#&&^   .J7                                                                        
         .7YP@@B?YG#GJ7~. ..Y?.                                                                     
           .!JB@@&@@&B@@BP^  7G5~.                                                                  
             .!?Y@@@@@&@B&&J   .^~~!^.        75.                                                   
                ^P&&&@@@@@@@PY..:^^!YY?YJ7!^J&@5..  ..                                              
                   :~7YPP#&&@@@@@@PBGBP5PB@@#BBB&@@@@@&#&#.                                         
                        ..:^7JP####G#&&#&@@@@@&&&GY7??^:.                                           
                                    .........                                                       
                                                                 
```

🔗 🏠 [Flask](https://flask.palletsprojects.com/en/2.2.x/)

# Flask

Flask es un microframework hecho en Python el cual una de sus grandes ventajas es que es simple y fácil de personalizar a medida que la aplicación crezca también las dependencias que se van a utilizar.

Algunas diferencias de con Django son:

1. Utiliza un template llamado Jinja2 que esta inspirado en los Django Templates.
2. Django es todo incluido mientras que Flask es lo más simple posible.
3. Django tiene un módelo MVC mientras que Flask no tiene un módelo especifico es libre.
4. Django tiene ORM mientras que Flask es más personalizable al trabajar con bases de datos.
5. Podemos extender sus funcionalidades con librerías `flaskextensions`

Extensiones de Flask.  
Aqui se mencionaran las mas usadas con Flask:  

```bash
flask-script  # Permite tener un comando de la línea de comando para manejar la aplicación.
flask-Bootstrap  # Hojas de estilo para la página.
flask-WTF  # Sirve para generar formularios de HTML con clases y objetos.
flask-Sqlalchemy  # Sirve para poder generar el modelo de datos.
flask-login  # Sirve para la autenticación de usuario y contraseña.
```

```py
from flask import Flask

"""
Para prender el servidor 👇
En consola: export FLASK_APP=main.py
Después: flask run

También se puede ejecutar el programa con -> flask --app main run
main es el nombre con el cual se guardo el script.


En browser localhost:5000 para ver el resultado.
"""
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hola de nuevo che mundo!!!"

```

### Diferente ip y puerto

Para ejecutar el script de flask en diferente IP y en diferente puerto.

```bash
flask --app main run --host=127.0.0.1 -p 8000
```

### Debug Mode

Para ejecutar flask en modo **debug**

```bash
flask --app main --debug run --host=127.0.0.1
```

También se puede exportar la variable `FLASK_DEBUG`

```bash
export FLASK_DEBUG=1
#
#para comprobar si se guarfo la variable
echo $FLASK_DEBUG
```

Y ejecutar el script de flask

```bash
flask --app main run
```

### Obtener la ip de la maquina por medio del _request_

```bash
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    user_ip_request = request.remote_addr

    return f"la ip del request es {user_ip_request}"

```

### Ciclos de Request y Response

🔗 ↗️ [Gestionar Cookies en Flask](https://lineadecodigo.com/python/gestionar-cookies-flask/)

Request-Response: es uno de los métodos básicos que usan las computadoras para comunicarse entre sí, en el que la primera computadora envía una solicitud de algunos datos y la segunda responde a la solicitud.

Por lo general, hay una serie de intercambios de este tipo hasta que se envía el mensaje completo.

Por ejemplo: navegar por una página web es un ejemplo de comunicación de request-response.

Request-response se puede ver como una llamada telefónica, en la que se llama a alguien y responde a la llamada; es decir hacemos una petición y recibimos una respuesta.

👇 Scrip de flask para hacer la redirección al en la ruta raíz y al mismo tiempo setear una cookie con un valor en especifico y después hacer la redirección a la ruta `/hello`.

En la consola se muestra

```bash
127.0.0.1 - - [03/Nov/2022 14:29:47] "GET /hello HTTP/1.1" 200 -
127.0.0.1 - - [03/Nov/2022 14:29:57] "GET / HTTP/1.1" 302 -
127.0.0.1 - - [03/Nov/2022 14:29:57] "GET /hello HTTP/1.1" 200 -
```

```bash
from flask import Flask, request, make_response, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    user_ip = request.remote_addr

    # response = make_response(redirect("/hello"))
    
    # generar una url completa a la ruta asignada por el método
    response = make_response(redirect(url_for('hello')))
    
    response.set_cookie("user_ip", user_ip)

    return response

@app.route("/hello")
def hello():
    user_ip = request.cookies.get("user_ip")

    return f'Tu dirección IP, (después de haberla obtenida con una cookie 🍪) es {user_ip}'
```

### Templates con Jinja 2

Un template es un archivo `.html` que permite renderiar información estática y dinámica, para este caso podríamos pasar la información de la ip del usuario directamente al HTML, en lugar de regresar la como una cadena de texto.

1. Crear un nuevo directorio llamado `templates`, y crear un archivo html `hello.html` e importa de la clase Flask el modulo `render_template`
2. En la ruta hello, donde ahora en vez de retornar una cadena, retornamos el template: `hello.html`
3. También enviamos la `user_ip`, y dentro del html, colocamos doble corchete, para indicar es una variable

```bash
from flask import Flask, request, make_response, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def index():
    user_ip = request.remote_addr

    # response = make_response(redirect("/hello"))

    # generar una url completa a la ruta asignada por el método
    response = make_response(redirect(url_for("hello")))

    response.set_cookie("user_ip", user_ip)

    return response


@app.route("/hello")
def hello():
    user_ip = request.cookies.get("user_ip")

    return render_template("hello.html", user_ip=user_ip)
```

### Estructuras de control

Iteración: es la repetición de un segmento de código dentro de un programa de computadora. Puede usarse tanto como un término genérico (como sinónimo de repetición), así como para describir una forma específica de repetición con un estado mutable.

Un ejemplo de iteración sería el siguiente:

```python
{% for key, segment in segment_details.items() %}
        <tr>
                <td>{{ key }}td>
                <td>{{ segment }}td>
        tr>
{% endfor %}  
```

En este ejemplo estamos iterando por cada segment_details.items() para mostrar los campos en una tabla  
`{{ key }} {{ segment }}`  
de esta forma dependiendo de cuantos segment_details.items() haya se repetirá el código.

```bash
from flask import Flask, request, make_response, redirect, url_for, render_template

app = Flask(__name__)

todos = ["todo 1", "todo 2", "todo 3"]

@app.route("/")
def index():
    user_ip = request.remote_addr
    # response = make_response(redirect("/hello"))

    # generar una url completa a la ruta asignada por el método
    response = make_response(redirect(url_for("hello")))

    response.set_cookie("user_ip", user_ip)

    return response


@app.route("/hello")
def hello():
    user_ip = request.cookies.get("user_ip")
    context = {
        "user_ip": user_ip,
        "todos": todos
    }

    return render_template("hello.html", **context)
```

```html
<main>
    {% if user_ip %}
        <h1>Tu dirección IP, (después de haberla obtenida con una cookie 🍪) es {{ user_ip }}</h1>  
    {% else %}
        <h2><a href="{{ url_for("index") }}">Ir al inicio.</a></h2>
    {% endif %}
    <ul>
        {% for todo in todos %}
            <li>{{ todo }}</li>
        {% endfor %}
    </ul>
</main>
```

### Herencia de templates

**Macro**: son un conjunto de comandos que se invocan con una palabra clave, opcionalmente seguidas de parámetros que se utilizan como código literal. Los Macros son manejados por el compilador y no por el ejecutable compilado.

Los macros facilitan la actualización y mantenimiento de las aplicaciones debido a que su re-utilización minimiza la cantidad de código escrito necesario para escribir un programa.

En este ejemplo nuestra macro se vería de la siguiente manera:

```py
{% macro nav_link(endpoint, text) %}
    {% if request.endpoint.endswith(endpoint) %}
        <li class="active"><a href="{{ url_for(endpoint) }}">{{text}}a>li>
    {% else %}
        <li><a href="{{ url_for(endpoint) }}">{{text}}a>li>
    {% endif %}
{% endmacro %}
```

Un ejemplo de uso de macros en Flask:

```py
{% from "macros.html" import nav_link with context %}

<html lang="en">
    <head>
    {% block head %}
        <title>My applicationtitle>
    {% endblock %}
    head>
    <body>
        <ul class="nav-list">
            {{ nav_link('home', 'Home') }}
            {{ nav_link('about', 'About') }}
            {{ nav_link('contact', 'Get in touch') }}
        ul>
    {% block body %}
    {% endblock %}
    body>
html>
```

Como podemos observar en la primera línea estamos llamando a macros.html que contiene todos nuestros macros, pero queremos uno en específico así que escribimos import nav_link para traer el macro deseado y lo renderizamos de esta manera en nuestro menú `{{ nav_link('home', 'Home') }}`.

Archivo `base.html`

```py
    <main>
      {% block content %}
      {% endblock content %}
    </main>
```

Archivo `macros.html`

```py
{% macro render_todo(todo) %}
    <li>Descripción: {{ todo }}</li>
{% endmacro  %}
```

Archivo `hello.html`

```py
{% extends 'base.html' %}
{% import "macros.html" as macros %}
{% block title %} {{ super() }}
    Bienvenido 👋
{% endblock title %}

{% block content %}
    {% if user_ip %}
            <h1>Tu dirección IP, (después de haberla obtenida con una cookie 🍪) es {{ user_ip }}</h1>  
        {% else %}
            <h2><a href="{{ url_for("index") }}">Ir al inicio.</a></h2>
        {% endif %}
        <ul>
            {% for todo in todos %}
                {{ macros.render_todo(todo) }}
            {% endfor %}
        </ul>
{% endblock content %}
```

En el archivo `base.html` en el bloque `{% block content %} {% endblock content %}` se va a insertar todo lo que esta en el archivo `hello.html` al momento de hacer el render de los templates.

### Configurar paginas de error

Códigos de error:  
**100**: no son errores sino mensajes informativos. Como usuario nunca los verás, sino que entre bambalinas indica que la petición se ha recibido y se continúa el proceso.

**200**: estos códigos también indican que todo ha ido correctamente. La petición se ha recibido, se ha procesado y se ha devuelto satisfactoriamente. Por tanto, nunca los verás en tu navegador, pues significan que todo ha ido bien.

**300**: están relacionados con redirecciones. Los servidores usan estos códigos para indicar al navegador que la página o recurso que han pedido se ha movido de sitio. Como usuario, no verás estos códigos, aunque gracias a ellos una página te podría redirigir automáticamente a otra.

**400**: corresponden a errores del cliente y con frecuencia sí los verás. Es el caso del conocido error 404, que aparece cuando la página que has intentado buscar no existe. Es, por tanto, un error del cliente (la dirección web estaba mal).

**500**: mientras que los códigos de estado 400 implican errores por parte del cliente (es decir, de parte tuya, tu navegador o tu conexión), los errores 500 son errores desde la parte del servidor. Es posible que el servidor tenga algún problema temporal y no hay mucho que puedas hacer salvo probar de nuevo más tarde.


```py
```






