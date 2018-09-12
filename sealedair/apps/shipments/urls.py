from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from django.urls import reverse_lazy
from django.conf.urls import url
from .views.web.shipments import (
    Dashboard, ShipmentList, ShipmentCreate,
    ShipmentUpdate, ShipmentDelete)
from .views.web.delay_reason import (
    DelayReasonList, DelayReasonCreate, DelayReasonUpdate, DelayReasonDelete)
from .views.rest.shipments import (
    ShipmentViewSet, ShipmentNextCheckpoint, ShipmentMetricsPerPlant)

urlpatterns = [
    url(r'^dashboard$',
        Dashboard.as_view(), name="dashboard"),
    url(r'^shipments$',
        ShipmentList.as_view(), name="shipment-listar"),
    url(r'^shipments/add/$',
        ShipmentCreate.as_view(), name='shipment-add'),
    url(r'^shipments/(?P<pk>[0-9]+)/$',
        ShipmentUpdate.as_view(), name='shipment-update'),
    url(r'^shipments/(?P<pk>[0-9]+)/delete/$',
        ShipmentDelete.as_view(), name='shipment-delete'),
    url(r'^shipments/(?P<pk>[0-9]+)/next/$',
        ShipmentNextCheckpoint.as_view(), name='shipment-next'),
    url(r'^shipments/metrics-per-plant/$',
        ShipmentMetricsPerPlant.as_view(), name='shipment-plant-metrics'),

    url(r'^delay-reason$',
        DelayReasonList.as_view(), name="delay-reason-list"),
    url(r'^delay-reason/add/$',
        DelayReasonCreate.as_view(), name="delay-reason-add"),
    url(r'^delay-reason/(?P<pk>[0-9]+)/$',
        DelayReasonUpdate.as_view(), name="delay-reason-update"),
    url(r'^delay-reason/(?P<pk>[0-9]+)/delete/$',
        DelayReasonDelete.as_view(), name="delay-reason-delete"),

    url(r'^$', RedirectView.as_view(
        url=reverse_lazy('shipments:dashboard')
    ), name='index'),
]

router = DefaultRouter()
router.register(r'api/shipments', ShipmentViewSet)
urlpatterns += router.urls
