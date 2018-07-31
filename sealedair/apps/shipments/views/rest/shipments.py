from rest_framework.viewsets import ModelViewSet
from ...serializers.shipments import ShipmentSerializer
from ...models import Shipment


class ShipmentViewSet(ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
