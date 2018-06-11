from rest_framework import serializers
from ..models import Skill
from .content import LessonSerializer


class SkillSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Skill
        fields = [
            'name', 'lessons'
        ]
