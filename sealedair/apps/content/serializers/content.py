from rest_polymorphic.serializers import PolymorphicSerializer
from rest_framework import serializers
from crum import get_current_request
from ...progress.models import LessonCompletion
from ..models import (
    Intro, Video, Article,
    ActivityList, Activity,
    Quiz, Question, Option,
)


BASE_LESSON_FIELDS = ['id', 'lesson_ptr_id', 'name']
FULL_LESSON_FIELDS = BASE_LESSON_FIELDS + ['body']
DEFAULT_LESSON_FIELDS = FULL_LESSON_FIELDS


def _get_leader_lesson_completion(obj):
    request = get_current_request()
    user = request.user

    completion = LessonCompletion.objects.filter(
        leader=user, lesson=obj)

    return completion.exists()


class IntroSerializer(serializers.ModelSerializer):
    leader_lesson_completion = serializers.SerializerMethodField()

    class Meta:
        model = Intro
        fields = FULL_LESSON_FIELDS + [
            'leader_lesson_completion']

    def get_leader_lesson_completion(self, obj):
        return _get_leader_lesson_completion(obj)


class VideoSerializer(serializers.ModelSerializer):
    leader_lesson_completion = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = FULL_LESSON_FIELDS + [
            'video_url'
        ] + ['leader_lesson_completion']

    def get_leader_lesson_completion(self, obj):
        return _get_leader_lesson_completion(obj)


class ArticleSerializer(serializers.ModelSerializer):
    leader_lesson_completion = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = FULL_LESSON_FIELDS + [
            'leader_lesson_completion']

    def get_leader_lesson_completion(self, obj):
        return _get_leader_lesson_completion(obj)


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name', 'description', 'body']


class ActivityListSerializer(serializers.ModelSerializer):
    leader_lesson_completion = serializers.SerializerMethodField()
    activities = ActivitySerializer(many=True)

    class Meta:
        model = ActivityList
        fields = BASE_LESSON_FIELDS + [
            'activities'
        ] + ['leader_lesson_completion']

    def get_leader_lesson_completion(self, obj):
        return _get_leader_lesson_completion(obj)


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'name', 'question_id']


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'name', 'options']


class QuizSerializer(serializers.ModelSerializer):
    leader_lesson_completion = serializers.SerializerMethodField()
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = BASE_LESSON_FIELDS + [
            'questions'
        ] + ['leader_lesson_completion']

    def get_leader_lesson_completion(self, obj):
        return _get_leader_lesson_completion(obj)


class LessonPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Intro: IntroSerializer,
        Video: VideoSerializer,
        Article: ArticleSerializer,
        ActivityList: ActivityListSerializer,
        Quiz: QuizSerializer
    }
