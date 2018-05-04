from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from ...companies.models import Industry


class IndustryCreate(LoginRequiredMixin, CreateView):
    model = Industry
    fields = ['name']
    template_name = 'admin/industries/create.html'
    success_url = reverse_lazy('admin:industry-list')


class IndustryUpdate(LoginRequiredMixin, UpdateView):
    model = Industry
    fields = ['name']
    template_name = 'admin/industries/update.html'
    success_url = reverse_lazy('admin:industry-list')


class IndustryDelete(LoginRequiredMixin, DeleteView):
    model = Industry
    template_name = 'admin/industries/delete.html'
    success_url = reverse_lazy('admin:industry-list')
