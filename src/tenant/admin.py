from django.contrib import admin, auth
from django_tenants.admin import TenantAdminMixin

from src.tenant.models import Client, Domain

class  DomainInline(admin.TabularInline):
    model = Domain
    max_num = 1
# Register your models here.
@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['schema_name']
    inlines = [DomainInline]
