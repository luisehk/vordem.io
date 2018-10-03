web: gunicorn publicomex.wsgi:application --workers 15 -k gevent --enable-stdio-inheritance
worker: celery worker --app=publicomex.celery.app -B
