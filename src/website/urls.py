from django.urls import path

from src.website.views import home
app_name = 'website'
urlpatterns = [
    path('', home,name="home")
]
