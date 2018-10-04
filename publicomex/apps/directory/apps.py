from django.db.models.signals import post_save
from django.apps import AppConfig


class DirectoryConfig(AppConfig):
    name = 'publicomex.apps.directory'
    label = 'publicomex_directory'
    verbose_name = 'Directory'

    def ready(self):
        from publicomex.apps.directory.models import File
        from publicomex.apps.directory.signals import (
            warm_image_file)

        post_save.connect(warm_image_file, sender=File)
