from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django_tenants.utils import tenant_context
from django.utils.translation import gettext, gettext_lazy as _

from src.tenant.models import Client, Domain


class ClientModelForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class CustomSignupForm(SignupForm):
    domain_name = forms.CharField(max_length=200)

    def clean_domain_name(self):
        domain_name = self.cleaned_data['domain_name']
        domain = Client.objects.filter(schema_name=domain_name).exists()
        if domain:
            self.add_error(
                "domain_name",
                _("Domain name already register"),
            )
        return domain_name

    def save(self, request):
        name = self.cleaned_data['domain_name']
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        password1 = self.cleaned_data['password1']
        schema = Client(schema_name=name)
        tenant = schema.save()
        domain = Domain()
        domain.domain = f"{name}.localhost"
        domain_url = f"http://{name}.localhost:8000/"
        domain.tenant = schema
        domain.is_primary = True
        domain.save()
        form = super(CustomSignupForm, self).save(request)
        form.save()
        with tenant_context(schema):
            print("In")
            user = User.objects.create(username=username, email=email, password=password1)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            print("No Issue")
        return reverse('account_login')
