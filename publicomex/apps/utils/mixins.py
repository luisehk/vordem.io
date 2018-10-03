from django.urls import reverse_lazy
from .exceptions import ConstraintsError
from django.db import ProgrammingError


class EditAfterSuccess(object):
    edit_reversable_url = ''

    def get_success_url(self):
        return reverse_lazy(
            self.edit_reversable_url,
            args=[self.object.id])


class CatchConstraintsErrorsOnCreate(object):
    def create(self, request):
        try:
            result = super().create(request)
            return result
        except ProgrammingError:
            raise ConstraintsError()
