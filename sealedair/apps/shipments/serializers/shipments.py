from rest_framework import serializers
from ..models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = [
            'carrier', 'plant', 'code', 'current_status',
            'start_datetime', 'arrival_datetime',
            'estimated_arrival_datetime', 'delay_reason'
        ]
