from django.contrib import admin, auth
from django_tenants.admin import TenantAdminMixin

from src.tenant.models import Client, Domain

# Register your models here.
@admin.register(Client)
class ClientAdmin(TenantAdminMixin,admin.ModelAdmin):
    list_display = ['schema_name']