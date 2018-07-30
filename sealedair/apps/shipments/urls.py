from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.conf.urls import url
from .views.web.shipments import (
    Dashboard, ShipmentList, ShipmentCreate,
    ShipmentUpdate, ShipmentDelete)

urlpatterns = [
    url(r'^dashboard$',
        Dashboard.as_view(), name="dashboard"),
    url(r'^shipments$',
        ShipmentList.as_view(), name="shipment-list"),
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
