from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView
from django.core.urlresolvers import reverse

from . import forms


# Create your views here.
def dashboard(request):
    return render(request, 'users/dashboard.html')


def logout_view(request):
    logout(request)
