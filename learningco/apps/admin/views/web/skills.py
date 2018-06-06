from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView)
from ..mixins import SkillGenericView, SkillFormView
from ....content.models import Skill


class SkillCreate(LoginRequiredMixin, SkillFormView, CreateView):
    template_name = 'admin/skills/create.html'


class SkillUpdate(LoginRequiredMixin, SkillFormView, UpdateView):
    template_name = 'admin/skills/update.html'


class SkillDelete(LoginRequiredMixin, SkillGenericView, DeleteView):
    template_name = 'admin/skills/delete.html'


class SkillDetail(LoginRequiredMixin, DetailView):
    template_name = 'admin/skills/detail.html'
    queryset = Skill.objects.all()


class SkillList(LoginRequiredMixin, ListView):
    template_name = 'admin/skills/list.html'
    queryset = Skill.objects.all()
