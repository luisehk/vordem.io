from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin
from django.views.generic import DeleteView, DetailView
from extra_views import CreateWithInlinesView, UpdateWithInlinesView
# from django.shortcuts import redirect
from django.urls import reverse_lazy
from ....content.models import Bundle, Skill


class BundleGenericView(ContextMixin):
    model = Bundle

    def get_success_url(self):
        return reverse_lazy(
            'admin:bundle-detail',
            args=(self.object.id,))

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        if 'skill_pk' in kwargs:
            ctx['skill'] = self.get_skill(kwargs['skill_pk'])
        else:
            ctx['skill'] = self.object.skill

        return ctx

    def get_skill(self, skill_pk):
        return Skill.objects.get(pk=skill_pk)


class BundleFormView(BundleGenericView):
    fields = [
        'skill', 'name', 'generation',
        'level_of_hierarchy', 'score_range']


class BundleCreate(LoginRequiredMixin, BundleFormView, CreateWithInlinesView):
    template_name = 'admin/bundles/create.html'


class BundleUpdate(LoginRequiredMixin, BundleFormView, UpdateWithInlinesView):
    template_name = 'admin/bundles/update.html'


class BundleDelete(LoginRequiredMixin, BundleGenericView, DeleteView):
    template_name = 'admin/bundles/delete.html'


class BundleDetail(LoginRequiredMixin, DetailView):
    template_name = 'admin/bundles/detail.html'
    queryset = Bundle.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
        # return redirect('content:intro-get-or-create', kwargs['pk'])
