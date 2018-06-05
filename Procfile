web: gunicorn learningco.wsgi:application -workers 5 -k gevent --enable-stdio-inheritance
worker: celery worker --app=learningco.celery.app -B
