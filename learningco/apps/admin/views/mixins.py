from django.urls import reverse_lazy
from ...utils.mixins import EditAfterSuccess
from ...companies.models import Company


class CompanyGenericView(object):
    model = Company
    success_url = reverse_lazy('admin:company-list')


class CompanyFormView(CompanyGenericView):
    fields = ['name', 'industry', 'size']


class EditCompanyAfterSuccess(EditAfterSuccess):
    edit_reversable_url = 'admin:company-update'


class EditIndustryAfterSuccess(EditAfterSuccess):
    edit_reversable_url = 'admin:industry-update'
