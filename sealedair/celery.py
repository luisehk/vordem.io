from celery import Celery
from celery.schedules import crontab
import os

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'sealedair.settings')

app = Celery('sealedair')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=0, minute=0, day_of_week=1),
        do_nothing.s(),
        name='Do nothing every week')

    sender.add_periodic_task(
        30.0,
        set_shipments_time_status.s(),
        name='Update shipments time status')


@app.task
def do_nothing():
    pass


@app.task
def set_shipments_time_status():
    from sealedair.apps.shipments.models import Shipment, Status

    shipments = Shipment.objects.exclude(
        current_status__isnull=True,
        current_status__checkpoint=Status.USA_DELIVERED)
    on_time_shipments = shipments.filter(
        current_status__time_status=Status.TIME_ONTIME)
    delayed_shipments = shipments.filter(
        current_status__time_status=Status.TIME_DELAYED)

    for shipment in on_time_shipments:
        status = shipment.current_status
        hours_spent = status.get_hours_since_start()

        if hours_spent > 8:
            status.time_status = Status.TIME_DELAYED
            status.save()

    for shipment in delayed_shipments:
        status = shipment.current_status
        hours_spent = status.get_hours_since_start()

        if hours_spent > 16:
            status.time_status = Status.TIME_LATE
            status.save()
