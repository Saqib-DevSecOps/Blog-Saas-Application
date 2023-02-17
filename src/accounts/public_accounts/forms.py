from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django_tenants.utils import schema_context, tenant_context
from django_tenants.urlresolvers import reverse

from src.tenant.models import Client, Domain


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
    domain = forms.CharField(max_length=200)

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

    def clean_domain(self):
        name = self.cleaned_data.get("domain")
        domain = Client.objects.filter(schema_name=name).exists()
        if domain:
            self.add_error("domain", "Domain Already registered")
        return name

    def save(self, commit=True):
        name = self.cleaned_data.get("domain")
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password= self.cleaned_data.get("password1")
        tenant = Client.objects.create(schema_name=name)
        domain_name = f"{name}.localhost"
        domain = Domain.objects.create(domain=domain_name, tenant=tenant)
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        print(tenant)
        if commit:
            user.save()
            print("sace")
        with tenant_context(tenant):
            user = User.objects.create_superuser(username=username,email = email,password=password)
            print(user)
            return redirect(f"{name}:8000/")
