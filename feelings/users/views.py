from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


# Create your views here.
def dashboard(request):
    return render(request, 'users/dashboard.html')


def logout_view(request):
    logout(request)


class SignupVoew(CreateView):
    form_class = UserCreationForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("home")