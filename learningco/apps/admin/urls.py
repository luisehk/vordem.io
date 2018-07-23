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
from .views.web.content import (
    Content01, Content02, Content03, Content04, Content05, Content06,
    Content07, Content08, Content09, Content10, Content11, Content12,
    Content13,)

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

    url(r'^bundles/add/$',
        BundleCreate.as_view(), name='bundle-add'),
    url(r'^bundles/detail/(?P<pk>[0-9]+)/$',
        BundleDetail.as_view(), name='bundle-detail'),
    url(r'^bundles/(?P<pk>[0-9]+)/$',
        BundleUpdate.as_view(), name='bundle-update'),
    url(r'^bundles/(?P<pk>[0-9]+)/delete/$',
        BundleDelete.as_view(), name='bundle-delete'),

    url(r'content/01$', Content01.as_view(), name='content-01'),
    url(r'content/02$', Content02.as_view(), name='content-02'),
    url(r'content/03$', Content03.as_view(), name='content-03'),
    url(r'content/04$', Content04.as_view(), name='content-04'),
    url(r'content/05$', Content05.as_view(), name='content-05'),
    url(r'content/06$', Content06.as_view(), name='content-06'),
    url(r'content/07$', Content07.as_view(), name='content-07'),
    url(r'content/08$', Content08.as_view(), name='content-08'),
    url(r'content/09$', Content09.as_view(), name='content-09'),
    url(r'content/10$', Content10.as_view(), name='content-10'),
    url(r'content/11$', Content11.as_view(), name='content-11'),
    url(r'content/12$', Content12.as_view(), name='content-12'),
    url(r'content/13$', Content13.as_view(), name='content-13'),

    url(r'^$', RedirectView.as_view(
        url=reverse_lazy('admin:skill-list')
    ), name='index'),
]
