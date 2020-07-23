
# Curso Avanzado de Django

- :link: [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)
    + :link: :octocat: [https://github.com/encode/django-rest-framework](https://github.com/encode/django-rest-framework)

- :link: :octocat: [http://www.cdrf.co/](http://www.cdrf.co/)

- :link: :video_camera: [Django Rest-framework Youtube 14 videos](https://www.youtube.com/playlist?list=PLgCYzUzKIBE9Pi8wtx8g55fExDAPXBsbV)
    + :link: :octocat: [mitchtabian / CodingWithMitchBlog-REST-API](https://github.com/mitchtabian/CodingWithMitchBlog-REST-API)

- :link: :video_camera: [Build an API with Django // Part 1 to 4](https://www.youtube.com/watch?v=RPsDhoWY_kc&list=PLLRM7ROnmA9HzbIXYN6D3wOZ0wUrqNs_d)
    + :link: :octocat: [justdjango / drf-api](https://github.com/justdjango/drf-api)

:link: :octocat: [circles.csv](https://gist.github.com/pablotrinidad/93ee462e0ee761bd505f0a2fed3d1c8c)

## 2. Cimientos
### 1. Arquitectura de una aplicación

### 2. The Twelve-Factor App

### 3. Codebase: Settings modular

### 4. Codebase: Dependencias y archivos de docker

### 5. Codebase: Docker

### 6. Setups alternativos

## 3. Modelos
### 6. Herencia de modelos

### 7. Proxy models

### 8. App de usuarios

### 9. Organizando modelos en un paquete de Django

### 10. Creando el modelo de perfil de usuario

### 11. Solución del reto: arreglando la migración de users a user

### 12. Aplicación y modelo de círculos

### 13. Migraciones y admin de círculos

## 4. Introducción a Django REST Framework
### 14. Aprende cómo construir tu propio API con Django Rest Framework

### 15. Vistas, URLs y Parsers de DRF

### 16. Serializers

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
    + 201: Creado
    + 304: No modificado
    + 404: No encontrado
    + 401: No autorizado
    + 403: Prohibido o restringido.

- Pro tips:
    + SSL
    + Caché
    + Valida
    + CSRF o Cross-Site Request Forgery
    + Limita los requests
    + Complementa tu API con un SDK

### 18. Request, response, renderers y parsers

- :link: [DRF Requests](https://www.django-rest-framework.org/api-guide/requests/)
- :link: [DRF Responses](https://www.django-rest-framework.org/api-guide/responses/)


## 5. Real DRF
### 19. Autenticación y tipos de autenticación
- :link: [DRF Authentication](https://www.django-rest-framework.org/api-guide/authentication/)
- :link: [DRF Permissions](https://www.django-rest-framework.org/api-guide/permissions/)
- :link: [JSON Web Tokens](https://jwt.io/)
- :link: [Basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication)
- :link: [OAuth](https://en.wikipedia.org/wiki/OAuth)

### 20. APIView

- :link: [APIView](https://www.django-rest-framework.org/api-guide/views/)
- :link: [Status Codes](https://www.django-rest-framework.org/api-guide/status-codes/)
- :link: [Validation - Object-level validation](https://www.django-rest-framework.org/api-guide/serializers/#validation)


### 21. Creando el token de autorización

- :link: [TokenAuthentication](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)


### 22. User sign up
- :link: []()


### 23. Limitar login a usuarios con cuenta verificada
:link: :octocat: [cride-platzi/cride/users/views/users.py](https://github.com/macknilan/cride-platzi/blob/15/User-signup/cride/users/serializers/users.py)

### 24. Configurar envío de email
:link: :octocat: [cride-platzi/cride/users/views/users.py](https://github.com/macknilan/cride-platzi/blob/16/Login-restricted/cride/users/serializers/users.py)

### 25. Instalar PyJWT y generar tokens

+ :link: :octocat: [cride-platzi/cride/users/views/users.py](https://github.com/macknilan/cride-platzi/blob/17/Confirmation-email/cride/users/serializers/users.py)
+ :link: :octocat: [Branch 18/JWT](https://github.com/macknilan/cride-platzi/commit/75f35ad6b7d96ff3489fa4708a7b8c44d82e24f4)
+ :link: :octocat: [anymail/django-anymail](https://github.com/anymail/django-anymail)
+ :link: [Sending email](https://docs.djangoproject.com/en/3.0/topics/email/)
+ :link: [render_to_string](https://docs.djangoproject.com/en/3.0/topics/templates/#django.template.loader.render_to_string)
+ :link: [JSON Web Token implementation in Python](https://github.com/jpadilla/pyjwt)
+ :link: [:house: PyJWT](https://pyjwt.readthedocs.io/en/latest/)
+ :link: :octocat: [django - class EmailMessage:](https://docs.djangoproject.com/en/3.0/_modules/django/core/mail/message/#EmailMessage)

### 26. Verificar cuenta usando JWT

+ :link: :octocat: [Branch 19/JWT-Verification](https://github.com/macknilan/cride-platzi/commit/61267700d183e5de803db3bda08d58dccda5477b)
+ :link: [DRF saving-instances](https://www.django-rest-framework.org/api-guide/serializers/#saving-instances)
+ :link: :octocat: [pyjwt/jwt/exceptions.py](https://github.com/jpadilla/pyjwt/blob/master/jwt/exceptions.py)
+ :link: :octocat: [PyJWT PyJWT classes Exceptions](https://github.com/jpadilla/pyjwt/blob/master/jwt/exceptions.py)

### 27. Actualizar modelo de circle (membership)

+ :link: [Django - Extra fields on many-to-many relationships](https://docs.djangoproject.com/en/3.0/topics/db/models/#extra-fields-on-many-to-many-relationships)
- :link: :octocat: [20/Membership-model](https://github.com/macknilan/cride-platzi/commit/68a57213aaf95c9ffb7fd8f33f9cd9ebe3a7321c)


### 28. Crear CircleViewSet 👀 🚨

- :link: :octocat: [21/CircleViewSet]()
- :link: :octocat: [django-rest-framework/rest_framework/viewsets.py](https://github.com/encode/django-rest-framework/blob/master/rest_framework/viewsets.py)
- :link: [django Rest Framework - ViewSets](https://www.django-rest-framework.org/api-guide/viewsets/)
- :link: [django Rest Framework - Generic views](https://www.django-rest-framework.org/api-guide/generic-views/)
- :link: :octocat: [django-rest-framework/rest_framework/generics.py](https://github.com/encode/django-rest-framework/blob/master/rest_framework/generics.py)
- :link: :octocat: [django-rest-framework/rest_framework/mixins.py](https://github.com/encode/django-rest-framework/blob/master/rest_framework/mixins.py)


### 29. Añadiendo autorización y paginación

- :link: :octocat: [22/Pagination-Auth](https://github.com/macknilan/cride-platzi/commit/424aebb22ca3f29977da069646db8961c5bab00c)
- :link: [Django Rest Framework - LimitOffsetPagination](https://www.django-rest-framework.org/api-guide/pagination/#limitoffsetpagination)
- :link: [Django REst Framework - Authentication](https://www.django-rest-framework.org/api-guide/authentication/)


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
- :link: :octocat: []()

### 40. Filtrado
- :link: :octocat: []()

### 41. App de rides y modelos
- :link: :octocat: []()

### 42. Implementar la publicación de un ride
- :link: :octocat: []()

### 43. Validación de campos de un serializer
- :link: :octocat: []()

### 44. Listado de rides
- :link: :octocat: []()

### 45. Editar un ride
- :link: :octocat: []()

### 46. Unirse a viaje
- :link: :octocat: []()

### 47. Terminar viaje
- :link: :octocat: []()

### 48. Calificar viaje
- :link: :octocat: []()

## 6. Tareas asíncronas
### 49. Creando tarea asíncrona

### 50. Creando tarea periódica

## 7. Testing
### 51. Python unittest y Django TestCase

### 52. DRF APITestCase

## 8. Django Admin
### 53. Admin actions: Modificar datos de un query

### 54. Admin actions: Regresando una respuesta HTTP

## 9. Deployment
### 55. Instalación de la aplicación

### 56. Configuración del dominio en Mailgun y del Bucket en Amazon S3

### 57. Configuración final de Docker Container usando Supervisor

### 58. Tutorial de despliegue de la aplicación

### 59. Futuros pasos y cierre del curso




















































































































