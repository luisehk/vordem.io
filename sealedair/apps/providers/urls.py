from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views.web.carriers import (
    CarrierList, CarrierCreate, CarrierUpdate, CarrierDelete)
from .views.rest.carriers import CarrierViewSet

urlpatterns = [
    url(r'^carriers$',
        CarrierList.as_view(), name="carrier-list"),
    url(r'^carriers/add/$',
        CarrierCreate.as_view(), name='carrier-add'),
    url(r'^carriers/(?P<pk>[0-9]+)/$',
        CarrierUpdate.as_view(), name='carrier-update'),
    url(r'^carriers/(?P<pk>[0-9]+)/delete/$',
        CarrierDelete.as_view(), name='carrier-delete'),

    url(r'^$', RedirectView.as_view(
        url=reverse_lazy('providers:carrier-list')
    ), name='index'),
]

router = DefaultRouter()
router.register(r'^api/carriers$', CarrierViewSet)
urlpatterns += router.urls
