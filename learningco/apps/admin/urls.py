from django.conf.urls import url
from .views.companies import (
    CompanyList, CompanyCreate, CompanyUpdate, CompanyDelete
)

urlpatterns = [
    url(r'^companies$',
        CompanyList.as_view(), name="company-list"),
    url(r'^companies/add/$',
        CompanyCreate.as_view(), name='company-add'),
    url(r'^companies/(?P<pk>[0-9]+)/$',
        CompanyUpdate.as_view(), name='company-update'),
    url(r'^companies/(?P<pk>[0-9]+)/delete/$',
        CompanyDelete.as_view(), name='company-delete'),
]
