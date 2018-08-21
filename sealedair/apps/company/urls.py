from django.conf.urls import url
from .views.web.plants import (
    PlantList, PlantCreate, PlantUpdate, PlantDelete)

urlpatterns = [
    url(r'^plants$',
        PlantList.as_view(), name="plant-list"),
    url(r'^plants/add/$',
        PlantCreate.as_view(), name='plant-add'),
    url(r'^plants/(?P<pk>[0-9]+)/$',
        PlantUpdate.as_view(), name='plant-update'),
    url(r'^plants/(?P<pk>[0-9]+)/delete/$',
        PlantDelete.as_view(), name='plant-delete'),


]
