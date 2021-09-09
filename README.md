# Post-prueba-tecnica-desarrollador-python

:link: :arrow_upper_right: [Doccumentación de la API con ✉️ 👨](https://documenter.getpostman.com/view/8810189/U16jLkXd)

- Para poder iniciar el proyecto desarrollado con **Django** hay que tener instalado  
  [x] Docker  
  [x] Docker compose

1. Clonar :octocat: el proyecto (:penguin: preferentemente)
2. Dentro del proyecto

```bash
docker-compose -f local.yml build
```

3. Para levantar el proyecto

```bash
docker-compose -f local.yml up
```

Login como admi al proyecto  
email: _la.bodega.services@gmail.com_  
pwd: _mack 2021_

Para iniciar desde cero el proyecto, eliminar los archivos `*.py` en las carpetas `migrations` y despues ejecutar los siguientes comandos.

Crear las migraciones.

```bash
docker-compose -f local.yml run --rm django python manage.py makemigrations
```

Ejecutar las migraciones.

```bash
docker-compose -f local.yml run --rm django python manage.py migrate
```

Crear el super-usuario(_email_)

```bash
docker-compose -f local.yml run --rm django python manage.py createsuperuser
```

Levantar el proyecto

```bash
docker-compose -f local.yml up
```

Entrar al link :link: [http://0.0.0.0:8000/](http://0.0.0.0:8000/)
