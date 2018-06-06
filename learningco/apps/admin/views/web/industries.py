from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView)
from ..mixins import IndustryGenericView, IndustryFormView


class IndustryCreate(LoginRequiredMixin, IndustryFormView, CreateView):
    template_name = 'admin/industries/create.html'


class IndustryUpdate(LoginRequiredMixin, IndustryFormView, UpdateView):
    template_name = 'admin/industries/update.html'


class IndustryDelete(LoginRequiredMixin, IndustryGenericView, DeleteView):
    template_name = 'admin/industries/delete.html'
