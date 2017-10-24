from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView


def dashboard(request):
    return render(request, 'users/dashboard.html')


def logout_view(request):
    logout(request)


class SignupVoew(CreateView):
    form_class = UserCreationForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("home")
