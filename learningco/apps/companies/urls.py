from rest_framework.routers import DefaultRouter
from .views.rest.companies import (
    CompanyViewSet,)


urlpatterns = []

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
urlpatterns += router.urls
