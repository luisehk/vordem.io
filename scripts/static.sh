DC_FILE=${1:-docker-compose.yml}

docker-compose -f $DC_FILE exec app python manage.py collectstatic --noinput --clear
