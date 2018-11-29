# Drf-Docker-PipEnv-Nginx-Daphne-Redis

## Prerequisites

1. Must have [Docker](https://www.docker.com/get-started) installed.

## Pre-setup

1. Change/duplicate `.env.tpl` to `.env` and edit the values inside accordingly

------------------------------

## 1. First migrate the database
`make migrate`

## 2. For building local development
`make local`

## To start and create the dockerize environment
`make up`

## To stop and remove the dockerize environment
`make down`

## To makemigrations
`make migrations name=` then the name you want to commit

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

### [Graphql-Python/Graphene-Django](http://docs.graphene-python.org/projects/django/en/latest/) <br />
Primary focus here is to give a good understanding of how to connect models from Django ORM to graphene object types.

### FAQ
* TypeError: 'module' object is not callable
This is cause by django 3.7 and pipenv 18.1 version. So to fix this 

	* `pip install pipenv`
	* `pipenv run pip install pip==18.0`
	* `pipenv install`

* I'm getting `ERROR: Get https://registry-1.docker.io/v2/: dial tcp: lookup registry-1.docker.io ... : read: connection refused` error.

    * Do `docker-machine ssh default`, then edit the resolve file `sudo vi /etc/resolv.conf` change the nameserver value to `1.1.1.1` or `8.8.8.8`
    
* : Bind for `0.0.0.0:5432` failed: port is already allocated
    
    * `docker ps`
    * after that this will showen up <br />
    ```13b484047582        postgres:9.6.5-alpine   "docker-entrypoint.s…"   28 hours ago        Up 5 hours          0.0.0.0:5432->5432/tcp   sample_db```
    
    * the conflict is ```0.0.0.0:5432->5432/tcp```
    * we need to stop the docker container first
    * `$ docker stop 13b484047582`
    * then remove 
    * `$ docker remove 13b484047582`
    * then re run the environment
    * `$ make local(rebuilding container) / make up(starting container)`

    
    
