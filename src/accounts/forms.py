from django.forms import ModelForm

from src.tenant.models import Client


class ClientModelForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


