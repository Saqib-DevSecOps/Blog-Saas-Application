"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, URLResolver, URLPattern


class RequestURLResolver(URLResolver):
    def __init__(self, urlconf_name, default_kwargs, request):
        self.request = request
        super(RequestURLResolver, self).__init__(None, urlconf_name, default_kwargs)


def select_url(request):
    tenant_name = request.tenant.name
    if tenant_name == "public":
        return [URLPattern('', include('src.website.urls'))]


def get_tenant_url(request):
    return RequestURLResolver(select_url(request), {}, request)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include([get_tenant_url])),
]
