from extra_views import CreateWithInlinesView, UpdateWithInlinesView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView
from django.views.generic.base import ContextMixin, TemplateView
from ...models import Shipment


class ShipmentGenericView(LoginRequiredMixin, ContextMixin):
    model = Shipment


class ShipmentFormView(ShipmentGenericView):
    fields = ['name', 'code', 'color']


class Dashboard(ShipmentGenericView, TemplateView):
    template_name = 'shipments/dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx


class ShipmentCreate(ShipmentFormView, CreateWithInlinesView):  # noqa
    template_name = 'shipments/shipments/create.html'


class ShipmentUpdate(ShipmentFormView, UpdateWithInlinesView):  # noqa
    template_name = 'shipments/shipments/update.html'


class ShipmentDelete(ShipmentGenericView, DeleteView):
    template_name = 'shipments/shipments/delete.html'


class ShipmentList(ShipmentGenericView, ListView):
    template_name = 'shipments/shipments/list.html'
    queryset = Shipment.objects.all()