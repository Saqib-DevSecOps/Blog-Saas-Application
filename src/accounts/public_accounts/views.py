from allauth.account.views import SignupView
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django_tenants.utils import tenant_context

from src.accounts.public_accounts.forms import CustomSignupForm, DomainFinderForm
from src.tenant.models import Client, Domain


class PublicSignUpView(CreateView):
    form_class = CustomSignupForm
    template_name = 'accounts/public_account/signup.html'

    def form_valid(self, form):
        name = form.cleaned_data.get("domain")
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        tenant = Client.objects.create(schema_name=name)
        domain_name = f"{name}.localhost"
        domain = Domain.objects.create(domain=domain_name, tenant=tenant)
        user = User.objects.create_user(username=username, email=email, password=password)
        print("sace")
        with tenant_context(tenant):
            user = User.objects.create_superuser(username=username, email=email, password=password)
            url = f"http://{name}.localhost:8000/accounts/login/"
            return HttpResponseRedirect(url)


class DomainFinder(View):
    def get(self, *args, **kwargs):
        form = DomainFinderForm()
        context = {"form": form}
        return render(self.request, template_name='accounts/public_account/domain_finder.html', context=context)

    def post(self, request, *args, **kwargs):
        form = DomainFinderForm(request.POST)
        if form.is_valid():
            domain_name = form.cleaned_data.get('domain')
            domain = Client.objects.filter(schema_name=domain_name)
            if domain.exists():
                url = f"http://{domain_name}.localhost:8000/accounts/login/"
                return HttpResponseRedirect(url)
            messages.error(request, "Domain nor Found")
            return redirect("public_accounts:domain_finder")
