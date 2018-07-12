from rest_framework.routers import DefaultRouter
from .views.rest.completion import (
    LessonCompletionViewSet, SkillCompletionViewSet)


urlpatterns = []

router = DefaultRouter()
router.register(r'lessons', LessonCompletionViewSet)
router.register(r'skills', SkillCompletionViewSet)
urlpatterns += router.urls
