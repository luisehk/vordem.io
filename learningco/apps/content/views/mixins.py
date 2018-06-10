from django.urls import reverse_lazy
from ...utils.mixins import EditAfterSuccess
from ...content.models import Video


DEFAULT_LESSON_FIELDS = ['skill', 'name', 'body', 'default', 'thumbnail']


class VideoGenericView(object):
    model = Video
    success_url = reverse_lazy('content:video-list')


class VideoFormView(VideoGenericView):
    fields = ['skill', 'name', 'body', 'default', 'video_url']


class EditVideoAfterSuccess(EditAfterSuccess):
    edit_reversable_url = 'content:video-update'


class EditIndustryAfterSuccess(EditAfterSuccess):
    edit_reversable_url = 'content:industry-update'
