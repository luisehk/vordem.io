from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from ...companies.models import Company


class CompanyList(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'admin/companies/list.html'


class CompanyCreate(LoginRequiredMixin, CreateView):
    model = Company
    fields = ['name', 'industry', 'size']
    template_name = 'admin/companies/create.html'


class CompanyUpdate(LoginRequiredMixin, UpdateView):
    model = Company
    fields = ['name', 'industry', 'size', 'human_resources', 'leaders']
    template_name = 'admin/companies/update.html'


class CompanyDelete(LoginRequiredMixin, DeleteView):
    model = Company
    template_name = 'admin/companies/delete.html'
    success_url = reverse_lazy('admin:company-list')
