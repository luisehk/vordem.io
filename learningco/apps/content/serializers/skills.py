from rest_framework import serializers
from ..models import Skill
from .content import IntroSerializer, VideoSerializer, ArticleSerializer


class SkillSerializer(serializers.ModelSerializer):
    intro = IntroSerializer()
    video = VideoSerializer()
    article = ArticleSerializer()

    class Meta:
        model = Skill
        fields = [
            'name', 'intro', 'video', 'article'
        ]
