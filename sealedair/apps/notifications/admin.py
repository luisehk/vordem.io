from ...admin import site
from .models import UserNotificationsConfig, Notification


site.register([UserNotificationsConfig, Notification])
