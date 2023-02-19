from django.contrib import admin

from src.website.models import Blog,BlogCategory

# Register your models here.

admin.site.register(Blog)
admin.site.register(BlogCategory)