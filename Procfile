web: gunicorn pythonjobs.wsgi --log-file -
worker: celery worker --app=pythonjobs.celery.app
