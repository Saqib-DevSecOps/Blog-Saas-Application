from django.urls import path

from src.accounts.public_accounts.views import PublicSignUpView

app_name = "public_accounts"
urlpatterns = [
    path('signup/', PublicSignUpView.as_view(),name="signup")

]
