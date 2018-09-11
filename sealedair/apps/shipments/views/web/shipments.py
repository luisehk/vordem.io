from extra_views import CreateWithInlinesView, UpdateWithInlinesView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView
from django.views.generic.base import ContextMixin, TemplateView
from django.db.models import F, Func
from django.db.models.functions import Coalesce
from django.db import models
from django.utils import timezone
from ...models import Shipment
from ....company.models import Plant
from datetime import timedelta


class ShipmentGenericView(LoginRequiredMixin, ContextMixin):
    model = Shipment


class ShipmentFormView(ShipmentGenericView):
    fields = ['name', 'code', 'color']


class Dashboard(ShipmentGenericView, TemplateView):
    template_name = 'shipments/dashboard.html'

    def _year_shipments(self, year):
        return Shipment.objects.filter(start_datetime__year=year)

    def _plant_shipments_metrics(self, plant, shipments):
        shipments_with_metrics = shipments.filter(
            plant=plant
        ).annotate(
            arrival=Coalesce(
                F('arrival_datetime'), timezone.now()
            )
        ).annotate(
            duration=Func(
                F('arrival'), models.F('start_datetime'), function='age')
        )

        return {
            'average_duration': (
                shipments_with_metrics.aggregate(
                    avg=models.Avg('duration'))['avg'] or timedelta(seconds=0)
            ).total_seconds() / 60 / 60 / 24,
            'count': shipments_with_metrics.count(),
            'percentage': int(((
                shipments_with_metrics.count() / shipments.count()
            ) if shipments.exists() else 1) * 100)
        }

    def get_plant_metrics(self, plant):
        current_year = timezone.now().year
        previous_year_shipments = self._year_shipments(current_year - 1)
        current_year_shipments = self._year_shipments(current_year)

        previous_year_metrics = self._plant_shipments_metrics(
            plant, previous_year_shipments)
        current_year_metrics = self._plant_shipments_metrics(
            plant, current_year_shipments)

        return {
            'id': plant.id,
            'code': plant.code,
            'color': plant.color,
            'name': plant.name,
            'previous_year_metrics': previous_year_metrics,
            'current_year_metrics': current_year_metrics
        }

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # todo:
        # - optimize
        # - move to ajax
        # - do it using subqueries
        ctx['plants'] = [
            self.get_plant_metrics(p)
            for p in Plant.objects.all()]

        ctx['badges'] = ['badge-danger', 'badge-warning', 'badge-success']
        return ctx


class ShipmentCreate(ShipmentFormView, CreateWithInlinesView):
    template_name = 'shipments/shipments/create.html'


class ShipmentUpdate(ShipmentFormView, UpdateWithInlinesView):
    template_name = 'shipments/shipments/update.html'


class ShipmentDelete(ShipmentGenericView, DeleteView):
    template_name = 'shipments/shipments/delete.html'


class ShipmentList(ShipmentGenericView, ListView):
    template_name = 'shipments/shipments/list.html'
    queryset = Shipment.objects.all()
