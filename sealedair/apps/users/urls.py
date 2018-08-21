from django.conf.urls import url
from .views import UsersList, UserCreate, UserUpdate, UserDelete

urlpatterns = [
    url(r'^list$',
        UsersList.as_view(), name="users-list"),
    url(r'^users/add/$',
        UserCreate.as_view(), name='users-add'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        UserUpdate.as_view(), name='users-update'),
    url(r'^users/(?P<pk>[0-9]+)/delete/$',
        UserDelete.as_view(), name='users-delete'),
]
