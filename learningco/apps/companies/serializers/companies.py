from rest_framework import serializers
from ..models import Company
from .industries import IndustrySerializer


class CompanySerializer(serializers.ModelSerializer):
    industry = IndustrySerializer()
    size = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ['id', 'name', 'industry', 'size']

    def get_size(self, obj):
        return obj.get_size_display()
