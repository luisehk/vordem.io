from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from . import views

router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'profile', views.ProfileViewSet)
router.register(r'user-notifications', views.UserNotificationsConfigViewSet)

urlpatterns = [
    url(r'^me/$', views.MyselfView.as_view()),
]
urlpatterns += router.urls
