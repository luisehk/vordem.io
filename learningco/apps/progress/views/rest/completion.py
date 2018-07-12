from rest_framework.viewsets import ModelViewSet
from ...models import LessonCompletion
from ...serializers.completion import LessonCompletionSerializer


class LessonCompletionViewSet(ModelViewSet):
    queryset = LessonCompletion.objects.all()
    serializer_class = LessonCompletionSerializer
