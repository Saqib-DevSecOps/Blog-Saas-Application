from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class HomeTemplateView(TemplateView):
    def get_template_names(self):
        print(self.request.tenant.name)
        if self.request.tenant.name == "public":
            return 'website/home.html'
        return 'website/hom2.html'
