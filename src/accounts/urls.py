from django.urls import path

from src.accounts.views import ClientCreateView

app_name = "accounts"
urlpatterns = [
    path('client/', ClientCreateView.as_view(), name='client'),
]
