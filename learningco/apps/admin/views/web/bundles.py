from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView, DetailView)
# from django.shortcuts import redirect
from django.urls import reverse_lazy
from ....content.models import Bundle


class BundleGenericView(object):
    model = Bundle

    def get_success_url(self):
        return reverse_lazy(
            'admin:bundle-detail',
            args=(self.object.id,))


class BundleFormView(BundleGenericView):
    fields = [
        'skill', 'name', 'generation',
        'level_of_hierarchy', 'score_range']


class BundleCreate(LoginRequiredMixin, BundleFormView, CreateView):
    template_name = 'admin/bundles/create.html'


class BundleUpdate(LoginRequiredMixin, BundleFormView, UpdateView):
    template_name = 'admin/bundles/update.html'


class BundleDelete(LoginRequiredMixin, BundleGenericView, DeleteView):
    template_name = 'admin/bundles/delete.html'


class BundleDetail(LoginRequiredMixin, DetailView):
    template_name = 'admin/bundles/detail.html'
    queryset = Bundle.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
        # return redirect('content:intro-get-or-create', kwargs['pk'])
