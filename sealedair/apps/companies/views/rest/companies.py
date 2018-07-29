from rest_framework.viewsets import ModelViewSet
from ...models import Company
from ...serializers.companies import (
    CompanySerializer,)


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
