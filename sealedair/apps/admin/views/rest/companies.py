from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ...serializers.companies import CompanyHumanResources, CompanyLeader


class AddHumanResourcesToCompany(APIView):
    def post(self, request, format=None):
        serializer = CompanyHumanResources(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddLeaderToCompany(APIView):
    def post(self, request, format=None):
        serializer = CompanyLeader(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
