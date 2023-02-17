from django.urls import path

from src.website.views import HomeTemplateView, home

app_name = 'tenant_website'
urlpatterns = [
    path('', home, name="home")
]
