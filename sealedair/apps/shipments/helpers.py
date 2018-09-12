from django.db.models import F, Func
from django.db.models.functions import Coalesce
from django.db import models
from django.utils import timezone
from .models import Shipment
from ..company.models import Plant
from datetime import timedelta


def _year_shipments(year):
    return Shipment.objects.filter(start_datetime__year=year)


def _plant_shipments_metrics(plant, shipments):
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


def get_plant_metrics(plant):
    current_year = timezone.now().year
    previous_year_shipments = _year_shipments(current_year - 1)
    current_year_shipments = _year_shipments(current_year)

    previous_year_metrics = _plant_shipments_metrics(
        plant, previous_year_shipments)
    current_year_metrics = _plant_shipments_metrics(
        plant, current_year_shipments)

    return {
        'id': plant.id,
        'code': plant.code,
        'color': plant.color,
        'name': plant.name,
        'previous_year_metrics': previous_year_metrics,
        'current_year_metrics': current_year_metrics
    }


def get_all_plants_metrics():
    # todo:
    # - optimize
    # - do it using subqueries
    return [
        get_plant_metrics(p)
        for p in Plant.objects.all()]
