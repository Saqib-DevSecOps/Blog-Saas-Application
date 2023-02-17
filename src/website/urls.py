from django.urls import path

from src.website.views import HomeTemplateView
app_name = 'website'
urlpatterns = [
    path('', HomeTemplateView.as_view(),name="home")
]
