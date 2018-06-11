from rest_framework import serializers
from ..models import Skill
from .content import LessonPolymorphicSerializer


class SkillSerializer(serializers.ModelSerializer):
    lessons = LessonPolymorphicSerializer(many=True)

    class Meta:
        model = Skill
        fields = [
            'name', 'lessons'
        ]
