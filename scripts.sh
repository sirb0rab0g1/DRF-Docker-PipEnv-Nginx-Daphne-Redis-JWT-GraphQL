#!/bin/bash
./ manage.py migrate --no-input
./ manage.py collectstatic --no-input
# python manage.py runserver 0.0.0.0:8000
daphne -b 0.0.0.0 -p 8000 api.asgi:application

# Prepare log files and start outputting logs to stdout
touch /srv/logs/gunicorn.log
touch /srv/logs/access.log
