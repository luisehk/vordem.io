from rest_framework import serializers
from ..models import Company
from .industries import IndustrySerializer
from ...score.serializers.scores import CompanyScoreSerializer


class CompanySerializer(serializers.ModelSerializer):
    industry = IndustrySerializer()
    size = serializers.SerializerMethodField()
    company_score = CompanyScoreSerializer(read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'industry', 'size', 'company_score']

    def get_size(self, obj):
        return obj.get_size_display()
