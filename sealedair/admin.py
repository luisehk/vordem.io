from django.contrib.admin import AdminSite
from django.contrib.admin.models import LogEntry
from django.contrib.auth import get_user_model


User = get_user_model()


class AdminSite(AdminSite):
    site_header = 'Site administration'


site = AdminSite(name='site_admin')
site.register([LogEntry, User])
