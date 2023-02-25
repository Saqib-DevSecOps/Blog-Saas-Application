from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django_tenants.utils import schema_context, tenant_context
from src.tenant.models import Client, Domain
from django.contrib.auth.forms import UserCreationForm


class CustomSignupForm(forms.ModelForm):
    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    email = forms.EmailField(max_length=30,required=True)
    domain = forms.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'domain']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)

    def clean_domain(self):
        name = self.cleaned_data.get("domain")
        domain = Client.objects.filter(schema_name=name).exists()
        if domain:
            self.add_error("domain", "Domain Already registered")
        return name


class DomainFinderForm(forms.Form):
    domain = forms.CharField(max_length=200, label="Domain Name"
                             , widget=forms.TextInput(attrs={"placeholder": "Enter Subdomain Name"}))
