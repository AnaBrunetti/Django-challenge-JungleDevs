# Overview
API developed with python + django + rest framework. For articles with authors. [test developed for JungleDevs]

# Requirements

* Docker [Installation](https://docs.docker.com/get-docker/ "Installation")

# Run project
* Git clone this repository.
* Open ide and project folder (vs used).

**Development**
* At terminal: <br>
 ```
 $ docker-compose build
 $ docker-compose up -d
 $ docker exec -it app-django-challenge bash
 $ python manage.py migrate
 $ python manage.py createsuperuser
 $ python manage.py collectstatic --no-input
 ```
* Access http://127.0.0.1:8080/ or http://localhost:8080/

**Production**
* At terminal: <br>
 ```
 $ docker-compose -f docker-compose-prd.yml build
 $ docker-compose -f docker-compose-prd.yml up -d
 $ docker exec -it app-django-prd-challenge bash
 $ python manage.py migrate
 $ python manage.py createsuperuser
 $ python manage.py collectstatic --no-input
 ```
* Access http://127.0.0.1:2324/ or http://localhost:2324/

# Endpoints
More details are avalibe at /redoc or /swagger <br>
Manager are avalibe at /admin
<br>
 **All GET methods don't list inactive items.**

Url | HTTP | Operation | Result
-- | -- |-- |--
`/api/login` | POST | CREATE | User Login and a new access token is create for the logged user.
`/api/sign-out` | POST | CREATE | User logout and disable the token.
`/api/sign-up` | POST | CREATE | Creates a new user.
`/api/password/change`| POST | UPDATE | Updates the user's password.
`/api/deactivateUser` | POST | CREATE | Deactivates an user.
`/api/reactivateUser` | POST | CREATE | Reactivates an user.
`/api/admin/authors/`| GET, POST | READ, CREATE | Gets all authors/ create a new one (Only for staff users).
`/api/admin/authors/{pk}`| GET, PUT, PATCH, DELETE | READ, UPDATE, DELETE | Gets an author by id and allows to edit/exclude it (Only for staff users).
`/api/admin/articles/`| GET, POST | READ, CREATE | Gets all articles/ create a new one (Only for staff users).
`/api/admin/articles/{pk}`| GET, PUT, PATCH, DELETE | READ, UPDATE, DELETE | Gets an article by id and allows to edit/exclude it (Only for staff users).
`/api/articles/`| GET | READ | Gets all articles.
`/api/articles/?category={category}`| GET | READ | Gets filtered articles by category name.
`/api/articles/{pk}`| GET | READ | Gets article's details by id. The response for a logged user is different of a not logged one.
