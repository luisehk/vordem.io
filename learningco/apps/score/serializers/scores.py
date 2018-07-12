from rest_framework import serializers
from ..models import (
    LeaderScore, LeaderSkillScore,
    CompanyScore, CompanySkillScore,)


class LeaderScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderScore
        fields = [
            'id', 'leader_id',
            'score_before', 'score_now']


class LeaderSkillScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderSkillScore
        fields = [
            'id', 'leader_id', 'skill_id',
            'score_before', 'score_now']


class CompanyScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyScore
        fields = [
            'id', 'company_id',
            'score_before', 'score_now']


class CompanySkillScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanySkillScore
        fields = [
            'id', 'company_id', 'skill_id',
            'score_before', 'score_now']
