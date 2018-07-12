from extra_views import (
    InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.db import transaction
from ..mixins import (
    LessonGenericView, BASE_LESSON_FIELDS,
    GetOrCreateBySkill)
from ...models import Quiz, Question, Option
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

    # only support options for existing questions
    def process_question_options(self, options):
        # split new and existing options into two lists
        new_options = [{
            'question_id': o['question_id'],
            'name': o['name']
        } for o in options if not o['id'] and o['name']]
        existing_options = [o for o in options if o['id']]

        # we will store all affected ids (new and existing)
        affected_ids = [o['id'] for o in existing_options]

        # create new options first
        for option in new_options:
            obj = Option.objects.create(**option)
            affected_ids.append(obj.id)

        # now update existing options with their
        for option in existing_options:
            Option.objects.filter(id=option['id']).update(**option)

        # now do some cleanup
        if options:
            # retrieve the quiz
            quiz = Quiz.objects.get(questions__id=options[0]['question_id'])

            # delete removed questions from this quiz
            Option.objects.filter(
                question__quiz__id=quiz.id
            ).exclude(id__in=affected_ids).delete()

            # delete options with empty text
            Option.objects.filter(name__exact='').delete()

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            if 'options-json' in request.POST:
                is_list, options = self.parse_options_json(
                    request.POST['options-json'])

                if is_list:
                    self.process_question_options(options)

        return super().post(request, *args, **kwargs)


class QuizDelete(LoginRequiredMixin, QuizFormView, DeleteView):  # noqa
    template_name = 'content/lessons/quizzes/delete.html'
