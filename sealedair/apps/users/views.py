from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import RedirectView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import UserRegistroForm, UserUpdateForm


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


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "users/update.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy('users:users-list')


class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "users/delete.html"
    success_url = reverse_lazy('users:users-list')
