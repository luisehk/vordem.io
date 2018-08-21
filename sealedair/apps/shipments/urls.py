from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from django.urls import reverse_lazy
from django.conf.urls import url
from .views.web.shipments import (
    Dashboard, ShipmentList, ShipmentCreate,
    ShipmentUpdate, ShipmentDelete)
from .views.rest.shipments import ShipmentViewSet

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

    url(r'^$', RedirectView.as_view(
        url=reverse_lazy('shipments:dashboard')
    ), name='index'),
]

router = DefaultRouter()
router.register(r'api/shipments', ShipmentViewSet)
urlpatterns += router.urls
