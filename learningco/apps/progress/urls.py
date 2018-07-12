from rest_framework.routers import DefaultRouter
from .views.rest.completion import LessonCompletionViewSet


urlpatterns = []

router = DefaultRouter()
router.register(r'lessons', LessonCompletionViewSet)
urlpatterns += router.urls
