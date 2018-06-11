from rest_polymorphic.serializers import PolymorphicSerializer
from rest_framework import serializers
from ..models import Intro, Video, Article, ActivityList, Quiz


DEFAULT_LESSON_FIELDS = ['id', 'name', 'body']


class IntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intro
        fields = DEFAULT_LESSON_FIELDS


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = DEFAULT_LESSON_FIELDS + ['video_url']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = DEFAULT_LESSON_FIELDS + ['description']


class ActivityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityList
        fields = DEFAULT_LESSON_FIELDS


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = DEFAULT_LESSON_FIELDS


class LessonPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Intro: IntroSerializer,
        Video: VideoSerializer,
        Article: ArticleSerializer,
        ActivityList: ActivityListSerializer,
        Quiz: QuizSerializer
    }
