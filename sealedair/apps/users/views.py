from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import RedirectView
from django.views.generic import ListView, CreateView
from .forms import UserRegistroForm


User = get_user_model()


class UserHome(LoginRequiredMixin, RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        return '/shipments/'


class UsersList(LoginRequiredMixin, ListView):
    model = User
    template_name = "users/list.html"


class UserCreate(LoginRequiredMixin, CreateView):
    model = User
    template_name = "users/create.html"
    form_class = UserRegistroForm
    success_url = reverse_lazy('users:users-list')
