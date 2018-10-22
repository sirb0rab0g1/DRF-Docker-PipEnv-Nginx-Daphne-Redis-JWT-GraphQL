# Use the Python Slim
FROM python:3.6.5-slim

# Force stdin, stdout and stderr to be totally unbuffered and don´t write .pyc or .pyo files
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

MAINTAINER Pasmo

RUN mkdir /starter-api && \
    mkdir /srv/logs

RUN set -xe \
        && apt-get update && apt-get install -y --no-install-recommends \
          curl \
          gettext \
          -y gcc \
          -y g++ \
        && pip install pipenv

COPY Pipfile Pipfile.lock scripts.sh /

RUN LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "pipenv install --system --dev" \
    && rm -rf ~/.cache/pip \
  && chmod +x scripts.sh

COPY . /starter-api/

WORKDIR /starter-api

EXPOSE 8000

EXPOSE 6379

CMD ["/scripts.sh"]
