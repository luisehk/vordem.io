from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.views.generic.base import RedirectView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import UserRegistroForm, UserProfileForm
from allauth.account.views import PasswordChangeView


User = get_user_model()


class UserHome(LoginRequiredMixin, RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        return '/shipments/'


class UsersList(LoginRequiredMixin, ListView):
    model = User
    template_name = "users/list.html"
    ordering = ['pk']


class UserCreate(LoginRequiredMixin, CreateView):
    model = User
    template_name = "users/create.html"
    form_class = UserRegistroForm
    success_url = reverse_lazy('users:users-list')

    def form_invalid(self, form):
        messages.error(
            self.request, "Ese email ya fue registrado.")
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
            print("Ya existe el email.", user)
            return self.form_invalid(form)
        except ObjectDoesNotExist:
            return super().form_valid(form)


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "users/update.html"
    form_class = UserProfileForm
    success_url = reverse_lazy('users:users-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(instance={
            'user': self.object,
            'profile': self.object.profile,
        })
        return kwargs

    def get(self, request, *args, **kwargs):
        if self.request.user == self.get_object():
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/users/list')


class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "users/delete.html"
    success_url = reverse_lazy('users:users-list')


class LoginAfterPasswordChangeView(PasswordChangeView):
    """
    Custom class to override the password change view.
    """
    @property
    def success_url(self):
        return reverse_lazy('shipments:dashboard')


login_after_password_change = login_required(
    LoginAfterPasswordChangeView.as_view())
