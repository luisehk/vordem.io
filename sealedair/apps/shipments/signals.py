from django.utils import timezone
from django.contrib.auth import get_user_model
from ..messaging.email.helpers import send_email
from .models import Status

User = get_user_model()


def _get_relevant_data(kwargs):
    # reusable function for the signals
    instance = kwargs.get('instance', None)
    created = kwargs.get('created', False)

    return instance, created


def set_status_as_current(sender, **kwargs):
    status, created = _get_relevant_data(kwargs)

    if created:
        shipment = status.shipment

        # set previous status arrival time
        if shipment.current_status:
            previous_status = shipment.current_status
            previous_status.end_datetime = timezone.now()
            previous_status.save()

        # set new status as current
        shipment.current_status = status
        shipment.save()

        # if status == delivered,
        # close the shipment and the status
        if status.checkpoint == Status.USA_DELIVERED:
            status.end_datetime = timezone.now()
            status.save()

            shipment.arrival_datetime = timezone.now()
            shipment.save()


def create_shipment_status(sender, **kwargs):
    shipment, created = _get_relevant_data(kwargs)

    if shipment.current_status is None:
        status = Status(shipment=shipment)
        status.save()

    if created:
        for user in User.objects.filter(
                notifications_config__new_shipment=True):
                send_email(
                    subject='Nuevo embarque creado',
                    to_email=[user.email],
                    template='emails/shipments/new_shipment.html',
                    ctx={
                        'user': user.first_name,
                        'shipment': shipment,
                        'truck': shipment.truck,
                        'plant': shipment.plant,
                        'carrier': shipment.truck.carrier.name
                    })
