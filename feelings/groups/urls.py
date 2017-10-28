from django.conf.urls import url, include

from .views import company

companies_patterns = [
    url(r'^create/$', company.CreateView.as_view(), name='create'),
    url(r'^edit/(?P<slug>[\w]+)/$', company.UpdateView.as_view(), name="update"),
    url(r'^(?P<slug>[\w]+)/$', company.DetailView.as_view(), name='detail'),
]
urlpatterns = [
    url(r'^company/', include(companies_patterns, namespace='companies'))
]
