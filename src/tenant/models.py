from django_tenants.models import TenantMixin, DomainMixin
from django.db import models


class Client(TenantMixin):
    schema_name = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    auto_create_schema = True

    def __str__(self):
        return self.schema_name


class Domain(DomainMixin):
    pass
