from celery import shared_task


def _send_message(users_ids, obj={}, title='', body=''):
    from fcm.utils import get_device_model
    from django.contrib.auth import get_user_model
    Device = get_device_model()
    User = get_user_model()
    users = User.objects.filter(id__in=users_ids)

    if users:
        devices = Device.objects.filter(user__in=users)
        if obj or title or body:
            devices.send_message(obj, notification={
                'title': title,
                'body': body,
                "server": 1
            })


@shared_task
def push_object(users_ids, obj={}, title='', body=''):
    _send_message(users_ids, obj=obj, title=title, body=body)
