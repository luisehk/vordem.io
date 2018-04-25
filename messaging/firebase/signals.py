from .tasks import push_message


def send_push_notification(sender, **kwargs):
    n = kwargs['instance']

    if kwargs['created']:
        push_message.delay(
            [n.recipient.id],
            '',
            n.description)
