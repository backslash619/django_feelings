from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'logout/$',views.logout_view,name='logout'),
    url(r'signup/$', views.SignupVoew.as_view(), name='signup'),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
]