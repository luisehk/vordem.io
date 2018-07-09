from rest_polymorphic.serializers import PolymorphicSerializer
from rest_framework import serializers
from ..models import (
    Intro, Video, Article,
    ActivityList, Activity,
    Quiz, Question, Option,
)


BASE_LESSON_FIELDS = ['id', 'name']
FULL_LESSON_FIELDS = ['id', 'name', 'body']
DEFAULT_LESSON_FIELDS = FULL_LESSON_FIELDS


class IntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intro
        fields = FULL_LESSON_FIELDS


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = FULL_LESSON_FIELDS + ['video_url']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = FULL_LESSON_FIELDS


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = FULL_LESSON_FIELDS


class ActivityListSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True)

    class Meta:
        model = ActivityList
        fields = BASE_LESSON_FIELDS + ['activities']


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = BASE_LESSON_FIELDS


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = BASE_LESSON_FIELDS + ['options']


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = BASE_LESSON_FIELDS + ['questions']


class LessonPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Intro: IntroSerializer,
        Video: VideoSerializer,
        Article: ArticleSerializer,
        ActivityList: ActivityListSerializer,
        Quiz: QuizSerializer
    }
