from django import forms
from django.forms import ModelForm

from .models import Clients


# Форма добавления клиента
class ClientsAddForm(ModelForm):
    contract_date = forms.DateField(
        label="Дата заключения договора", widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = Clients
        fields = "__all__"


# Форма редактирования записи клиента
class ClientsEditForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = "__all__"
