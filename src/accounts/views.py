from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView
from allauth.account.views import SignupView
from src.accounts.forms import ClientModelForm, CustomSignupForm
from src.tenant.models import Client, Domain


# Create your views here.

class LoginCheck(View):
    def get(self, request):
        if str(request.tenant) == "public":
            return redirect('/admin')
        print(request.tenant)


class LogoutCheck(View):
    def get(self, request, *args, **kwargs):
        if str(request.tenant) == "public":
            return redirect('account_login')
        return redirect("tenant_website:home")
