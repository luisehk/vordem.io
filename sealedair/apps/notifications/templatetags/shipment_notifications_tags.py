from django import template
from ..models.notifications import Notification
register = template.Library()


@register.inclusion_tag('notifications/notifications.html')
def all_notifications():
    notifications = Notification.objects.all().order_by('-pk')
    return {'notifications': notifications}
