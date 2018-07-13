from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    UpdateView, DeleteView, DetailView)
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model


User = get_user_model()


class LeaderGenericView(object):
    model = User

    def get_success_url(self):
        return reverse_lazy(
            'admin:leader-detail',
            args=(self.object.id,))


class LeaderFormView(LeaderGenericView):
    fields = ['first_name', 'last_name']


class LeaderUpdate(LoginRequiredMixin, LeaderFormView, UpdateView):
    template_name = 'admin/leaders/update.html'


class LeaderDelete(LoginRequiredMixin, LeaderGenericView, DeleteView):
    template_name = 'admin/leaders/delete.html'


class LeaderDetail(LoginRequiredMixin, DetailView):
    template_name = 'admin/leaders/detail.html'
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        obj = self.object
        skl = obj.leader_skill_score.prefetch_related('skill').all()
        ctx['skill_scores'] = skl
        return ctx
