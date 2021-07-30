# Curso Avanzado de Django

- :link: [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)

  - :link: :octocat: [https://github.com/encode/django-rest-framework](https://github.com/encode/django-rest-framework)

- :link: :octocat: [http://www.cdrf.co/](http://www.cdrf.co/)

- :link: :video_camera: [Django Rest-framework Youtube 14 videos](https://www.youtube.com/playlist?list=PLgCYzUzKIBE9Pi8wtx8g55fExDAPXBsbV)

  - :link: :octocat: [mitchtabian / CodingWithMitchBlog-REST-API](https://github.com/mitchtabian/CodingWithMitchBlog-REST-API)

- :link: :video_camera: [Build an API with Django // Part 1 to 4](https://www.youtube.com/watch?v=RPsDhoWY_kc&list=PLLRM7ROnmA9HzbIXYN6D3wOZ0wUrqNs_d)
  - :link: :octocat: [justdjango / drf-api](https://github.com/justdjango/drf-api)

:link: :octocat: [circles.csv](https://gist.github.com/pablotrinidad/93ee462e0ee761bd505f0a2fed3d1c8c)

## 2. Cimientos

### 1. Arquitectura de una aplicación

El objetivo de este curso es convertirte en un Backend profesional que usa Django como su herramienta profesional.

- El Backend consiste en:
  - Servidor
  - Aplicación
  - Base de Datos

Un Backend developer es un diseñador, su trabajo consiste un 90% en leer, diseñar, analizar y planear. Un 10% en programar. Nuestro trabajo más importante es el diseño del sistema y las decisiones tomadas son más costosas y más difíciles de cambiar.

Web Services es la manera en que se implementan las arquitecturas orientadas a servicios, se crean bloques que son accesibles a través de la web, son independientes del lenguaje de programación.

    - SOAP: Tiene su propio estándar, conocido por utilizar XML.
    - REST: Representational State Transfer, el objetivo es que nuestras operaciones sean Stateless. REST depende mucho más del protocolo HTTP.
    - GraphQL: Es el más moderno, desarrollado por Facebook. Funciona más como un Query Language para las API, un lenguaje de consultas.

### 2. The Twelve-Factor App

- :link: [The twelve-factor app](https://12factor.net/)
- :link: [The twelve-factor/es/ app](https://12factor.net/es/)
- :link: [Twelve-factor app development on Google Cloud](https://cloud.google.com/solutions/twelve-factor-app-development-on-gcp)

* Algunos principios de Twelve Factor app

  - Formas declarativas de configuración
  - Un contrato claro con el OS
  - Listas para lanzar
  - Minimizar la diferencia entre entornos
  - Fácil de escalar

* **Codebase**: Se refiere a que nuestra app siempre debe estar trackeada por un sistema de control de versiones como Git, Mercurial, etc. Una sola fuente de verdad.
* **Dependencias**: Una 12 factor app nunca debe depender de la existencia implícita de nuestro OS, siempre se declaran explícitamente qué dependencias usa el proyecto y se encarga de que estas no se filtren. Dependency Isolation.
* **Configuración**: Acá nos referimos a algo que va a cambiar durante entornos.
* **Backing services**: Estos pueden ser conectados y desconectados a voluntad. Es cualquier servicio que nuestra aplicación puede consumir a través de la red como Base de Datos, Mensajería y Cola, Envío de Emails o Caché.
* **Build, release, run**: Separa estrictamente las etapas de construcción y las de ejecución. _Build_ es convertir nuestro código fuente en un paquete._Release_ es la etapa donde agregamos a nuestro paquete cosas de configuración como variables de entorno y _Run_ donde corremos la aplicación en el entorno correspondiente. Las etapas no se pueden mezclar.
* **Procesos**: En el caso más complejo tenemos muchos procesos corriendo como Celery y Redis, en esta parte los procesos son `stateless` y no comparten nada. Cualquier dato que necesite persistir en memoria o en disco duro tiene que almacenarse en un `backing services`,
* **Dev/prod parity**: Reducir la diferencia entre entornos para reducir tiempo entre deploys y las personas involucradas sean las mismas que puedan hacer el deploy
* **Admin processes**: Tratar los procesos administrativos como una cosa diferente, no deben estar con la app.

- :link: [Twelve-Factor App methodology](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology)

| #    | Factor              | Description                                                                                                         |
| ---- | ------------------- | ------------------------------------------------------------------------------------------------------------------- |
| I    | Codebase            | There should be exactly one codebase for a deployed service with the codebase being used for many deployments.      |
| II   | Dependencies        | All dependencies should be declared, with no implicit reliance on system tools or libraries.                        |
| III  | Config              | Configuration that varies between deployments should be stored in the environment.                                  |
| IV   | Backing services    | All backing services are treated as attached resources and attached and detached by the execution environment.      |
| V    | Build, release, run | The delivery pipeline should strictly consist of build, release, run.                                               |
| VI   | Processes           | Applications should be deployed as one or more stateless processes with persisted data stored on a backing service. |
| VII  | Port binding        | Self-contained services should make themselves available to other services by specified ports.                      |
| VIII | Concurrency         | Concurrency is advocated by scaling individual processes.                                                           |
| IX   | Disposability       | Fast startup and shutdown are advocated for a more robust and resilient system.                                     |
| X    | Dev/Prod parity     | All environments should be as similar as possible.                                                                  |
| XI   | Logs                | Applications should produce logs as event streams and leave the execution environment to aggregate.                 |
| XII  | Admin Processes     | Any needed admin tasks should be kept in source control and packaged with the application.                          |

### 3. Codebase: Settings modular

- :link: :octocat: [Codebase](https://github.com/macknilan/cride-platzi/commit/88c798f8f34cbe2cee5688f8259276e15ad13480)
- :link: :octocat: [joke2k/django-environ](https://github.com/joke2k/django-environ)
- :link: :octocat: [django-extensions/django-extensions ](https://github.com/django-extensions/django-extensions)
- :link: :octocat: [anymail/django-anymail](https://github.com/anymail/django-anymail)
- :link: :octocat: [jschneier/django-storages ](https://github.com/jschneier/django-storages)

### 4. Codebase: Dependencias y archivos de docker

:link: :octocat: []()

### 5. Codebase: Docker

:link: :octocat: [Cookiecutter Django list of commands](https://github.com/macknilan/Cuaderno/blob/master/Docker/Docker.md#cookiecutter-django-list-of-commands)

#### Docker básicos

```bash
$ docker images
$ docker container
$ docker volume
$ docker network
# PARA CADA UNO
ls
rm
prune
-a
-q
```

#### Docker imagenes

Listar todos las imagenes

```bash
docker images -a
```

#### Docker contenedores

Listar todos los contenedores

```bash
$ docker container ls -a
```

Detener todos los contenedores

```bash
$ docker container stop $(docker container ls -aq)
```

Detener y eliminar todos contenedores

```bash
$ docker container rm $(docker container ls -aq)
```

Elininar todos los contenedore detenidos, imagenes colgadas y networks no utilizadas

```bash
$ docker system prune
```

Eliminar todos los volumenes no utilizados

```bash
$ docker system prune --volumes
```

#### Algunos comandos de `docker-compose`

```bash
# COMPOSE_FILE
$ export COMPOSE_FILE=local.yml

$ docker-compose build
$ docker-compose up
$ docker-compose ps
$ docker-compose down
```

#### Docker-compose imagenes

```bash
# Para construir las imagenes
$ docker-compose -f local.yml build

# Para correr el stack
$ docker-compose -f local.yml up

# Para ver el estado de los procesos de Docker
$ docker-compose -f local.yml ps

# Para detener la ejecución
$ docker-compose -f local.yml down
```

#### Comandos de administración

La bandera `--rm` lo que hace es que crea un contenedor solo para el fin indicado y cuando acabe de ejecutarse el comando **mata el contenedor**

```bash
# Para correr comandos de Django usamos
docker-compose run --rm django COMMAND
#
# Por ejemplo para crear un super usuario
docker-compose run --rm django python manage.py createsuperuser
```

#### Habilitar debugger

```bash
# 1 Para correr el stack de contenedores
$ docker-compose -f local.yml up
```

```bash
# 2 Saber con que nombre esta el contenedor
$ docker-compose -f local.yml ps
```

```bash
# 3 MATAR EL DOCKER DJANGO
$ docker rm -f <ID>
```

```bash
# 4 DESPUES DE SACAR/MATAR EL DOCKER DE django PARA LEVANTAR LO DE NUEVO ES
$ docker-compose -f local.yml run --rm --service-ports django
# Hacer migraciones
$ docker-compose -f local.yml run --rm django python manage.py makemigrations
# Migrar a la BD
$ docker-compose -f local.yml run --rm django python manage.py migrate
# EJEMPLO PARA CREAR SUPER-USUARIO
$ docker-compose -f local.yml run --rm django python manage.py createsuperuser
# Cuando se presentan problemas con las migraciones y una opción es que se elimine el "volumen" de la BD donde se almacena la data tiene la terminación NOMBRE DEL PROYECTO_postgres_data
#Primero se tiene que detener la ejecucion de docker-compose
$ docker-compose -f local.yml down
# Mostrar los volunenes de docker
$ docker volume ls
# Eliminar el volimen NOMBRE DEL PROYECTO_postgres_data
$ docker volume rm NOMBRE DEL PROYECTO_postgres_data
```

### 6. Setups alternativos

- :link: :octocat: [cookiecutter/cookiecutter ](https://github.com/cookiecutter/cookiecutter)
- :link: :octocat: [pydanny/cookiecutter-django](https://github.com/pydanny/cookiecutter-django)
- :link: :octocat: 👀 🚨 [Add nginx to serving static files #2311](https://github.com/pydanny/cookiecutter-django/issues/2311)
- :link: :octocat: 👀 🚨 [nginx-le/nginx-le - Nginx with automatic let's encrypt (docker image)](https://github.com/nginx-le/nginx-le)

## 3. Modelos

### 6. Herencia de modelos

- :link: :octocat: [Abstract classes](https://github.com/macknilan/cride-platzi/commit/4fbcaa66286549c525f3b4d5fc5d769aa63429a3)
- :link: [djangoproject - Model inheritance](https://docs.djangoproject.com/en/3.1/topics/db/models/#model-inheritance)

**Abstract base classes**

> Abstract base classes are useful when you want to put some common information into a number of other models. You write your base class and put abstract=True in the Meta class. This model will then not be used to create any database table. Instead, when it is used as a base class for other models, its fields will be added to those of the child class.

- :link: [djangoproject - Model Meta options](https://docs.djangoproject.com/en/3.1/ref/models/options/#model-meta-options)
- :link: :octocat: [djangoproject - Model Meta options](https://docs.djangoproject.com/en/3.1/ref/models/options/)

La herencia de modelos puede ser útil porque podemos tener datos generales que pueden ser heredados por otras que no necesariamente tienen su propia tabla, porque queremos que haya herencia de múltiples tablas que se reflejan en la base de datos o porque queremos extender la funcionalidad de un modelo.

### 7. Proxy models

Los Proxys nos permiten extender la funcionalidad de un modelo sin crear una nueva tabla en la base de datos, la diferencia con los Abstract Models es que estas solo exponen un molde de atributos y las proxys extienden de una tabla ya existente.

### 8. App de usuarios

- :link: :octocat: [4/Model-package](https://github.com/macknilan/cride-platzi/commit/6b7b33c12794122c24dd6bad5d4646ddda3640eb)
- :link: [djangoproject - Extending the existing User model¶](https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#extending-the-existing-user-model)

### 9. Organizando modelos en un paquete de Django

- :link: :octocat: [4/Model-package](https://github.com/macknilan/cride-platzi/commit/6b7b33c12794122c24dd6bad5d4646ddda3640eb)
- :link: [djangoproject - Extending the existing User model](https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#extending-the-existing-user-model)
- :link: [djangoproject - AUTH_USER_MODEL¶](https://docs.djangoproject.com/en/3.1/ref/settings/#auth-user-model)

Deconstruir el modelo de Usuario en múltiples archivos dentro de un paquete

### 10. Creando el modelo de perfil de usuario

- :link: :octocat: [5/Profile-model](https://github.com/macknilan/cride-platzi/commit/fa8deb45c207562a8298189f0a44331541414f7d)
- :link: [djangoproject - Model field reference](https://docs.djangoproject.com/en/3.1/ref/models/fields/#module-django.db.models.fields)
- :link: [djangoproject - ForeignKey.on_delete](https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.ForeignKey.on_delete)

### 11. Solución del reto: arreglando la migración de users a user

- :link: :octocat: [6/Typo-models](https://github.com/macknilan/cride-platzi/commit/45976eb95d00f72ed26125d65235aefaeb951bb0)
- :link: [djangoproject - Squashing migrations¶](https://docs.djangoproject.com/en/3.1/topics/migrations/#more-advanced-migrations)

### 12. Aplicación y modelo de círculos

- :link: :octocat: [7/Circles-app-and-model](https://github.com/macknilan/cride-platzi/commit/2dc2646c6c05d37729cc273a322dabdee80546da)
- :link: [djangoproject - Model field reference](https://docs.djangoproject.com/en/3.1/ref/models/fields/)
- :link: [Archivo circles.csv](https://github.com/macknilan/cride-platzi/blob/2dc2646c6c05d37729cc273a322dabdee80546da/circles.csv)

Django Integer Field types:

- **IntegerField**: Puede almacenar valores enteres desde -2147483648 hasta 2147483647.
- **PositiveIntegerField**: Como un IntegerField, pero debe ser positivo o cero . Puede almacenar valores desde 0 hasta 2147483647. El valor 0 es aceptado por razones de compatibilidad hacia atrás.
- **PositiveSmallIntegerField**: Como un PositiveIntegerField, pero solo permite valores hasta un cierto limite (dependiente de la base de datos). Puede almacenar valores desde 0 hasta 32767 en todas las bases de datos compatibles con Django.
- **SmallIntegerField**: Como un IntegerField, pero solo permite valores bajo un determinado limite (dependiente de la base de datos). Puede almacenar valores desde -32768 hasta 32767 en todas las bases de datos compatibles con Django.
- **BigIntegerField**: Un entero de 64 bits, muy parecido a IntegerField, excepto que se garantiza que se ajustan a los números desde -9223372036854775808 hasta 9223372036854775807. El widget predeterminado en un formulario para este campo es un TextInput.

### 13. Migraciones y admin de círculos

- :link: :octocat: [8/Circles-admin - Circles admin and migrations applied](https://github.com/macknilan/cride-platzi/commit/e86be73b23afa971d208139db6e992b38d6ecfde)
- :link: :octocat: [Github Gist](https://gist.github.com/pablotrinidad/93ee462e0ee761bd505f0a2fed3d1c8c)
- :link: [django-extensions ](https://django-extensions.readthedocs.io/en/latest/)

```py
def import_circle_to_csv(path: str):
    import csv
    with open(path) as csv_file:
        circles = [Circle(**attrs) for attrs in csv.DictReader(csv_file)]

    Circle.objects.bulk_create(circles)
    for circle in circles:
        print(f'circle saved success: {circle}')

```

## 4. Introducción a Django REST Framework

### 14. Aprende cómo construir tu propio API con Django Rest Framework

- :link: :octocat: [9/Live-without-DRF](https://github.com/macknilan/cride-platzi/commit/d18186222f4839bb85a4ac10071aa0c217b422f6)
- :link: [Request and response objects](https://docs.djangoproject.com/en/3.1/ref/request-response/)
- :link: [HTTPie—aitch-tee-tee-pie—is a user-friendly command-line HTTP client for the API era. It comes with JSON support, syntax highlighting, persistent sessions, wget-like downloads, plugins, and more. ](https://httpie.org/)

```bash
# Debian, Ubuntu, etc.
apt install httpie
```

| HTTP method | Action            | Description                 |
| ----------- | ----------------- | --------------------------- |
| GET         | .list()           | Get a list of countries.    |
| GET         | .retrieve()       | Get a single country.       |
| POST        | .create()         | Create a new country.       |
| PUT         | .update()         | Update a country.           |
| PATCH       | .partial_update() | Partially update a country. |
| DELETE      | .destroy()        | Delete a country.           |

_Django Rest Framework_ es una librería que cuenta con muchas herramientas para poder crear nuestras **APIs** con ayuda de Django. Tiene algunos beneficios como políticas de autenticación incluyendo packetes de _OAuth1_ y _OAuth2_, _serialización de datos que soporta ORM_ (Object-relational Mapping), puedes hacer uso de las populares Class Based Views y Function Based Views si necesitas algo más personalizado. Empresas como Mozilla, Red Hat, Heroku y Eventbrit lo utilizan.

### 15. Vistas, URLs y Parsers de DRF

- :link: :octocat: [10/Intro-to-DRF](https://github.com/macknilan/cride-platzi/commit/50e7443ad80ce3ca8f52efb1c4d0392e68653508)
- :link: :octocat: [encode/django-rest-framework](https://github.com/encode/django-rest-framework)
- :link: [Django REST Framework](https://www.django-rest-framework.org)
- :link: [DRF - Class-based Views( @api_view()) ](https://www.django-rest-framework.org/api-guide/views/)
- :link: [DRF - Request ](https://www.django-rest-framework.org/api-guide/requests/)

👀❗️

- **ViewSet**: Cuando usamos la mayoria de operaciones crud en un modelo
- **Generics**: Cuando solo desee permitir algunas operaciones en un modelo
- **ApiView** :Cuando desee personalizar completamente las operaciones de un modelo.

👀❗️

### 16. Serializers

- :link: :octocat: [11/Intro-to-serializers](https://github.com/macknilan/cride-platzi/commit/1db127eb100eef514d8b2e244623a10aedf0b87d)
- :link: [DRF - Serializers](https://www.django-rest-framework.org/api-guide/serializers/)
- :link: [DRF - Serializer fields](https://www.django-rest-framework.org/api-guide/fields/)
- :link: [DRF - Serializers( .is_valid() )](https://www.django-rest-framework.org/api-guide/serializers/#validation)
- :link: [DRF - Saving instances](https://www.django-rest-framework.org/api-guide/serializers/#saving-instances)

> Los serializers son contenedores que nos permiten tomar tipos de datos complejos, convertirlos en datos nativos de python para después poderlos usar como JSON o XML. Son contenedores que amoldan datos para que cumplan con las condiciones de los serializers y sean llevados a un tipo de estos y después estos puedan ser transformados en otra cosa.

### 17. Buenas prácticas para el diseño de un API REST

- :notebook_with_decorative_cover: [api-design-ebook-2012-03.pdf](docs/api-design-ebook-2012-03.pdf)
- :link: [Facebook Graph API](https://developers.facebook.com/docs/graph-api/)
- :notebook_with_decorative_cover: [APIs_design.pdf](docs/APIs_design.pdf)
- :link: [List of HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

Uno de los prerequisitos para crear APIs es conocer el protocolo HTTP. Verbos, métodos, estados y las cabeceras.

Van a estar diseñando una interfaz para programadores para que otros programadores puedan interactuar, nos olvidaremos de los templates para que un equipo de Frontend se encargue de eso. Debemos tener la perspectiva de un usuario de API y no la de un diseñador de API.

El objetivo es algo que siempre se deben preguntar qué problema deben de resolverle al usuario final nuestra API. El éxito de nuestra API se mide por qué tan rápido nuestros compañeros pueden usarla.

**REST**: Es una serie de principio de cómo diseñar una web service. Un estilo de arquitectura.

- HTTP Status Code:

  - 201: Creado
  - 304: No modificado
  - 404: No encontrado
  - 401: No autorizado
  - 403: Prohibido o restringido.

- Pro tips:
  - SSL
  - Caché
  - Valida
  - CSRF o Cross-Site Request Forgery
  - Limita los requests
  - Complementa tu API con un SDK

### 18. Request, response, renderers y parsers

- :link: [DRF - Requests](https://www.django-rest-framework.org/api-guide/requests/)
- :link: [DRF - Responses](https://www.django-rest-framework.org/api-guide/responses/)
- :link: [DRF - Parsers](https://www.django-rest-framework.org/api-guide/parsers/)
- :link: [DRF - Renders](https://www.django-rest-framework.org/api-guide/renderers/)
- :link: [HTTP Status Codes](https://httpstatuses.com/)

Dejar desahabilitado :link: [BrowsableAPIRenderer](https://www.django-rest-framework.org/api-guide/renderers/#browsableapirenderer) que es _enders data into HTML for the Browsable API_.

Lo que hace es poner una interfas gráfica para que se muestre la API en una _URL_ del proyesto que muy pocas ocasiones es utilizada por los clientes.

Se recomienda no dejar habilitado esta opción.

## 5. Real DRF

### 19. Autenticación y tipos de autenticación

- :link: [DRF - Authentication](https://www.django-rest-framework.org/api-guide/authentication/)
- :link: [DRF - Permissions](https://www.django-rest-framework.org/api-guide/permissions/)
- :link: [JSON Web Tokens](https://jwt.io/)
- :link: [Basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication)
- :link: [OAuth](https://en.wikipedia.org/wiki/OAuth)

- :link: :octocat: [SimpleJWT/django-rest-framework-simplejwt ](https://github.com/SimpleJWT/django-rest-framework-simplejwt)
- :link: [Docs - Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

La autenticación es la parte de asociar una petición a un usuario y después al objeto request se le asigna dos propiedades como `request.user` y`request.auth`

- Tipos de autenticación
  1. Basic
  2. Token
  3. Session
  4. Oauth
  5. Json Web Token JWT (EXTRA)

### 20. APIView

- :link: :octocat: [13/APIView](https://github.com/macknilan/cride-platzi/commit/f5ad39d16f8d3e014b8d9927347d01ac2c4a9ac5)
- :link: [APIView](https://www.django-rest-framework.org/api-guide/views/)
- :link: [Status Codes](https://www.django-rest-framework.org/api-guide/status-codes/)
- :link: [Validation - Object-level validation](https://www.django-rest-framework.org/api-guide/serializers/#validation)

### 21. Creando el token de autorización

:link: :octocat: [14/Token-creation](https://github.com/macknilan/cride-platzi/commit/62413099b80cfc617d0150382f1d837435bf08da)

- :link: [TokenAuthentication](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)

Todos los serializers comparten contexto, como los templates, y es un atributo de clase y es un diccionario `self.context['']`

### 22. User sign up

- :link: []()

### 23. Limitar login a usuarios con cuenta verificada

:link: :octocat: [15/User-signup](https://github.com/macknilan/cride-platzi/blob/15/User-signup/cride/users/serializers/users.py)

### 24. Configurar envío de email

:link: :octocat: [16/Login-restricted](https://github.com/macknilan/cride-platzi/blob/16/Login-restricted/cride/users/serializers/users.py)

### 25. Instalar PyJWT y generar tokens

- :link: :octocat: [cride-platzi/cride/users/views/users.py](https://github.com/macknilan/cride-platzi/blob/17/Confirmation-email/cride/users/serializers/users.py)
- :link: :octocat: [Branch 18/JWT](https://github.com/macknilan/cride-platzi/commit/75f35ad6b7d96ff3489fa4708a7b8c44d82e24f4)
- :link: :octocat: [anymail/django-anymail](https://github.com/anymail/django-anymail)
- :link: [Sending email](https://docs.djangoproject.com/en/3.0/topics/email/)
- :link: [render_to_string](https://docs.djangoproject.com/en/3.0/topics/templates/#django.template.loader.render_to_string)
- :link: [JSON Web Token implementation in Python](https://github.com/jpadilla/pyjwt)
- :link: [:house: PyJWT](https://pyjwt.readthedocs.io/en/latest/)
- :link: :octocat: [django - class EmailMessage:](https://docs.djangoproject.com/en/3.0/_modules/django/core/mail/message/#EmailMessage)

### 26. Verificar cuenta usando JWT 👀 🚨

- :link: :octocat: [Branch 19/JWT-Verification](https://github.com/macknilan/cride-platzi/commit/61267700d183e5de803db3bda08d58dccda5477b)
- :link: [DRF saving-instances](https://www.django-rest-framework.org/api-guide/serializers/#saving-instances)
- :link: :octocat: [pyjwt/jwt/exceptions.py](https://github.com/jpadilla/pyjwt/blob/master/jwt/exceptions.py)
- :link: :octocat: [PyJWT classes Exceptions](https://github.com/jpadilla/pyjwt/blob/master/jwt/exceptions.py)

### 27. Actualizar modelo de circle (membership)

- :link: [Django - Extra fields on many-to-many relationships](https://docs.djangoproject.com/en/3.0/topics/db/models/#extra-fields-on-many-to-many-relationships)

* :link: :octocat: [20/Membership-model](https://github.com/macknilan/cride-platzi/commit/68a57213aaf95c9ffb7fd8f33f9cd9ebe3a7321c)

### 28. Crear CircleViewSet 👀 🚨

- :link: :octocat: [21/CircleViewSet](https://github.com/macknilan/cride-platzi/commit/56ea57dcdf6e198e57cc86c6eb33b18e64865f66)
- :link: :octocat: [django-rest-framework/rest_framework/viewsets.py](https://github.com/encode/django-rest-framework/blob/master/rest_framework/viewsets.py)
- :link: [django Rest Framework - ViewSets](https://www.django-rest-framework.org/api-guide/viewsets/)
- :link: [django Rest Framework - Generic views](https://www.django-rest-framework.org/api-guide/generic-views/)
- :link: :octocat: [django-rest-framework/rest_framework/generics.py](https://github.com/encode/django-rest-framework/blob/master/rest_framework/generics.py)
- :link: :octocat: [django-rest-framework/rest_framework/mixins.py](https://github.com/encode/django-rest-framework/blob/master/rest_framework/mixins.py)

> Mixin: Una clase que expone metodos y estos metodos pueden ser llamados por otras clases eventualmente.

> ViewSet: Se encarga de todas las acciones relacionadas con un modelo CRUD dentro del la misma clase.

### 29. Añadiendo autorización y paginación

- :link: :octocat: [22/Pagination-Auth](https://github.com/macknilan/cride-platzi/commit/424aebb22ca3f29977da069646db8961c5bab00c)
- :link: [Django Rest Framework - Pagination](https://www.django-rest-framework.org/api-guide/pagination/#limitoffsetpagination)
- :link: [Django REst Framework - Authentication](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)
- :link: [Django REst Framework - Permissions(EN LA VISTA)](https://www.django-rest-framework.org/api-guide/permissions/#isauthenticated)

Como convenciónn, cuendo se borra un elemento no se regresa el elemento eliminado, solo se regresa el status `204 No Content`

Las peticiones son `stateless`

### 30. Creación de circulos

- :link: :octocat: [23/Circle-creation](https://github.com/macknilan/cride-platzi/commit/ec81778d09017e0dde40c2dc05fae1514d096bac)
- :link: [ModelViewSet -> CreateModelMixin -> def perform_create(self, serializer):](http://www.cdrf.co/3.9/rest_framework.mixins/CreateModelMixin.html)

### 31. Update de círculo, custom permissions y DRF Mixins

- :link: :octocat: [24/Circle-update](https://github.com/macknilan/cride-platzi/commit/412a6b3b1e4ab8d91fa2e6f5f55f8cef15649b58)
- :link: [DRF - Introspecting ViewSet actions](https://www.django-rest-framework.org/api-guide/viewsets/#introspecting-viewset-actions)
- :link: [DRF - Permissions](https://www.django-rest-framework.org/api-guide/permissions/)

### 32. Migración de vistas de usuarios a ViewSets 👀 🚨

- :link: :octocat: [25/Viewset-actions](https://github.com/macknilan/cride-platzi/commit/e01010d90ae1ff68aa679492ec6346f1102a7001)
- :link: [ViewSets](https://www.django-rest-framework.org/api-guide/viewsets/)
- :link: [ViewSets - Marking extra actions for routing(actions)](https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing)

`detail=True` Son aquellas acciones que parten a traves de un `id/pk`. Por ejemplo algún CRUD sobre un item

`detail=False` Son aquellas acciones que pueden ser como reportes(listar), hacer login, sign-up, por ejemplo.

### 33. Detalle de usuario

- :link: :octocat: [26/User-detail](https://github.com/macknilan/cride-platzi/commit/af5a72490a06a7028b62a377ba5451c758955f74)
- :link: [DRF - Permissions](https://www.django-rest-framework.org/api-guide/permissions/)
- :link: [DjangoProject - ManyToManyField.through_fields](https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ManyToManyField.through_fields)

### 34. Update profile data

- :link: :octocat: [27/Update-profile](https://github.com/macknilan/cride-platzi/commit/2c39b7f40402e9ef77f40a748f87bff36fe382e4)

### 35. List members - Recursos anidado

- :link: :octocat: [28/Circle-members](https://github.com/macknilan/cride-platzi/commit/b6cdced0b576d7ae87d095ab8db417f711ea1226)
- :link: [DRF - Serializer relations](https://www.django-rest-framework.org/api-guide/relations/)

### 36. Retrieve destroy member

- :link: :octocat: [29/Retrieve-destroy-member](https://github.com/macknilan/cride-platzi/commit/507521e99d069165794f0b30aa4e335f02f06226)
- :link: [CDRF - class DestroyModelMixin](http://www.cdrf.co/3.9/rest_framework.mixins/DestroyModelMixin.html)

### 37. Modelo de invitaciones y manager

- :link: :octocat: [30/Invitation-manager](https://github.com/macknilan/cride-platzi/commit/3302902e1303e0fe9bf7e648f6250f15ac6731ac)
- :link: [Django project - Managers](https://docs.djangoproject.com/en/3.0/topics/db/managers/)

### 38. Obtener invitaciones de un miembro

- :link: :octocat: [31/Member-invitations](https://github.com/macknilan/cride-platzi/commit/ed4cef4def7a29b1a1ffaed183d599d42f8d683d#diff-77d02c60fa749b2d6439aef9799c8cf5)

### 39. Unirse a grupo

- :link: :octocat: [32/Join-Circle](https://github.com/macknilan/cride-platzi/commit/bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29)

### 40. Filtrado

- :link: :octocat: [C33 - Filter](https://github.com/macknilan/cride-platzi/commit/0257eb0426b03a55826bff8d62c152640c330f8d)
- :link: :octocat: [DRF - Filtering](https://www.django-rest-framework.org/api-guide/filtering/)

### 41. App de rides y modelos 👀 🚨

- Aplicación de rides
  - Modelo Rides
  - Quien ofrece el ride
  - En que circulo lo ofrece
  - Lugar de salida
  - Horario de salida
  - Lugar de llegada
  - Hora de llegada
  - Asientos disponibles
  - Comentarios extra
  - Posibilidad de guardar los pasajeros que se van sumando
  - Activar y desactivar ride

* :link: :octocat: [C34 - App Rides & Models](https://github.com/macknilan/cride-platzi/commit/a13b3d5527ef2c949f69a5c1af4bbd3532dfaa28)

### 42. Implementar la publicación de un ride

- :link: :octocat: [C35 - Implementar la publicación de un ride](https://github.com/macknilan/cride-platzi/commit/bc2ddd3416bc672b663992128a8e80bb3a15c61e)

### 43. Validación de campos de un serializer 👀 🚨

- :link: :octocat: [C36 - Validación de campos de un serializer (Validate fields in serializer)](https://github.com/macknilan/cride-platzi/commit/ebe0df18c5e1513589f26de2e8af163653598021)
- :link: [DRF - class GenericViewSet](http://www.cdrf.co/3.9/rest_framework.viewsets/GenericViewSet.html)

### 44. Listado de rides

- :link: :octocat: [C37 - Listing Rides(Listado de rides)](https://github.com/macknilan/cride-platzi/commit/bdb126ca0672d6666bbd289f165c39f6d7f21765)
- :link: [DRF - class GenericViewSet](http://www.cdrf.co/3.9/rest_framework.viewsets/GenericViewSet.html)

### 45. Editar un ride

- :link: :octocat: [C38 - Edit Ride(Editar un Ride)](https://github.com/macknilan/cride-platzi/commit/61d0e5e94063665411bf3578f63088e2b2aa76c5)
- :link: [DRF](https://www.django-rest-framework.org/api-guide/relations/#stringrelatedfield)
- :link: [class BaseSerializer - def update](http://www.cdrf.co/3.9/rest_framework.serializers/BaseSerializer.html)

### 46. Unirse a viaje

- :link: :octocat: [C39 - Join a Ride(Unirse a un Ride)](https://github.com/macknilan/cride-platzi/commit/cbbd4a25c49328696651bcf6c542907d5359257c)
- :link: [djangop roject - Many-to-many relationships](https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_many/)
- :link: [Django REST framework - Partial updates](https://www.django-rest-framework.org/api-guide/serializers/#partial-updates)

### 47. Terminar viaje

- :link: :octocat: [C40 - Finish ride(Terminar viaje)](https://github.com/macknilan/cride-platzi/commit/920c585287cdeb71685a8ea7e438a3ddbe65a665)

### 48. Calificar viaje 👀 🚨

- :link: :octocat: [C41 - Calificar ride](https://github.com/macknilan/cride-platzi/commit/78b0fba1144ea7710e83d62d7b051988a9e0108a)

## 6. Tareas asíncronas

### 49. Creando tarea asíncrona

- :link: :octocat: [C42 - Async task(Tareas asincronas)](https://github.com/macknilan/cride-platzi/commit/4b890a2f491b2a2acdf3068d231da6977d4050c2)
- :link: :octocat: [Celery - Calling Tasks](https://docs.celeryproject.org/en/latest/userguide/calling.html#basics)

### 50. Creando tarea periódica

- :link: :octocat: [C25 - Scheduled task (Creando tarea periódica)](https://github.com/macknilan/cride-platzi/commit/d17041ecc1f3351311e26e480b1884d1728659db)

## 7. Testing

### 51. Python unittest y Django TestCase

- :link: :octocat: [C46 - Testing with django(Python unittest y Django TestCase)](https://github.com/macknilan/cride-platzi/commit/fdbc4952b4c8d417506df75703fd32d3a03b2a11)
- :link: [Writing and running tests](https://docs.djangoproject.com/en/3.0/topics/testing/overview/)
- :link: [unittest — Unit testing framework](https://docs.python.org/3.7/library/unittest.html)
- :link: [25.3. unittest — Unit testing framework](https://docs.python.org/2/library/unittest.html)

Unit Tests o Pruebas Unitarias estamos hablando de pruebas que prueban módulos particulares que por si solos no reflejan una funcionalidad compleja.

Las pruebas de integración son módulos que se componen de múltiples partes, unidades.

### 52. DRF APITestCase

- :link: :octocat: [C45 - DRF APITestCase](https://github.com/macknilan/cride-platzi/commit/3ae147aeec997c8c7b202e19f81d224e651cf3d2)
- :link: [DRF - Testing](https://www.django-rest-framework.org/api-guide/testing/)

## 8. Django Admin

### 53. Admin actions: Modificar datos de un query

- :link: :octocat: [46 - Admin actions: updating query(Admin actions: Modificar datos de un query)](https://github.com/macknilan/cride-platzi/commit/ff7c27e679c9598e21de0661952f8f3fd42867dc)
- :link: [djangoproject - Admin actions](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/actions/)

### 54. Admin actions: Regresando una respuesta HTTP

- :link: [djangoproject - Outputting CSV with Django](https://docs.djangoproject.com/en/3.1/howto/outputting-csv/)

Los Admin actions son funcionalidades que nos permiten agregar cambios a un queryset de un conjuto de datos del admin.

Ahora que ya sabes cómo construir una API, una recomendación es no extender el admin de Django más allá de sus capacidades.

`cride/circles/admin.py`

```py
"""Circles admin."""

# Django
from django.contrib import admin
from django.http import HttpResponse

# Model
from cride.circles.models import Circle
from cride.rides.models import Ride

# Utilities
import csv
from django.utils import timezone
from datetime import datetime, timedelta


@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    """Circle admin."""

    list_display = (
        'slug_name',
        'name',
        'is_public',
        'verified',
        'is_limited',
        'members_limit'
    )
    search_fields = ('slug_name', 'name')
    list_filter = (
        'is_public',
        'verified',
        'is_limited'
    )

    actions = ['make_verified', 'make_unverified', 'download_todays_rides']

    def make_verified(self, request, queryset):
        """Make circles verified."""
        queryset.update(verified=True)
    make_verified.short_description = 'Make selected circles verified'

    def make_unverified(self, request, queryset):
        """Make circles unverified."""
        queryset.update(verified=False)
    make_unverified.short_description = 'Make selected circles unverified'

    def download_todays_rides(self, request, queryset):
        """Return today's rides."""
        now = timezone.now()
        start = datetime(now.year, now.month, now.day, 0, 0, 0)
        end = start + timedelta(days=1)
        rides = Ride.objects.filter(
            offered_in__in=queryset.values_list('id'),
            departure_date__gte=start,
            departure_date__lte=end
        ).order_by('departure_date')

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="rides.csv"'
        writer = csv.writer(response)
        writer.writerow([
            'id',
            'passengers',
            'departure_location',
            'departure_date',
            'arrival_location',
            'arrival_date',
            'rating',
        ])
        for ride in rides:
            writer.writerow([
                ride.pk,
                ride.passengers.count(),
                ride.departure_location,
                str(ride.departure_date),
                ride.arrival_location,
                str(ride.arrival_date),
                ride.rating,
            ])

        return response
    download_todays_rides.short_description = 'Download todays rides'
```

## 9. Deployment

### 55. Instalación de la aplicación 👀 🚨

- :link: :octocat: [C47 - AWS Keys removed from production settings file(Instalación de la aplicación)](https://github.com/macknilan/cride-platzi/commit/b6905d9ff2fdacc4f240dbe9f9bc884805ebd04a)
- :link: 🐋 [Install Docker Engine](https://docs.docker.com/engine/install/)
- :link: 🐋 [Install Docker Compose](https://docs.docker.com/compose/install/)
- :link: 📓 [Deployment with Docker](https://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html)

### 56. Configuración del dominio en Mailgun y del Bucket en Amazon S3

- :link: :octocat: [Deploy - Configuración del dominio en Mailgun y del Bucket en Amazon S3](https://github.com/macknilan/cride-platzi/commit/36b5e28361d44dc13c2bae9f36a9fe574040e4df)
- :link: ✉️ [Mailgun](https://www.mailgun.com/)

### 57. Configuración final de Docker Container usando Supervisor 👀 🚨

Configurar un dominio y un certificado SSL de lets encrypt

### 58. Tutorial de despliegue de la aplicación

- :link: :octocat: []()

### 59. Futuros pasos y cierre del curso
