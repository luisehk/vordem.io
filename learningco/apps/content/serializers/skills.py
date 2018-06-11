from rest_framework import serializers
from ..models import Skill, Intro, Video, Article
from .content import IntroSerializer, VideoSerializer, ArticleSerializer


class SkillSerializer(serializers.ModelSerializer):
    intro = serializers.SerializerMethodField()
    video = serializers.SerializerMethodField()
    article = serializers.SerializerMethodField()

    class Meta:
        model = Skill
        fields = [
            'name', 'intro', 'video', 'article'
        ]

    def get_lesson(self, obj, model_class, serializer_class):
        data = model_class.objects.filter(skill=obj).last()

        if data:
            serializer = serializer_class(data)
            return serializer.data
        else:
            return None

    def get_intro(self, obj):
        return self.get_lesson(obj, Intro, IntroSerializer)

    def get_video(self, obj):
        return self.get_lesson(obj, Video, VideoSerializer)

    def get_article(self, obj):
        return self.get_lesson(obj, Article, ArticleSerializer)
