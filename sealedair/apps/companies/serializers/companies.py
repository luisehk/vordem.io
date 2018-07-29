from rest_framework import serializers
from ..models import Company
from .industries import IndustrySerializer
from ...score.serializers.scores import CompanyScoreSerializer
from ...utils.serializers import BetterVersatileImageFieldSerializer


class CompanySerializer(serializers.ModelSerializer):
    avatar = BetterVersatileImageFieldSerializer(sizes='company_avatar')
    industry = IndustrySerializer(read_only=True)
    size = serializers.SerializerMethodField()
    company_score = CompanyScoreSerializer(read_only=True)

    class Meta:
        model = Company
        fields = [
            'id', 'avatar', 'name',
            'industry', 'size', 'company_score']

    def get_size(self, obj):
        return obj.get_size_display()
