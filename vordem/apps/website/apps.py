from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    name = 'vordem.apps.website'
    label = 'vordem_website'
    verbose_name = 'Website'

    def ready(self):
        pass
