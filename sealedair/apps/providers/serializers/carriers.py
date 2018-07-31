from rest_framework import serializers
from ..models import Carrier, Truck


class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = [
            'id', 'name', 'code', 'color'
        ]


class TruckSerializer(serializers.ModelSerializer):
    carrier = CarrierSerializer()

    class Meta:
        model = Truck
        fields = [
            'id', 'code', 'carrier'
        ]
