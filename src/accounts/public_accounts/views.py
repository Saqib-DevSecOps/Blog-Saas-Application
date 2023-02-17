from allauth.account.views import SignupView
from django.views.generic import CreateView

from src.accounts.public_accounts.forms import CustomSignupForm


class PublicSignUpView(CreateView):
    form_class = CustomSignupForm
    template_name = 'accounts/public_account/signup.html'
