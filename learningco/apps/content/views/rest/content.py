from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ...serializers.skills import SkillSerializer
from ...models import Skill


class UserContent(APIView):
    def get(self, request, format=None):
        skills = Skill.objects.all()
        serializer = SkillSerializer(data=skills, many=True)
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_200_OK)
