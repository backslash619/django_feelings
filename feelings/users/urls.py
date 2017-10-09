from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'logout/$',views.logout_view,name='logout'),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
]