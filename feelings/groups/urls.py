from django.conf.urls import url, include

from .views import company, family

companies_patterns = [
    url(r'^create/$', company.CreateView.as_view(), name='create'),
    url(r'^edit/(?P<slug>[-\w\d]+)/$', company.UpdateView.as_view(), name="update"),
    url(r'^(?P<slug>[-\w\d]+)/$', company.DetailView.as_view(), name='detail'),
]
families_patterns = [
    url(r'^create/$', family.CreateView.as_view(), name='create'),
    url(r'^edit/(?P<slug>[-\w\d]+)/$', family.UpdateView.as_view(), name="update"),
    url(r'^(?P<slug>[-\w\d]+)/$', family.DetailView.as_view(), name='detail'),
]
urlpatterns = [
    url(r'^company/', include(companies_patterns, namespace='companies')),
    url(r'^family/', include(families_patterns, namespace='families'))
]
