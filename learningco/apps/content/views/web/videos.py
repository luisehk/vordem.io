from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from ..mixins import (
    DEFAULT_LESSON_FIELDS, LessonGenericView,
    GetOrCreateBySkill)
from extra_views import CreateWithInlinesView, UpdateWithInlinesView
from ...models import Video


class VideoGenericView(LessonGenericView):
    model = Video


class VideoFormView(VideoGenericView):
    fields = DEFAULT_LESSON_FIELDS + ['video_url']


class VideoGetOrCreate(LoginRequiredMixin, GetOrCreateBySkill):
    model = Video


class VideoCreate(LoginRequiredMixin, VideoFormView, CreateWithInlinesView):
    template_name = 'content/lessons/videos/create.html'


class VideoUpdate(LoginRequiredMixin, VideoFormView, UpdateWithInlinesView):
    template_name = 'content/lessons/videos/update.html'


class VideoDelete(LoginRequiredMixin, VideoGenericView, DeleteView):
    template_name = 'content/lessons/videos/delete.html'
