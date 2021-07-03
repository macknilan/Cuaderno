#### <a name="INDEX"> :whale2: + :snake: </a>

- :link: [Last estable release python](https://endoflife.date/python)
- :link: [discuss.python.org release](https://discuss.python.org/tag/release)

- [Django on Docker](#Django-on-Docker)
- [Django on Docker in progress](#Django-on-Docker-in-progress)
- [Docker With Django And Postgresql](#Docker-With-Django-And-Postgresql)

### Django on Docker

:construction: En la carpeta Docker se encuentra el ejemplo **dj_docker**

#### :whale: + :snake: Docker + Django

Descargar la imagen de PostgreSQL

```bash
$ docker pull postgres
```

Iniciar una instancia de PostgreSQL

```bash
$ docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

Ya que el contenedor/imagen se este ejecutando, en otra terminal(o en la misma), ejecutar el siguiente comando, para poder entrar al contenedor

```bash
docker exec -it postgres psql -U postgres
```

- :link: [Django on Docker - A Simple Introduction](https://www.codingforentrepreneurs.com/blog/django-on-docker-a-simple-introduction)
- :link: [Installing system packages in Docker with minimal bloat](https://pythonspeed.com/articles/system-packages-docker/)

Crear una carpeta `dj_docker`

Instalar pipenv

```bash
$ python3 -m pip install --user pipenv
```

Crear carpeta con el nombre del projecto

```bash
$ mkdir dj_docker
```

Crear el ambiente virtual

```bash
# --tree QUE OCUPE PYTHON 3
$ pipenv --three
```

Instalar django

```bash
$ pipenv install django
```

Instalar gunicorn

```bash
$ pipenv install gunicorn
```

Activar amviente virtual

```bash
$ pipenv shell
```

Crear un proyecto en django

```bash
$ pipenv run django-admin startproject dj_docker .
```

BD local y migraciones

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuse
#
USER: dj_doker_2020
PWD: dj docker 2020
```

Actualizar dentro de `settings.py`

```bash
# importar os
import os
...
# DEBUG can be True/False or 1/0
DEBUG = int(os.environ.get('DEBUG', default=1))
```

Crear el archivo `.env` en carpeta raiz solo con la info de `DEBUG=1`

```bash
touch .env
# EDITAR EL ARCHIVO Y PONER SOLO LA INFO
DEBUG=1
```

Probar la configuración con

```bash
$ gunicorn dj_docker.wsgi:application --bind 0.0.0.0:8000
```

En local browser ir a la dirección `http://localhost:8000/`

Crear el archivo `Dockerfile` la imagen y el contenedor

Dentro de la carpeta del proyecto `dj_docker` crear el archivo `Dockerfile`

```bash
$ touch Dockerfile
```

Estructura de archivos y carpetas del projecto

```bash
.
├── db.sqlite3
├── dj_docker
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Dockerfile
├── .env
├── install-packages.sh
├── manage.py
├── Pipfile
└── Pipfile.lock
```

El archivo `Dockerfile` ocupa la imagen

```bash
$ docker pull $ docker pull python:3.9-slim-buster
```

```bash
# BASE IMAGE
FROM python:3.9-slim-buster

# RUN ITS CONTENT THE FILE TO INSTALL
# UPDATES FROM THE DEBIAN REPOSITORIES
COPY install-packages.sh .
RUN chmod +x install-packages.sh
RUN ./install-packages.sh

# CREATE AND SET WORKING DIRECTORY
RUN mkdir /app
WORKDIR /app

# ADD CURRENT DIRECTORY CODE TO WORKING DIRECTORY
ADD . /app/

# SET DEFAULT ENVIRONMENT VARIABLES
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DEBIAN_FRONTEND=noninteractive
# ENV LANG C.UTF-8

# SET PROJECT ENVIRONMENT VARIABLES
# GRAB THESE VIA PYTHON'S os.environ
# THESE ARE 100% OPTIONAL HERE
ENV PORT=8000

RUN apt-get update \
  # && apt-get install -y apt-utils \
  # DEPENDENCIES FOR BUILDING PYTHON PACKAGES
  && apt-get install -y build-essential \
  # PSYCOPG2 DEPENDENCIES
  && apt-get install -y libpq-dev \
  # TRANSLATIONS DEPENDENCIES
  && apt-get install -y gettext \
  # INSTALL GIT
  && apt-get install -y git \
  # CLEANING UP UNUSED FILES
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# INSTALL ENVIRONMENT DEPENDENCIES
RUN pip3 install --upgrade pip
RUN pip3 install pipenv

# INSTALL DEPENDENCIES FOR PROJECT FROM PIPFILE
RUN pipenv install --skip-lock --system --dev

EXPOSE 8888
CMD gunicorn dj_docker.wsgi:application --bind 0.0.0.0:$PORT
```

:eyes: En el mismo nivel se crea el archivo `install-packages.sh` el cual tiene por objetivo instalar las actualizaciones de debian por separado (_hay que hacer más pruebas para obtener menor peso de la imagen_)

```bash
#!/bin/bash

# Bash "strict mode", to help catch problems and bugs in the shell
# script. Every bash script you write should include this. See
# http://redsymbol.net/articles/unofficial-bash-strict-mode/ for
# details.
set -euo pipefail

# Tell apt-get we're never going to be able to give manual
# feedback:
export DEBIAN_FRONTEND=noninteractive

# Update the package listing, so we know what package exist:
apt-get update

# Install security updates:
apt-get -y upgrade

apt-get -y install --no-install-recommends apt-utils

# Install a new package, without unnecessary recommended packages:
apt-get -y install --no-install-recommends syslog-ng

# Delete cached files we don't need anymore:
apt-get clean
rm -rf /var/lib/apt/lists/*
```

Construir la imagen Docker

```bash
$ docker build -t simple-django-on-docker -f Dockerfile .
```

Ejecutar el contenedor

```bash
$  docker run -it -p 80:8888 simple-django-on-docker
```

En la dirección `http://localhost` para comprobar que se esta ejecutando

[[Volver al inicio]](#INDEX)

## :construction: :construction: :construction: :construction:

### Django on Docker in progress

## :construction: :construction: :construction: :construction:

Crear una carpeta `core`

Instalar pipenv

```bash
$ python3 -m pip install --user pipenv
```

Crear carpeta con el nombre del projecto

```bash
$ mkdir core
```

Crear el ambiente virtual

```bash
# --tree QUE OCUPE PYTHON 3
$ pipenv --three
```

Instalar django & libreria para PosrgreSQL

```bash
$ pipenv install django
# psycopg2
$ pipenv install psycopg2
# django-environ
$ pipenv install django-environ
```

:rotating_light: Activar ambiente virtual

```bash
$ pipenv shell
```

Crear un proyecto en django

```bash
$ pipenv run django-admin startproject core .
```

:eyes: Tener previamente PostgreSQL :octocat: [PostgreSQL](https://github.com/macknilan/Cuaderno/blob/master/PostgreSQL/PostgreSQL.md)

Cambiar la configuración de conección en `settings.py` para que se conecte a la BD de _PostgreSQL(local)_ y hacer pruebas de conexión

```bash
DATABASES = {
	'default': {
    	'ENGINE': 'django.db.backends.postgresql_psycopg2',
    	'NAME': 'sandbox',
    	'USER': 'user_sandbox',
    	'PASSWORD': 'user_sandbox_2020',
    	# 'HOST': 'db', # SET IN docker-compose.yml
    	'HOST': 'localhost',
    	'PORT': '5432',
	}
}
```

BD local y migraciones

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuse
#
USER: core_2020
PWD: dj pg docker 2020
```

Actualizar dentro de `settings.py`

```bash
# importar os
import os
...
# DEBUG can be True/False or 1/0
DEBUG = int(os.environ.get('DEBUG', default=1))
```

Crear el archivo `.env` en carpeta raiz solo con la info de `DEBUG=1`

```bash
touch .env
# EDITAR EL ARCHIVO Y PONER SOLO LA INFO
DEBUG=1
```

En la carpeta `core`

El archivo `Dockerfile` ocupa la imagen

```bash
$ docker pull $ docker pull python:3.9-slim-buster
```

```bash
# BASE IMAGE
FROM python:3.9-slim-buster

# RUN ITS CONTENT THE FILE TO INSTALL
# UPDATES FROM THE DEBIAN REPOSITORIES
COPY install-packages.sh .
RUN chmod +x install-packages.sh
RUN ./install-packages.sh

# CREATE AND SET WORKING DIRECTORY
RUN mkdir /app
WORKDIR /app

# ADD CURRENT DIRECTORY CODE TO WORKING DIRECTORY
ADD . /app/

# SET DEFAULT ENVIRONMENT VARIABLES
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DEBIAN_FRONTEND=noninteractive
# ENV LANG C.UTF-8

# SET PROJECT ENVIRONMENT VARIABLES
# GRAB THESE VIA PYTHON'S os.environ
# THESE ARE 100% OPTIONAL HERE
# ENV PORT=8000

RUN apt-get update \
  # && apt-get install -y apt-utils \
  # DEPENDENCIES FOR BUILDING PYTHON PACKAGES
  && apt-get install -y build-essential \
  # PSYCOPG2 DEPENDENCIES
  && apt-get install -y libpq-dev \
  # TRANSLATIONS DEPENDENCIES
  && apt-get install -y gettext \
  # INSTALL GIT
  && apt-get install -y git \
  # CLEANING UP UNUSED FILES
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# INSTALL ENVIRONMENT DEPENDENCIES
RUN pip3 install --upgrade pip
RUN pip3 install pipenv

# INSTALL DEPENDENCIES FOR PROJECT FROM PIPFILE
RUN pipenv install --skip-lock --system --dev

EXPOSE 8000
```

:eyes: En el mismo nivel se crea el archivo `install-packages.sh` el cual tiene por objetivo instalar las actualizaciones de debian por separado (_hay que hacer más pruebas para obtener menor peso de la imagen_)

- :link: :whale2: [Compose file versions and upgrading](https://docs.docker.com/compose/compose-file/compose-versioning/)

:file_cabinet: `local.yml`

```bash
version: '3.9'

services:
  postgres:
    image: postgres
    env_file:
      - ./.envs/.local/.postgres
    container_name: postgres
    volumes:
      - local_postgres_data:/var/lib/postgresql/data
      # - local_postgres_data_backups:/backups
    ports:
      - "5432:5432"
  django:
    build: .
    env_file:
      - ./.envs/.local/.django
      - ./.envs/.local/.postgres
    container_name: django
    command: python /app/manage.py migrate
    command: python /app/manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
        - "8000:8000"
    depends_on:
        - postgres
volumes:
  local_postgres_data:
```

Estructura de archivos y carpetas del projecto

```bash
.
├── core
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Dockerfile
├── install-packages.sh
├── local.yml
├── manage.py
├── Pipfile
└── Pipfile.lock
```

Como la imagen esta previamente desarrollada con un proyecto

```bash
# COMPOSE_FILE
$ export COMPOSE_FILE=local.yml

$ docker-compose build
$ docker-compose up
$ docker-compose ps
$ docker-compose down
```

```bash
$ docker-compose -f local.yml up --build
#
$ docker-compose -f local.yml ps
```

### Docker With Django And Postgresql

## :construction: :construction: (WIP) :construction: :construction:

1. Hacer folder `sandbox_dj_docker`
2. Crear el archivo `requirements.txt`

```txt
Django >= 3.2
psycopg2-binary >= 2.9
```

3. Crear el archivo Dockerfile

```
# GET THE IMAGE SLIM-BUSTER
FROM python:3.9-slim-buster
# FORCE STDIN, STDOUT AND STDERR TO BE TOTALLY UNBUFFERED. ON SYSTEMS WHERE IT MATTERS, ALSO PUT STDIN, STDOUT AND STDERR IN BINARY MODE.
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/
#
```

4. Crear el archivo `docker-compose.yml`

```yml
version: "3.9"

services:
  db:
    image: postgres
    volumes:
      - ./data/db:/var/lib/postgres/data
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
  web:
    build: .
    command: python3 manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
```

5. ejecutar el siguiente comando para crear el proyecto en la carpeta que se creo

```bash
$ docker-compose run web django-admin startproject dj_docker .
```

🚨 ¿POR QUE SE INSTALA CON ROOT, INVESTIGAR?

5. Modificar en el `settings.py`

```py
...
import psycopg2.extensions
...
ALLOWED_HOSTS = ['0.0.0.0']
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',  # SET IN docker-compose.yml
        'PORT': '5432',
    },
    'OPTIONS': {
        'isolation_level': psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE,
    },
}
```

6. Ejecutar los comando para ejecutar docker

```bash
# REALISAR LAS MIGRACIONES
$  docker-compose run web python manage.py makemigrations
#
$  docker-compose run web python manage.py migrate
# PARA LEVANTAR/INICIAR DOCKER-COMPOSE
$ docker-compose up
# PARA DETENER DOCKER-COMPOSE
$ docker-compose down
```

[[Volver al inicio]](#INDEX)
