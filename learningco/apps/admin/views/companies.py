from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView)
from ...companies.models import Company


class CompanyList(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'admin/company_list.html'
