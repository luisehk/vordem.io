from django.urls import reverse_lazy
from ...utils.mixins import EditAfterSuccess
from ...content.models import Video


DEFAULT_LESSON_FIELDS = ['skill', 'name', 'body', 'default', 'thumbnail']


class VideoGenericView(object):
    model = Video

    def get_success_url(self):
        return reverse_lazy('admin:skill-detail', args=(self.object.skill.id,))


class VideoFormView(VideoGenericView):
    fields = ['skill', 'name', 'body', 'default', 'video_url']


class EditVideoAfterSuccess(EditAfterSuccess):
    edit_reversable_url = 'content:video-update'


class EditIndustryAfterSuccess(EditAfterSuccess):
    edit_reversable_url = 'content:industry-update'
