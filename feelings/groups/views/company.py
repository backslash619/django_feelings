from braces.views import LoginRequiredMixin
from  braces.views import SetHeadlineMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.views import generic

from .. import forms


class CreateView(LoginRequiredMixin,
                 SetHeadlineMixin,
                 generic.CreateView):
    form_class = forms.CompanyForm
    headline = "Create New Company Group"
    success_url = reverse_lazy('users:dashboard')
    template_name = 'groups/companies/_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        self.object.members.add(self.request.user)
        return response


class UpdateView(LoginRequiredMixin,
                 SetHeadlineMixin,
                 generic.UpdateView):
    form_class = forms.CompanyForm
    template_name = 'groups/companies/_form.html'
    success_url = reverse_lazy('users:dashboard')

    def get_queryset(self):
        return self.request.user.companies.all()

    def get_headline(self):
        return 'Edit - {}'.format(self.object.name)

    def get_success_url(self):
        return reverse('groups:companies:detail', kwargs={
            'slug': self.object.slug
        })


class DetailView(LoginRequiredMixin,
                 SetHeadlineMixin,
                 generic.DetailView):
    form_class = forms.CompanyForm
    template_name = 'groups/companies/_detail.html'
    success_url = reverse_lazy('users:dashboard')

    def get_queryset(self):
        return self.request.user.companies.all()

    def get_headline(self):
        return 'Detail - {}'.format(self.object.name)
