from django.urls import reverse_lazy
from ...content.models import Intro, Video, Article


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


class IntroGenericView(LessonGenericView):
    model = Intro


class IntroFormView(IntroGenericView):
    fields = DEFAULT_LESSON_FIELDS


class ArticleGenericView(LessonGenericView):
    model = Article


class ArticleFormView(ArticleGenericView):
    fields = DEFAULT_LESSON_FIELDS + ['description']
