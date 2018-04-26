from .tasks import push_object


def send_push_notification(sender, **kwargs):
    n = kwargs['instance']

    if kwargs['created']:
        push_object.delay(
            [n.recipient.id],
            '',
            n.description)
