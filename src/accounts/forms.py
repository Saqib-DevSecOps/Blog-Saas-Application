from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django_tenants.utils import tenant_context

from src.tenant.models import Client, Domain


class ClientModelForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class CustomSignupForm(SignupForm):
    domain_name = forms.CharField(max_length=200)

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
        with tenant_context(schema):
            user = User.objects.create_superuser(username=username, email=email, password=password1)
            user.is_active = True
            user.save()
        form = super(CustomSignupForm, self).save(request)
        return redirect(domain_url)
