from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import RedirectView


class UserHome(LoginRequiredMixin, RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        return '/admin/'
