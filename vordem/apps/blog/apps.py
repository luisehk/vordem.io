from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'vordem.apps.blog'
    label = 'vordem_blog'
    verbose_name = 'Blog'

    def ready(self):
        pass
