from django.urls import path

from src.accounts.public_accounts.views import PublicSignUpView, DomainFinder

app_name = "public_accounts"
urlpatterns = [
    path('signup/', PublicSignUpView.as_view(), name="signup"),
    path('find-domain/', DomainFinder.as_view(), name="domain_finder"),
]
