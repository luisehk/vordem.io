from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from ..mixins import LessonGenericView, FULL_LESSON_FIELDS, GetOrCreateBySkill
from extra_views import CreateWithInlinesView, UpdateWithInlinesView
from ...models import Intro


class IntroGenericView(LessonGenericView):
    model = Intro


class IntroFormView(IntroGenericView):
    fields = FULL_LESSON_FIELDS


class IntroGetOrCreate(LoginRequiredMixin, GetOrCreateBySkill):
    model = Intro


class IntroCreate(LoginRequiredMixin, IntroFormView, CreateWithInlinesView):
    template_name = 'content/lessons/intros/create.html'


class IntroUpdate(LoginRequiredMixin, IntroFormView, UpdateWithInlinesView):
    template_name = 'content/lessons/intros/update.html'


class IntroDelete(LoginRequiredMixin, IntroGenericView, DeleteView):
    template_name = 'content/lessons/intros/delete.html'
