from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from allauth.account.views import SignupView
from src.accounts.forms import ClientModelForm, CustomSignupForm
from src.tenant.models import Client, Domain


# Create your views here.

class ClientCreateView(View):
    def get(self, request):
        form = ClientModelForm()
        return render(request, 'accounts/client.html',
                      context={'form': form})

    def post(self, request):
        tenant_form = ClientModelForm(request.POST)
        if tenant_form.is_valid():
            name = tenant_form.cleaned_data.get('name')
            tenant = tenant_form.save()
            domain = Domain()
            print(name)
            domain.domain = name
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()
        return HttpResponse('error')
