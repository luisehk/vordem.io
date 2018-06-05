from ..models import CustomDevice
from .serializers import DeviceSerializer
from rest_framework import viewsets


class DevicesViewSet(viewsets.ModelViewSet):
    queryset = CustomDevice.objects.all()
    serializer_class = DeviceSerializer
