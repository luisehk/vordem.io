from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from ...companies.models import Company


class CompanyList(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'admin/company_list.html'


class CompanyCreate(LoginRequiredMixin, CreateView):
    model = Company
    fields = ['name']
    template_name = 'admin/company_create.html'


class CompanyUpdate(LoginRequiredMixin, UpdateView):
    model = Company
    fields = ['name']
    template_name = 'admin/company_update.html'


class CompanyDelete(LoginRequiredMixin, DeleteView):
    model = Company
    template_name = 'admin/company_delete.html'
    success_url = reverse_lazy('admin:company-list')
