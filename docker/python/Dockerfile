FROM python:3.6
MAINTAINER Luis Herrada <luis@vordem.mx>

# environment configuration
ENV PYTHONUNBUFFERED 1

# create app directory
WORKDIR /root

# install pip requirements
ADD requirements.txt /root/

# install gettext
RUN apt-get update
RUN apt-get install gettext -y

# install pip requirements
RUN pip install -r requirements.txt --default-timeout 450

# run code through volume
VOLUME /usr/src/app
WORKDIR /usr/src/app

# install postgres-client
RUN apt-get install -y postgresql-client

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "learningco.wsgi:application", "--reload", "--enable-stdio-inheritance"]
