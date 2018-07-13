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

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        obj = self.object
        skl = obj.company_skill_scores.prefetch_related('skill').all()
        ctx['skill_scores'] = skl
        return ctx


class CompanyLeaders(LoginRequiredMixin, DetailView):
    template_name = 'admin/companies/leaders.html'
    queryset = Company.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        obj = self.object
        leaders = obj.leaders.prefetch_related('profile').all()
        ctx['leaders'] = leaders
        return ctx


class CompanyList(LoginRequiredMixin, ListView):
    template_name = 'admin/companies/list.html'
    queryset = Company.objects.all()
