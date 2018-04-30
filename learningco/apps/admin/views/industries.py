from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .mixins import EditIndustryAfterSuccess
from ...companies.models import Industry


class IndustryList(LoginRequiredMixin, ListView):
    model = Industry
    template_name = 'admin/industries/list.html'


class IndustryCreate(LoginRequiredMixin, EditIndustryAfterSuccess, CreateView):
    model = Industry
    fields = ['name']
    template_name = 'admin/industries/create.html'


class IndustryUpdate(LoginRequiredMixin, EditIndustryAfterSuccess, UpdateView):
    model = Industry
    fields = ['name']
    template_name = 'admin/industries/update.html'


class IndustryDelete(LoginRequiredMixin, DeleteView):
    model = Industry
    template_name = 'admin/industries/delete.html'
    success_url = reverse_lazy('admin:industry-list')
