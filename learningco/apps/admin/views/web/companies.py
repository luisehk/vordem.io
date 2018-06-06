from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView,
    DetailView, ListView)
from ..mixins import CompanyGenericView, CompanyFormView
from ....companies.models import Company


class CompanyCreate(LoginRequiredMixin, CompanyFormView, CreateView):
    template_name = 'admin/companies/create.html'


class CompanyUpdate(LoginRequiredMixin, CompanyFormView, UpdateView):
    template_name = 'admin/companies/update.html'


class CompanyDelete(LoginRequiredMixin, CompanyGenericView, DeleteView):
    template_name = 'admin/companies/delete.html'


class CompanyDetail(LoginRequiredMixin, DetailView):
    template_name = 'admin/companies/detail.html'
    queryset = Company.objects.all()


class CompanyList(LoginRequiredMixin, ListView):
    template_name = 'admin/companies/list.html'
    queryset = Company.objects.all()
