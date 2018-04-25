from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'profile', views.ProfileViewSet)

urlpatterns = []
urlpatterns += router.urls
