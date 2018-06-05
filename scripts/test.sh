#!/bin/sh
set -e
set -x

DC_FILE=${1:-docker-compose.yml}
CODE_PATH=/usr/src/app

docker-compose -f "$DC_FILE" run app flake8
docker-compose -f "$DC_FILE" run app radon cc "$CODE_PATH"
docker-compose -f "$DC_FILE" run app radon mi "$CODE_PATH"
docker-compose -f "$DC_FILE" run app bandit -r "$CODE_PATH"
# docker-compose -f $DC_FILE run app python manage.py test -k
