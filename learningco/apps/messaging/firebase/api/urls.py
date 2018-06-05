from rest_framework.routers import DefaultRouter
from .views import DevicesViewSet


router = DefaultRouter()
router.register(r'devices', DevicesViewSet)
urlpatterns = router.urls
