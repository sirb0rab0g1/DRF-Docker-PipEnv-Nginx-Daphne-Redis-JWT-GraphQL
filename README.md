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

## To GET/POST/PATCH navigate to
[http://localhost:8000/api/basic/information/](http://localhost:8000/api/basic/information/)

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
