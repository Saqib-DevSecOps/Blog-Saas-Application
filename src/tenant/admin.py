from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from src.tenant.models import Client


@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'paid_until')

