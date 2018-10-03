from celery import Celery
from celery.schedules import crontab
import os

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'publicomex.settings')

app = Celery('publicomex')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=0, minute=0, day_of_week=1),
        do_nothing.s(),
        name='Do nothing every week')


@app.task
def do_nothing():
    pass
