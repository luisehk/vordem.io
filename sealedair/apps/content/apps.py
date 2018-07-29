from django.apps import AppConfig
from django.db.models.signals import post_save


class ContentConfig(AppConfig):
    name = 'sealedair.apps.content'
    label = 'sealedair_content'

    def ready(self):
        from sealedair.apps.content.models import Lesson
        from sealedair.apps.content.signals import warm_lesson_thumbnail

        post_save.connect(warm_lesson_thumbnail, sender=Lesson)
