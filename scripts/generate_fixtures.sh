#!/bin/sh
set -e
set -x

DC_FILE=${1:-docker-compose.yml}

docker-compose -f "$DC_FILE" run app python manage.py dumpdata sealedair_providers.Carrier --indent 2 > fixtures/carriers.json
docker-compose -f "$DC_FILE" run app python manage.py dumpdata sealedair_company.Plant --indent 2 > fixtures/plants.json   