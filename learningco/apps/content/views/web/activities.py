from extra_views import (
    InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from ..mixins import (
    LessonGenericView, BASE_LESSON_FIELDS,
    GetOrCreateBySkill)
from ...models import ActivityList, Activity


class ActivityListGenericView(LessonGenericView):
    model = ActivityList


class ActivityListFormView(ActivityListGenericView):
    fields = BASE_LESSON_FIELDS


class ActivityForm(object):
    fields = ['name', 'description', 'body']



class ActivityInline(ActivityForm, InlineFormSet):
    model = Activity
    factory_kwargs = {
        'can_order': True,
        'can_delete': True,
        'extra': 0,
    }


class ActivityListGetOrCreate(LoginRequiredMixin, GetOrCreateBySkill):
    model = ActivityList


class ActivityListCreate(LoginRequiredMixin, ActivityListFormView, CreateWithInlinesView):  # noqa
    model = ActivityList
    inlines = [ActivityInline]
    template_name = 'content/lessons/activities/create.html'


class ActivityListUpdate(LoginRequiredMixin, ActivityListFormView, UpdateWithInlinesView):  # noqa
    model = ActivityList
    inlines = [ActivityInline]
    template_name = 'content/lessons/activities/update.html'


class ActivityListDelete(LoginRequiredMixin, ActivityListFormView, DeleteView):  # noqa
    template_name = 'content/lessons/activities/delete.html'
