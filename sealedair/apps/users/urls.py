from django.conf.urls import url
from .views import UsersList, UserCreate

urlpatterns = [
    url(r'^list$',
        UsersList.as_view(), name="users-list"),
    url(r'^users/add/$',
        UserCreate.as_view(), name='users-add'),
    # url(r'^carriers/(?P<pk>[0-9]+)/$',
    #     CarrierUpdate.as_view(), name='carrier-update'),
    # url(r'^carriers/(?P<pk>[0-9]+)/delete/$',
    #     CarrierDelete.as_view(), name='carrier-delete'),

    # url(r'^$', RedirectView.as_view(
    #     url=reverse_lazy('providers:carrier-list')
    # ), name='index'),
]
