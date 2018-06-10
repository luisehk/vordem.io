from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView,
    DetailView, ListView)
from ..mixins import VideoGenericView, VideoFormView
from ....content.models import Video


class VideoCreate(LoginRequiredMixin, VideoFormView, CreateView):
    template_name = 'content/lessons/videos/create.html'


class VideoUpdate(LoginRequiredMixin, VideoFormView, UpdateView):
    template_name = 'content/lessons/videos/update.html'


class VideoDelete(LoginRequiredMixin, VideoGenericView, DeleteView):
    template_name = 'content/lessons/videos/delete.html'


class VideoDetail(LoginRequiredMixin, DetailView):
    template_name = 'content/lessons/videos/detail.html'
    queryset = Video.objects.all()


class VideoList(LoginRequiredMixin, ListView):
    template_name = 'content/lessons/videos/list.html'
    queryset = Video.objects.all()
