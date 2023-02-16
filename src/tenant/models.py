from django_tenants.models import TenantMixin, DomainMixin
from django.db import models


class Client(TenantMixin):
    auto_create_schema = True


class Domain(DomainMixin):
    pass
