from django.conf.urls import url
from .views.companies import CompanyList

urlpatterns = [
    url(r'^companies$', CompanyList.as_view(), name="company_list"),
]
