from rest_framework import serializers
from ..models import LessonCompletion, SkillCompletion


class LessonCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonCompletion
        fields = [
            'id', 'lesson',
            'completed', 'score']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user

        # save the object with the given user
        extra_data = {'leader': user}
        return super().create({**validated_data, **extra_data})  # noqa


class SkillCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCompletion
        fields = [
            'id', 'skill',
            'completed', 'score', 'comment']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user

        # save the object with the given user
        extra_data = {'leader': user}
        return super().create({**validated_data, **extra_data})  # noqa
