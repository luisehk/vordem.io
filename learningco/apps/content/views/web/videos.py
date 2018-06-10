from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView,)
from ..mixins import VideoGenericView, VideoFormView


class VideoCreate(LoginRequiredMixin, VideoFormView, CreateView):
    template_name = 'content/lessons/videos/create.html'


class VideoUpdate(LoginRequiredMixin, VideoFormView, UpdateView):
    template_name = 'content/lessons/videos/update.html'


class VideoDelete(LoginRequiredMixin, VideoGenericView, DeleteView):
    template_name = 'content/lessons/videos/delete.html'
