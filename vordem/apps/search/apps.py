from django.apps import AppConfig


class SearchConfig(AppConfig):
    name = 'vordem.apps.search'
    label = 'vordem_search'
    verbose_name = 'Search'

    def ready(self):
        pass
