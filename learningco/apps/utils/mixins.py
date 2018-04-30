from django.urls import reverse_lazy


class EditAfterSuccess(object):
    edit_reversable_url = ''

    def get_success_url(self):
        return reverse_lazy(
            self.edit_reversable_url,
            args=[self.object.id])
