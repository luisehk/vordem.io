from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView)
from ..mixins import ArticleGenericView, ArticleFormView


class ArticleCreate(LoginRequiredMixin, ArticleFormView, CreateView):
    template_name = 'content/lessons/articles/create.html'


class ArticleUpdate(LoginRequiredMixin, ArticleFormView, UpdateView):
    template_name = 'content/lessons/articles/update.html'


class ArticleDelete(LoginRequiredMixin, ArticleGenericView, DeleteView):
    template_name = 'content/lessons/articles/delete.html'
