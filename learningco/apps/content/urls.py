from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.conf.urls import url
from .views.web.videos import (
    VideoCreate, VideoUpdate, VideoDelete
)
from .views.web.intros import (
    IntroCreate, IntroUpdate, IntroDelete
)
from .views.web.articles import (
    ArticleCreate, ArticleUpdate, ArticleDelete
)

urlpatterns = [
    url(r'^intros/add/$',
        IntroCreate.as_view(), name='intro-add'),
    url(r'^intros/(?P<pk>[0-9]+)/$',
        IntroUpdate.as_view(), name='intro-update'),
    url(r'^intros/(?P<pk>[0-9]+)/delete/$',
        IntroDelete.as_view(), name='intro-delete'),

    url(r'^articles/add/$',
        ArticleCreate.as_view(), name='article-add'),
    url(r'^articles/(?P<pk>[0-9]+)/$',
        ArticleUpdate.as_view(), name='article-update'),
    url(r'^articles/(?P<pk>[0-9]+)/delete/$',
        ArticleDelete.as_view(), name='article-delete'),

    url(r'^videos/add/$',
        VideoCreate.as_view(), name='video-add'),
    url(r'^videos/(?P<pk>[0-9]+)/$',
        VideoUpdate.as_view(), name='video-update'),
    url(r'^videos/(?P<pk>[0-9]+)/delete/$',
        VideoDelete.as_view(), name='video-delete'),

    url(r'^$', RedirectView.as_view(
        url=reverse_lazy('admin:skill-list')
    ), name='index'),
]
