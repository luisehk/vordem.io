from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from ...companies.models import Company, Industry


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "admin/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companies'] = Company.objects.all()
        context['industries'] = Industry.objects.all()
        return context
