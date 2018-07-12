from rest_framework import serializers
from ..models import LessonCompletion


class LessonCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonCompletion
        fields = [
            'id', 'lesson_id', 'leader_id',
            'completed', 'score']
