from django.apps import AppConfig
from django.db.models.signals import post_save


class ContentConfig(AppConfig):
    name = 'learningco.apps.content'
    label = 'learningco_content'

    def ready(self):
        from learningco.apps.content.models import Lesson
        from learningco.apps.content.signals import warm_lesson_thumbnail

        post_save.connect(warm_lesson_thumbnail, sender=Lesson)
