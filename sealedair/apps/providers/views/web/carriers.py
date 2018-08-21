from extra_views import CreateWithInlinesView, UpdateWithInlinesView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView
from django.views.generic.base import ContextMixin
from ...models import Carrier


class CarrierGenericView(LoginRequiredMixin, ContextMixin):
    model = Carrier

    def get_success_url(self):
        return reverse_lazy(
            'providers:carrier-list')


class CarrierFormView(CarrierGenericView):
    fields = ['name', 'code', 'color']


class CarrierCreate(CarrierFormView, CreateWithInlinesView):
    template_name = 'providers/carriers/create.html'


class CarrierUpdate(CarrierFormView, UpdateWithInlinesView):
    template_name = 'providers/carriers/update.html'


class CarrierDelete(CarrierGenericView, DeleteView):
    template_name = 'providers/carriers/delete.html'


class CarrierList(CarrierGenericView, ListView):
    template_name = 'providers/carriers/list.html'
    queryset = Carrier.objects.all().order_by('pk')
