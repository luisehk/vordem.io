from django.apps import AppConfig


class DirectoryConfig(AppConfig):
    name = 'publicomex.apps.directory'
    label = 'publicomex_directory'
    verbose_name = 'Directory'

    def ready(self):
        pass
