from rest_framework.viewsets import ModelViewSet
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ...serializers.shipments import (
    ShipmentCreationSerializer, ShipmentSerializer, CommentSerializer)
from ...models import Shipment, Comment
from ...helpers import get_all_plants_metrics


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

    def post(self, request, pk):
        shipment = self.get_object(pk)
        shipment.next_checkpoint()

        return Response(
            {'success': "success"},
            status=status.HTTP_200_OK)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
