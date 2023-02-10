from django.urls import path

from src.website.views import HomeTemplateView

urlpatterns = [
    path('',HomeTemplateView.as_view())
]