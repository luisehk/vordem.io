web: gunicorn vordem.wsgi:application --workers 5 -k gevent --enable-stdio-inheritance
worker: celery worker --app=vordem.celery.app -B
