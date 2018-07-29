web: gunicorn sealedair.wsgi:application --workers 5 -k gevent --enable-stdio-inheritance
worker: celery worker --app=sealedair.celery.app -B
