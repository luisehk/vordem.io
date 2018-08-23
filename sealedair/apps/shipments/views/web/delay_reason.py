from extra_views import CreateWithInlinesView, UpdateWithInlinesView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView
from django.views.generic.base import ContextMixin, TemplateView
from ...models import DelayReason


class DelayReasonGenericView(LoginRequiredMixin, ContextMixin):
    model = DelayReason

    def get_success_url(self):
        return reverse_lazy(
            'shipments:delay-reason-list')


class DelayReasonFormView(DelayReasonGenericView):
    fields = ['reason']


class DelayReasonList(DelayReasonGenericView, ListView):
    template_name = 'shipments/delay_reason/list.html'
    queryset = DelayReason.objects.all().order_by('pk')


class DelayReasonCreate(DelayReasonFormView, CreateWithInlinesView):
    template_name = 'shipments/delay_reason/create.html'


class DelayReasonUpdate(DelayReasonFormView, UpdateWithInlinesView):
    template_name = 'shipments/delay_reason/update.html'


class DelayReasonDelete(DelayReasonGenericView, DeleteView):
    template_name = 'shipments/delay_reason/delete.html'
