from django.urls import reverse_lazy
from ...content.models import Video


DEFAULT_LESSON_FIELDS = ['skill', 'name', 'body', 'default', 'thumbnail']


class LessonGenericView(object):
    def get_success_url(self):
        return reverse_lazy(
            'admin:skill-detail',
            args=(self.object.skill.id,))


class VideoGenericView(LessonGenericView):
    model = Video


class VideoFormView(VideoGenericView):
    fields = ['skill', 'name', 'body', 'default', 'video_url']
