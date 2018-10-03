from django.apps import AppConfig


class RequestsConfig(AppConfig):
    name = 'publicomex.apps.requests'
    label = 'publicomex_requests'
    verbose_name = 'Requests'

    def ready(self):
        pass
