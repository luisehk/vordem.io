from rest_framework.viewsets import ModelViewSet
from ...serializers.shipments import (
    ShipmentCreationSerializer, ShipmentSerializer)
from ...models import Shipment


class ShipmentViewSet(ModelViewSet):
    queryset = Shipment.objects.all()
    filter_fields = ('current_status__checkpoint',)

    def get_serializer_class(self):
        if self.action == 'list':
            return ShipmentSerializer
        elif self.action == 'retrieve':
            return ShipmentSerializer
        elif self.action == 'create':
            return ShipmentCreationSerializer
        elif self.action == 'update':
            return ShipmentSerializer
        else:
            return ShipmentSerializer
