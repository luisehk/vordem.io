from rest_framework.viewsets import ModelViewSet
from ...serializers.carriers import CarrierSerializer
from ...models import Carrier


class CarrierViewSet(ModelViewSet):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer
