from django import forms
from .models import Clients


class ClientsAddForm(forms.Form):
    # Основная информация
    client_name = forms.CharField(max_length=100, label="Наименование организации")
    contract_number = forms.CharField(max_length=50, label="Номер договора")
    contract_date = forms.DateField(
        label="Дата заключения договора",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    director_position = forms.CharField(max_length=100, label="Должность директора")
    director_name = forms.CharField(max_length=100, label="ФИО директора")

    # ЖД реквизиты
    destination_station_name = forms.CharField(
        max_length=100, label="Наименование ЖД станции"
    )
    destination_station_id = forms.IntegerField(label="Номер ЖД станции")
    receiver_name = forms.CharField(max_length=100, label="Имя получателя")
    receiver_id = forms.IntegerField(label="Номер получателя")
    receiver_okpo = forms.IntegerField(label="ОКПО")
    receiver_adress = forms.CharField(max_length=200, label="Адрес получателя")
    special_marks = forms.CharField(max_length=200, label="Особые отметки")

    # Номер приложения
    last_application_number = forms.CharField(max_length=50, label="Номер приложения")


class ClientsEditForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ["client_name", "contract_number", "contract_date"]
