from rest_framework.viewsets import ModelViewSet
from ...serializers.plants import PlantSerializer
from ...models import Plant


class PlantViewSet(ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
