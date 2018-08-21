from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import RedirectView
from django.views.generic import ListView


User = get_user_model()


class UserHome(LoginRequiredMixin, RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        return '/shipments/'


class UsersList(LoginRequiredMixin, ListView):
    model = User
    template_name = "users/list.html"
