from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView)
from ..mixins import IndustryGenericView, IndustryFormView
from ....companies.models import Industry


class IndustryCreate(LoginRequiredMixin, IndustryFormView, CreateView):
    template_name = 'admin/industries/create.html'


class IndustryUpdate(LoginRequiredMixin, IndustryFormView, UpdateView):
    template_name = 'admin/industries/update.html'


class IndustryDelete(LoginRequiredMixin, IndustryGenericView, DeleteView):
    template_name = 'admin/industries/delete.html'


class IndustryDetail(LoginRequiredMixin, DetailView):
    template_name = 'admin/industries/detail.html'
    queryset = Industry.objects.all()


class IndustryList(LoginRequiredMixin, ListView):
    template_name = 'admin/industries/list.html'
    queryset = Industry.objects.all()
