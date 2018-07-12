from rest_framework.viewsets import ModelViewSet
from ...models import LessonCompletion, SkillCompletion
from ...serializers.completion import (
    LessonCompletionSerializer, SkillCompletionSerializer)


class LessonCompletionViewSet(ModelViewSet):
    queryset = LessonCompletion.objects.all()
    serializer_class = LessonCompletionSerializer


class SkillCompletionViewSet(ModelViewSet):
    queryset = SkillCompletion.objects.all()
    serializer_class = SkillCompletionSerializer
