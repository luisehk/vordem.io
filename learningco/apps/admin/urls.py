from django.conf.urls import url
from .views.companies import (
    CompanyList, CompanyCreate, CompanyUpdate, CompanyDelete
)
from .views.industries import (
    IndustryList, IndustryCreate, IndustryUpdate, IndustryDelete
)
from .views.admin import IndexView

urlpatterns = [
    url(r'^companies$',
        CompanyList.as_view(), name="company-list"),
    url(r'^companies/add/$',
        CompanyCreate.as_view(), name='company-add'),
    url(r'^companies/(?P<pk>[0-9]+)/$',
        CompanyUpdate.as_view(), name='company-update'),
    url(r'^companies/(?P<pk>[0-9]+)/delete/$',
        CompanyDelete.as_view(), name='company-delete'),

    url(r'^industries$',
        IndustryList.as_view(), name="industry-list"),
    url(r'^industries/add/$',
        IndustryCreate.as_view(), name='industry-add'),
    url(r'^industries/(?P<pk>[0-9]+)/$',
        IndustryUpdate.as_view(), name='industry-update'),
    url(r'^industries/(?P<pk>[0-9]+)/delete/$',
        IndustryDelete.as_view(), name='industry-delete'),

    url(r'^$', IndexView.as_view(), name='index'),
]
