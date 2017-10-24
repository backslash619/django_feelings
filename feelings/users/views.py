from braces.views import SelectRelatedMixin
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views import generic


class DashboardView(LoginRequiredMixin,
                    generic.DeleteView,
                    SelectRelatedMixin):
    model = User
    select_related = ('thoughts',)
    template_name = "users/dashboard.html"

    def get_object(self, queryset=None):
        return self.request.user

def logout_view(request):
    logout(request)


class SignupVoew(generic.CreateView):
    form_class = UserCreationForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("home")
