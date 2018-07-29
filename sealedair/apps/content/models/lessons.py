from versatileimagefield.fields import VersatileImageField, PPOIField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer
from versatileimagefield.placeholder import OnDiscPlaceholderImage
from django.contrib.auth import get_user_model
from embed_video.fields import EmbedVideoField
from embed_video.backends import detect_backend
from polymorphic.models import PolymorphicModel
from django.urls import reverse_lazy
from django.db import models
from django.conf import settings
from .skills import Skill
import os


User = get_user_model()


class Lesson(PolymorphicModel):
    skill = models.ForeignKey(
        Skill, verbose_name='Competencia',
        null=False, on_delete=models.CASCADE,
        related_name='lessons')
    name = models.CharField(
        verbose_name='Nombre',
        max_length=150)
    body = models.TextField(blank=False, default='')
    thumbnail = VersatileImageField(
        null=True, blank=True, ppoi_field='ppoi',
        placeholder_image=OnDiscPlaceholderImage(
            path=os.path.join(
                settings.BASE_DIR,
                'static/imgs/profile-neutral.png'
            )))
    ppoi = PPOIField('Image PPOI', default=(0.5, 0.5))

    class Meta:
        ordering = ['name']
        verbose_name = 'Lección'

    def __str__(self):
        return self.name

    def get_type(self):
        return self._meta.verbose_name.title()

    def warm_thumbnail(self):
        img_warmer = VersatileImageFieldWarmer(
            instance_or_queryset=self,
            rendition_key_set='lesson_thumbnail',
            image_attr='thumbnail')

        img_warmer.warm()

    def get_thumbnail(self):
        return self.thumbnail.url

    def get_update_url(self):
        return ''

    def get_create_url(self, skill):
        return ''

    def get_skill_attribute_name(self):
        return ''


class Intro(Lesson):
    class Meta:
        ordering = ['name']
        verbose_name = 'Intro'

    def get_update_url(self):
        return reverse_lazy(
            'content:intro-update',
            args=(self.id,))

    def get_create_url(self, skill):
        return reverse_lazy(
            'content:intro-add',
            kwargs={
                'skill_pk': skill.id
            })

    def get_skill_attribute_name(self):
        return 'intro'


class Video(Lesson):
    video_url = EmbedVideoField()

    class Meta:
        ordering = ['name']
        verbose_name = 'Video'

    def get_thumbnail(self):
        video = detect_backend(self.video_url)
        return video.get_thumbnail_url()

    def get_update_url(self):
        return reverse_lazy(
            'content:video-update',
            args=(self.id,))

    def get_create_url(self, skill):
        return reverse_lazy(
            'content:video-add',
            kwargs={
                'skill_pk': skill.id
            })

    def get_skill_attribute_name(self):
        return 'video'


class Quiz(Lesson):
    class Meta:
        ordering = ['name']
        verbose_name = 'Cuestionario'

    def get_update_url(self):
        return reverse_lazy(
            'content:quiz-update',
            args=(self.id,))

    def get_create_url(self, skill):
        return reverse_lazy(
            'content:quiz-add',
            kwargs={
                'skill_pk': skill.id
            })

    def get_skill_attribute_name(self):
        return 'quiz'


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, verbose_name='Cuestionario',
        null=False, on_delete=models.CASCADE,
        related_name='questions')
    name = models.TextField(blank=False)


class Option(models.Model):
    question = models.ForeignKey(
        Question, verbose_name='Pregunta',
        null=False, on_delete=models.CASCADE,
        related_name='options')
    name = models.TextField(blank=False)
    value = models.IntegerField(default=0)


class Article(Lesson):
    class Meta:
        ordering = ['name']
        verbose_name = 'Articulo'

    def get_update_url(self):
        return reverse_lazy(
            'content:article-update',
            args=(self.id,))

    def get_create_url(self, skill):
        return reverse_lazy(
            'content:article-add',
            kwargs={
                'skill_pk': skill.id
            })

    def get_skill_attribute_name(self):
        return 'article'


class ActivityList(Lesson):
    class Meta:
        ordering = ['name']
        verbose_name = 'Actividades'

    def get_update_url(self):
        return reverse_lazy(
            'content:activity-update',
            args=(self.id,))

    def get_create_url(self, skill):
        return reverse_lazy(
            'content:activity-add',
            kwargs={
                'skill_pk': skill.id
            })

    def get_skill_attribute_name(self):
        return 'activity_list'


class Activity(models.Model):
    activity_list = models.ForeignKey(
        ActivityList, verbose_name='Lista de actividades',
        null=False, on_delete=models.CASCADE,
        related_name='activities')
    name = models.CharField(max_length=150)
    description = models.TextField(blank=False)
    body = models.TextField(blank=False, default='')
