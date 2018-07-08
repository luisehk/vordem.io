from extra_views import (
    InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from ..mixins import ActivityListFormView, ActivityForm
from ...models import ActivityList, Activity


class ActivityInline(ActivityForm, InlineFormSet):
    model = Activity
    factory_kwargs = {
        'can_order': True,
        'can_delete': True,
        'extra': 0,
    }


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
