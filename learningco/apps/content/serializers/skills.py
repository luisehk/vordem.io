from rest_framework import serializers
from ..models import Skill
from .content import (
    IntroSerializer, VideoSerializer, ArticleSerializer,
    ActivityListSerializer)


class SkillSerializer(serializers.ModelSerializer):
    intro = IntroSerializer()
    video = VideoSerializer()
    article = ArticleSerializer()
    activity_list = ActivityListSerializer()

    class Meta:
        model = Skill
        fields = [
            'name', 'intro', 'video', 'article', 'activity_list'
        ]
