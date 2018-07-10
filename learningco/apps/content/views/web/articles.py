from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from ..mixins import (
    LessonGenericView, FULL_LESSON_FIELDS,
    GetOrCreateBySkill)
from extra_views import CreateWithInlinesView, UpdateWithInlinesView
from ...models import Article


class ArticleGenericView(LessonGenericView):
    model = Article


class ArticleFormView(ArticleGenericView):
    fields = FULL_LESSON_FIELDS


class ArticleGetOrCreate(LoginRequiredMixin, GetOrCreateBySkill):
    model = Article


class ArticleCreate(LoginRequiredMixin, ArticleFormView, CreateWithInlinesView):  # noqa
    template_name = 'content/lessons/articles/create.html'


class ArticleUpdate(LoginRequiredMixin, ArticleFormView, UpdateWithInlinesView):  # noqa
    template_name = 'content/lessons/articles/update.html'


class ArticleDelete(LoginRequiredMixin, ArticleGenericView, DeleteView):
    template_name = 'content/lessons/articles/delete.html'
