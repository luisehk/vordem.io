from django.views.generic.base import RedirectView
from django.conf.urls import url
from .views import (
    Home, About, Services, Projects, Blog,
    Contact, RequestQuote, Careers, ApplyToJob,
    SingleArticle, SingleProject
)

app_name = 'website'

urlpatterns = [
    url(r'^home/$', Home.as_view(), name='home'),
    url(r'^about/$', About.as_view(), name='about'),
    url(r'^services/$', Services.as_view(), name='services'),
    url(r'^projects/$', Projects.as_view(), name='projects'),
    url(r'^blog/$', Blog.as_view(), name='blog'),
    url(r'^contact/$', Contact.as_view(), name='contact'),
    url(r'^quote/$', RequestQuote.as_view(), name='quote'),
    url(r'^careers/$', Careers.as_view(), name='careers'),
    url(r'^apply/$', ApplyToJob.as_view(), name='apply'),
    url(r'^project/$', SingleProject.as_view(), name='project'),
    url(r'^article/$', SingleArticle.as_view(), name='article'),
    url(r'^$', RedirectView.as_view(url='/home/'))
]
