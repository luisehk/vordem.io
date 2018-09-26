from rest_framework.viewsets import ModelViewSet
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ...serializers.shipments import (
    ShipmentCreationSerializer, ShipmentSerializer,
    StatusDateSerializer, CommentSerializer)
from ...models import Shipment, Comment
from ...helpers import get_all_plants_metrics


class ShipmentViewSet(ModelViewSet):
    queryset = Shipment.objects.all()
    filter_fields = ('current_status__checkpoint',)
    ordering = (
        'arrival_datetime', 'start_datetime',
        'current_status', 'current_status__start_datetime')

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


class ShipmentMetricsPerPlant(APIView):
    def get(self, request):
        return Response(
            get_all_plants_metrics(),
            status=status.HTTP_200_OK)


class ShipmentNextCheckpoint(APIView):
    def get_object(self, pk):
        try:
            return Shipment.objects.get(pk=pk)
        except Shipment.DoesNotExist():
            raise Http404

    def serialize_data(self, shipment):
        serializer = ShipmentSerializer(shipment)
        return serializer.data

    def generate_response(self, serialized_data):
        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        shipment = self.get_object(pk)

        # previous status
        previous_status = shipment.current_status

        # advance to new status
        shipment.next_checkpoint()

        # set the start datetime for new status
        date_serializer = StatusDateSerializer(
            shipment.current_status, data=request.data, partial=True)
        date_serializer.is_valid(raise_exception=True)
        date_serializer.save()

        # update previous status new date, so it matches with specified date
        previous_status.end_datetime = shipment.current_status.start_datetime
        previous_status.save()

        # serialize data for the response
        serialized_data = self.serialize_data(shipment)
        return self.generate_response(serialized_data)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_fields = ('shipment',)
    ordering = ('-datetime')
