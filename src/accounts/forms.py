from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import User

from src.tenant.models import Client, Domain


class ClientModelForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class CustomSignupForm(SignupForm):
    domain_name = forms.CharField(max_length=200)

    def save(self, request):
        name = self.cleaned_data['domain_name']
        schema = Client(schema_name=name)
        tenant = schema.save()
        domain = Domain()
        domain.domain = f"{name}.localhost"
        print(tenant)
        domain.tenant = tenant
        domain.is_primary = True
        domain.save()
        print(domain)
        return super(CustomSignupForm, self).save(request)
