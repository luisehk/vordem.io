from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from .views.web.videos import (
    VideoCreate, VideoUpdate, VideoDelete,
    VideoGetOrCreate
)
from .views.web.intros import (
    IntroCreate, IntroUpdate, IntroDelete,
    IntroGetOrCreate
)
from .views.web.articles import (
    ArticleCreate, ArticleUpdate, ArticleDelete,
    ArticleGetOrCreate
)
from .views.web.activities import (
    ActivityListCreate, ActivityListUpdate, ActivityListDelete,
    ActivityListGetOrCreate
)
from .views.web.quizzes import (
    QuizCreate, QuizUpdate, QuizDelete,
    QuizGetOrCreate
)
from .views.rest.content import UserContent, OptionViewSet

urlpatterns = [
    url(r'^intros/(?P<skill_pk>[0-9]+)/add/$',
        IntroCreate.as_view(), name='intro-add'),
    url(r'^intros/(?P<skill_pk>[0-9]+)/get_or_create/$',
        IntroGetOrCreate.as_view(), name='intro-get-or-create'),
    url(r'^intros/(?P<pk>[0-9]+)/$',
        IntroUpdate.as_view(), name='intro-update'),
    url(r'^intros/(?P<pk>[0-9]+)/delete/$',
        IntroDelete.as_view(), name='intro-delete'),

    url(r'^articles/(?P<skill_pk>[0-9]+)/add/$',
        ArticleCreate.as_view(), name='article-add'),
    url(r'^articles/(?P<skill_pk>[0-9]+)/get_or_create/$',
        ArticleGetOrCreate.as_view(), name='article-get-or-create'),
    url(r'^articles/(?P<pk>[0-9]+)/$',
        ArticleUpdate.as_view(), name='article-update'),
    url(r'^articles/(?P<pk>[0-9]+)/delete/$',
        ArticleDelete.as_view(), name='article-delete'),

    url(r'^videos/(?P<skill_pk>[0-9]+)/add/$',
        VideoCreate.as_view(), name='video-add'),
    url(r'^videos/(?P<skill_pk>[0-9]+)/get_or_create/$',
        VideoGetOrCreate.as_view(), name='video-get-or-create'),
    url(r'^videos/(?P<pk>[0-9]+)/$',
        VideoUpdate.as_view(), name='video-update'),
    url(r'^videos/(?P<pk>[0-9]+)/delete/$',
        VideoDelete.as_view(), name='video-delete'),

    url(r'^activities/(?P<skill_pk>[0-9]+)/add/$',
        ActivityListCreate.as_view(), name='activity-add'),
    url(r'^activities/(?P<skill_pk>[0-9]+)/get_or_create/$',
        ActivityListGetOrCreate.as_view(), name='activity-get-or-create'),
    url(r'^activities/(?P<pk>[0-9]+)/$',
        ActivityListUpdate.as_view(), name='activity-update'),
    url(r'^activities/(?P<pk>[0-9]+)/delete/$',
        ActivityListDelete.as_view(), name='activity-delete'),

    url(r'^quizzes/(?P<skill_pk>[0-9]+)/add/$',
        QuizCreate.as_view(), name='quiz-add'),
    url(r'^quizzes/(?P<skill_pk>[0-9]+)/get_or_create/$',
        QuizGetOrCreate.as_view(), name='quiz-get-or-create'),
    url(r'^quizzes/(?P<pk>[0-9]+)/$',
        QuizUpdate.as_view(), name='quiz-update'),
    url(r'^quizzes/(?P<pk>[0-9]+)/delete/$',
        QuizDelete.as_view(), name='quiz-delete'),

    url(r'^user-content/$',
        UserContent.as_view(), name='user-content'),

    url(r'^$', RedirectView.as_view(
        url=reverse_lazy('admin:skill-list')
    ), name='index'),
]

router = DefaultRouter()
router.register(r'options', OptionViewSet)
urlpatterns += router.urls
