from extra_views import (
    InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from ..mixins import (
    LessonGenericView, BASE_LESSON_FIELDS,
    GetOrCreateBySkill)
from ...models import Quiz, Question
import json


class QuizGenericView(LessonGenericView):
    model = Quiz


class QuizFormView(QuizGenericView):
    fields = BASE_LESSON_FIELDS


class QuestionForm(object):
    fields = ['name']


class QuestionInline(QuestionForm, InlineFormSet):
    model = Question
    factory_kwargs = {
        'can_order': True,
        'can_delete': True,
        'extra': 1,
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

    def parse_options_json(self, options_json):
        options = json.loads(options_json)
        return isinstance(options, list), options

    def process_question_options(self, options):
        print('OPTIONS', options)

    def post(self, request, *args, **kwargs):
        if 'options-json' in request.POST:
            is_list, options = self.parse_options_json(
                request.POST['options-json'])

            if is_list:
                self.process_question_options(options)

        return super().post(request, *args, **kwargs)


class QuizDelete(LoginRequiredMixin, QuizFormView, DeleteView):  # noqa
    template_name = 'content/lessons/quizzes/delete.html'
