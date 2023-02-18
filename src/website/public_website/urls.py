from django.urls import path

from src.website.public_website.views import HomeTemplateView

app_name = 'public_website'
urlpatterns = [
    path('', HomeTemplateView.as_view(),name="home")
]
