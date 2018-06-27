from django.urls import reverse_lazy
from ...content.models import Intro, Video, Article, ActivityList


DEFAULT_LESSON_FIELDS = ['skill', 'name', 'body']


class LessonGenericView(object):
    def get_success_url(self):
        return reverse_lazy(
            'admin:skill-detail',
            args=(self.object.skill.id,))


class VideoGenericView(LessonGenericView):
    model = Video


class VideoFormView(VideoGenericView):
    fields = DEFAULT_LESSON_FIELDS + ['video_url']


class IntroGenericView(LessonGenericView):
    model = Intro


class IntroFormView(IntroGenericView):
    fields = DEFAULT_LESSON_FIELDS


class ArticleGenericView(LessonGenericView):
    model = Article


class ArticleFormView(ArticleGenericView):
    fields = DEFAULT_LESSON_FIELDS + ['description']


class ActivityListGenericView(LessonGenericView):
    model = ActivityList


class ActivityListFormView(ActivityListGenericView):
    fields = DEFAULT_LESSON_FIELDS


class ActivityForm(object):
    fields = ['title', 'description', 'body']
