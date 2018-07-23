from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.conf.urls import url
from .views.rest.companies import (
    AddHumanResourcesToCompany, AddLeaderToCompany)
from .views.web.companies import (
    CompanyCreate, CompanyUpdate, CompanyDelete,
    CompanyDetail, CompanyList, CompanyLeaders)
from .views.web.leaders import (
    LeaderUpdate, LeaderDelete, LeaderDetail)
from .views.web.industries import (
    IndustryCreate, IndustryUpdate, IndustryDelete, IndustryList,
    IndustryDetail)
from .views.web.skills import (
    SkillCreate, SkillUpdate, SkillDelete, SkillList, SkillDetail)
from .views.web.bundles import (
    BundleCreate, BundleUpdate, BundleDelete, BundleDetail)

urlpatterns = [
    url(r'^companies$',
        CompanyList.as_view(), name="company-list"),
    url(r'^companies/add/$',
        CompanyCreate.as_view(), name='company-add'),
    url(r'^companies/detail/(?P<pk>[0-9]+)/$',
        CompanyDetail.as_view(), name='company-detail'),
    url(r'^companies/leaders/(?P<pk>[0-9]+)/$',
        CompanyLeaders.as_view(), name='company-leaders'),
    url(r'^companies/(?P<pk>[0-9]+)/$',
        CompanyUpdate.as_view(), name='company-update'),
    url(r'^companies/(?P<pk>[0-9]+)/delete/$',
        CompanyDelete.as_view(), name='company-delete'),
    url(r'^companies/add-hr/$',
        AddHumanResourcesToCompany.as_view(), name='company-add-hr'),
    url(r'^companies/add-leader/$',
        AddLeaderToCompany.as_view(), name='company-add-leader'),

    url(r'^industries$',
        IndustryList.as_view(), name="industry-list"),
    url(r'^industries/add/$',
        IndustryCreate.as_view(), name='industry-add'),
    url(r'^industries/detail/(?P<pk>[0-9]+)/$',
        IndustryDetail.as_view(), name='industry-detail'),
    url(r'^industries/(?P<pk>[0-9]+)/$',
        IndustryUpdate.as_view(), name='industry-update'),
    url(r'^industries/(?P<pk>[0-9]+)/delete/$',
        IndustryDelete.as_view(), name='industry-delete'),

    url(r'^leaders/detail/(?P<pk>[0-9]+)/$',
        LeaderDetail.as_view(), name='leader-detail'),
    url(r'^leaders/(?P<pk>[0-9]+)/$',
        LeaderUpdate.as_view(), name='leader-update'),
    url(r'^leaders/(?P<pk>[0-9]+)/delete/$',
        LeaderDelete.as_view(), name='leader-delete'),

    url(r'^skills$',
        SkillList.as_view(), name="skill-list"),
    url(r'^skills/add/$',
        SkillCreate.as_view(), name='skill-add'),
    url(r'^skills/detail/(?P<pk>[0-9]+)/$',
        SkillDetail.as_view(), name='skill-detail'),
    url(r'^skills/(?P<pk>[0-9]+)/$',
        SkillUpdate.as_view(), name='skill-update'),
    url(r'^skills/(?P<pk>[0-9]+)/delete/$',
        SkillDelete.as_view(), name='skill-delete'),

    url(r'^bundles/(?P<skill_pk>[0-9]+)/add/$',
        BundleCreate.as_view(), name='bundle-add'),
    url(r'^bundles/detail/(?P<pk>[0-9]+)/$',
        BundleDetail.as_view(), name='bundle-detail'),
    url(r'^bundles/(?P<pk>[0-9]+)/$',
        BundleUpdate.as_view(), name='bundle-update'),
    url(r'^bundles/(?P<pk>[0-9]+)/delete/$',
        BundleDelete.as_view(), name='bundle-delete'),

    url(r'^$', RedirectView.as_view(
        url=reverse_lazy('admin:skill-list')
    ), name='index'),
]
