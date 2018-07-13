from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView

from ..api.serializers import UserSerializer, ProfileSerializer
from ..models import Profile


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MyselfView(APIView):
    queryset = User.objects.all()

    def get_queryset(self):
        u = self.request.user
        q = self.queryset

        return q.filter(
            id=u.id
        ) if u.is_authenticated else q.none()

    def get(self, request, format=None):
        return Response(
            UserSerializer(self.get_queryset().first(), many=False).data
        )
