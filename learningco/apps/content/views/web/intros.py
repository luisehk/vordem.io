from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView)
from ..mixins import IntroGenericView, IntroFormView


class IntroCreate(LoginRequiredMixin, IntroFormView, CreateView):
    template_name = 'content/lessons/intros/create.html'


class IntroUpdate(LoginRequiredMixin, IntroFormView, UpdateView):
    template_name = 'content/lessons/intros/update.html'


class IntroDelete(LoginRequiredMixin, IntroGenericView, DeleteView):
    template_name = 'content/lessons/intros/delete.html'
