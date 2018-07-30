from extra_views import CreateWithInlinesView, UpdateWithInlinesView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView
from django.views.generic.base import ContextMixin
from ...models import Plant


class PlantGenericView(LoginRequiredMixin, ContextMixin):
    model = Plant


class PlantFormView(PlantGenericView):
    fields = ['name', 'code', 'color']


class PlantCreate(PlantFormView, CreateWithInlinesView):  # noqa
    template_name = 'company/plants/create.html'


class PlantUpdate(PlantFormView, UpdateWithInlinesView):  # noqa
    template_name = 'company/plants/update.html'


class PlantDelete(PlantGenericView, DeleteView):
    template_name = 'company/plants/delete.html'


class PlantList(PlantGenericView, ListView):
    template_name = 'company/plants/list.html'
    queryset = Plant.objects.all()
