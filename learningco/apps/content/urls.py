from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.conf.urls import url
from .views.web.videos import (
    VideoCreate, VideoUpdate, VideoDelete, VideoList, VideoDetail
)

urlpatterns = [
    url(r'^videos$',
        VideoList.as_view(), name="video-list"),
    url(r'^videos/add/$',
        VideoCreate.as_view(), name='video-add'),
    url(r'^videos/detail/(?P<pk>[0-9]+)/$',
        VideoDetail.as_view(), name='video-detail'),
    url(r'^videos/(?P<pk>[0-9]+)/$',
        VideoUpdate.as_view(), name='video-update'),
    url(r'^videos/(?P<pk>[0-9]+)/delete/$',
        VideoDelete.as_view(), name='video-delete'),

    url(r'^$', RedirectView.as_view(
        url=reverse_lazy('admin:skill-list')
    ), name='index'),
]
