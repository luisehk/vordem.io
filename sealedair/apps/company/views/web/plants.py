from extra_views import CreateWithInlinesView, UpdateWithInlinesView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView
from django.views.generic.base import ContextMixin
from ...models import Plant


class PlantGenericView(LoginRequiredMixin, ContextMixin):
    model = Plant

    def get_success_url(self):
        return reverse_lazy(
            'company:plant-list')


class PlantFormView(PlantGenericView):
    fields = ['name', 'code', 'color']


class PlantCreate(PlantFormView, CreateWithInlinesView):
    template_name = 'company/plants/create.html'


class PlantUpdate(PlantFormView, UpdateWithInlinesView):
    template_name = 'company/plants/update.html'


class PlantDelete(PlantGenericView, DeleteView):
    template_name = 'company/plants/delete.html'


class PlantList(PlantGenericView, ListView):
    template_name = 'company/plants/list.html'
    queryset = Plant.objects.all().order_by('pk')
