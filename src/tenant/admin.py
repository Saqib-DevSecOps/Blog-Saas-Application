from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from src.tenant.models import Client, Domain


class DomainInline(admin.TabularInline):
    model = Domain
    max_num = 1
@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'paid_until')

    inlines = [DomainInline]
