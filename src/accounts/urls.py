from django.urls import path

from src.accounts.views import Login_Check

app_name = "accounts"
urlpatterns = [
    path('login-check', Login_Check.as_view(), name="login_check")
]
