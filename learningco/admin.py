from django.contrib.admin import AdminSite
from django.contrib.admin.models import LogEntry


class AdminSite(AdminSite):
    site_header = 'Site administration'


site = AdminSite(name='site_admin')
site.register(LogEntry)
