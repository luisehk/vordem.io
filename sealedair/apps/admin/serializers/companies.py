from rest_framework import serializers
from ...companies.models import Company
from ...users.helpers import invite_user


class CompanyHumanResources(serializers.Serializer):
    company_id = serializers.IntegerField(required=True)
    email = serializers.EmailField(required=True)

    def create(self, validated_data):
        # TODO: will clean this up later
        company = Company.objects.get(id=validated_data['company_id'])
        user = invite_user(validated_data['email'])
        company.human_resources.add(user)
        return validated_data


class CompanyLeader(serializers.Serializer):
    company_id = serializers.IntegerField(required=True)
    email = serializers.EmailField(required=True)

    def create(self, validated_data):
        # TODO: will clean this up later
        company = Company.objects.get(id=validated_data['company_id'])
        user = invite_user(validated_data['email'])
        company.leaders.add(user)
        return validated_data
