from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views.web.plants import (
    PlantList, PlantCreate, PlantUpdate, PlantDelete)
from .views.rest.plants import PlantViewSet


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

router = DefaultRouter()
router.register(r'api/plants', PlantViewSet, base_name='plant-api')
urlpatterns += router.urls
