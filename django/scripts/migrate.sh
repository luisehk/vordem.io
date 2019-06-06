#!/bin/sh
set -e
set -x

DC_FILE=${1:-docker-compose.yml}

docker-compose -f "$DC_FILE" run app python manage.py migrate contenttypes
docker-compose -f "$DC_FILE" run app python manage.py migrate auth
docker-compose -f "$DC_FILE" run app python manage.py migrate sites
docker-compose -f "$DC_FILE" run app python manage.py migrate
