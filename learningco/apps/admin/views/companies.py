from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.views.generic import (
    CreateView, UpdateView, DeleteView, DetailView)
from .mixins import CompanyGenericView, CompanyFormView
from ..serializers.companies import CompanyHumanResources
from ...companies.models import Company


class CompanyCreate(LoginRequiredMixin, CompanyFormView, CreateView):
    template_name = 'admin/companies/create.html'


class CompanyUpdate(LoginRequiredMixin, CompanyFormView, UpdateView):
    template_name = 'admin/companies/update.html'


class CompanyDelete(LoginRequiredMixin, CompanyGenericView, DeleteView):
    template_name = 'admin/companies/delete.html'


class CompanyDetail(LoginRequiredMixin, DetailView):
    template_name = 'admin/companies/detail.html'
    queryset = Company.objects.all()


class AddHumanResourcesToCompany(APIView):
    def post(self, request, format=None):
        serializer = CompanyHumanResources(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
