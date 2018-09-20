from django.utils import timezone
from django.contrib.auth import get_user_model
from crum import get_current_user
from sealedair.apps.notifications.models import Notification
from pytz import timezone as pytz_timezone
from .models import Status, Shipment, Comment

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
    user_request = get_current_user()  # user logged in
    # create status
    if shipment.current_status is None:
        status = Status(shipment=shipment)
        status.save()

    if created:
        # create new shipment
        Notification.objects.create(
            user=user_request,
            shipment=shipment,
            message="Nuevo Envío",
            reason=Notification.NEW_SHIPMENT)

        for user in User.objects.filter(
                notifications_config__email=True,
                notifications_config__new_shipment=True):
            shipment.email_notification_create_new_shipment(user)

    else:
        # modified shipment 'Destino: Entregado'
        if shipment.current_status.checkpoint == 'UDE':
            Notification.objects.create(
                user=user_request,
                shipment=shipment,
                message="Envío entregado",
                reason=Notification.DELIVERED_SHIPMENT)

            for user in User.objects.filter(
                    notifications_config__email=True,
                    notifications_config__delivered_shipment=True):
                shipment.email_notification_delivered_shipment(user)


def check_if_eta_changed(sender, **kwargs):
    new_shipment, created = _get_relevant_data(kwargs)

    if not created:
        # add a comment to the shipment if the ETA was changed
        original_shipment = Shipment.objects.get(id=new_shipment.id)
        original_eta = original_shipment.estimated_arrival_datetime
        new_eta = new_shipment.estimated_arrival_datetime
        current_user = get_current_user()

        if original_eta != new_eta:
            # NOTE: since we need to create the datetime to string
            # we are converting it to America/Monterrey timezone
            mty = pytz_timezone('America/Monterrey')
            dtf = '%d de %B del %Y a las %I:%M%p'  # date time format
            new_eta_str = new_eta.astimezone(mty).strftime(dtf)

            msg = ''

            if original_eta:
                verb = 'cambiado'
            else:
                verb = 'establecido'

            if current_user:
                msg += 'El usuario <strong>{}</strong> ha {} el ETA '.format(
                    current_user.get_full_name() or current_user.email,
                    verb
                )
            else:
                msg += 'El ETA ha sido {} '.format(
                    verb
                )

            if original_eta:
                original_eta_str = original_eta.astimezone(mty).strftime(dtf)
                msg += 'de <strong>{}</strong> a <strong>{}</strong>.'.format(
                    original_eta_str,
                    new_eta_str
                )
            else:
                msg += 'a <strong>{}</strong>.'.format(
                    new_eta_str
                )

            Comment.objects.create(
                shipment=original_shipment,
                user_id=1,  # this user is added via fixture
                body=msg)
