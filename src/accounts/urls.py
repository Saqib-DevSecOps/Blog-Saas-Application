from django.urls import path

from src.accounts.views import LogoutCheck,LoginCheck

app_name = "accounts"
urlpatterns = [
    path('login_check', LoginCheck.as_view(), name='login_check'),
    path('logout-check/', LogoutCheck.as_view(), name='logout_check'),
]
