#!/bin/sh
set -e
set -x

DC_FILE=${1:-docker-compose.yml}

touch .env
docker-compose -f $DC_FILE build
docker-compose -f $DC_FILE run app python manage.py migrate
docker-compose -f $DC_FILE run app python manage.py collectstatic --noinput
docker-compose -f $DC_FILE run app python manage.py loaddata fixtures/initial_data.json
