from extra_views import (
    InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from ..mixins import QuizFormView, QuestionForm, GetOrCreateBySkill
from ...models import Quiz, Question


class QuestionInline(QuestionForm, InlineFormSet):
    model = Question
    factory_kwargs = {
        'can_order': True,
        'can_delete': True,
        'extra': 0,
    }


class QuizGetOrCreate(LoginRequiredMixin, GetOrCreateBySkill):
    model = Quiz


class QuizCreate(LoginRequiredMixin, QuizFormView, CreateWithInlinesView):  # noqa
    model = Quiz
    inlines = [QuestionInline]
    template_name = 'content/lessons/quizzes/create.html'


class QuizUpdate(LoginRequiredMixin, QuizFormView, UpdateWithInlinesView):  # noqa
    model = Quiz
    inlines = [QuestionInline]
    template_name = 'content/lessons/quizzes/update.html'


class QuizDelete(LoginRequiredMixin, QuizFormView, DeleteView):  # noqa
    template_name = 'content/lessons/quizzes/delete.html'
