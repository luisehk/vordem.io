from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView)
from .mixins import CompanyGenericView, CompanyFormView


class CompanyCreate(LoginRequiredMixin, CompanyFormView, CreateView):
    template_name = 'admin/companies/create.html'


class CompanyUpdate(LoginRequiredMixin, CompanyFormView, UpdateView):
    template_name = 'admin/companies/update.html'


class CompanyDelete(LoginRequiredMixin, CompanyGenericView, DeleteView):
    template_name = 'admin/companies/delete.html'
