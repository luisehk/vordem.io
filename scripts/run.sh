#!/bin/sh
set -e
set -x

DC_FILE=${1:-docker-compose.yml}

docker-compose -f $DC_FILE stop
docker-compose -f $DC_FILE up -d
