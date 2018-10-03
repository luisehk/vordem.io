Publicomex

Run locally:
docker-compose up

Run as daemon:
docker-compose up -d

Check logs
docker-compose logs -f

Create a .env file if none is present:
touch .env

Remember to run this command when deploying:
./scripts/deploy.sh

Enforce pep8 (linter)
docker-compose run app flake8

If not using docker, please note requirements.txt file is located in docker/python
