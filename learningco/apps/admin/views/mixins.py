from django.urls import reverse_lazy
from ...utils.mixins import EditAfterSuccess
from ...companies.models import Company, Industry
from ...content.models import Skill


class CompanyGenericView(object):
    model = Company
    success_url = reverse_lazy('admin:company-list')


class CompanyFormView(CompanyGenericView):
    fields = ['name', 'industry', 'size']


class IndustryGenericView(object):
    model = Industry
    success_url = reverse_lazy('admin:industry-list')


class IndustryFormView(IndustryGenericView):
    fields = ['name']


class SkillGenericView(object):
    model = Skill
    success_url = reverse_lazy('admin:skill-list')


class SkillFormView(SkillGenericView):
    fields = ['name']


class EditCompanyAfterSuccess(EditAfterSuccess):
    edit_reversable_url = 'admin:company-update'


class EditIndustryAfterSuccess(EditAfterSuccess):
    edit_reversable_url = 'admin:industry-update'
