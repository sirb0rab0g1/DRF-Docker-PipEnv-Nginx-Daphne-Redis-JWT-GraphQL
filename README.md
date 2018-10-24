# Drf-Docker-PipEnv-Nginx-Daphne-Redis

## For building local development
`make local`

## To start and create the dockerize environment
`make up`

## To stop and remove the dockerize environment
`make down`

## To makemigrations
`make migrations name=` then the name you want to commit

## To migrate
`make migrate`

# How to

## After building your local development you must create a superuser account
`make superuser` required because of JWT authentication

## Then login in django admin
[http://localhost:8000/api/admin/](http://localhost:8000/api/admin)

## After a successful login navigate to
[http://localhost:8000/api/basic/information/](http://localhost:8000/api/basic/information/)

# EXTRAS
## To run a editor inside docker container using bpython
`make editor`

# FEATURES!!

### [Docker](https://docs.docker.com/compose/) <br />
deployment of applications inside software containers

### [Django Rest Framework](https://www.django-rest-framework.org/) <br />
Browsable api

### [PipEnv](https://pipenv.readthedocs.io/) <br /> 
For installing dependencies

### [Nginx](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/) <br /> 
As proxy

### [Daphne](https://github.com/django/daphne) <br /> 
As the interface server

### [Channels](https://channels.readthedocs.io/en/latest/)
Handling connections and sockets asynchronously

### [Redis](http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html) <br /> 
As the backend

### [Annoying](https://github.com/skorokithakis/django-annoying) <br />
This django application eliminates certain annoyances in the Django framework.

### [JWT Json Web Token](https://github.com/GetBlimp/django-rest-framework-jwt) <br />
Unlike some more typical uses of JWTs, this module only generates authentication tokens that will verify the user who is requesting one of your DRF protected API resources.
