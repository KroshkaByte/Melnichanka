from django import forms
from django.forms import ModelForm


from .models import Clients


class ClientsAddForm(forms.Form):
    # Основная информация
    client_name = forms.CharField(max_length=100, label="Название предприятия")
    contract_number = forms.CharField(max_length=50, label="Номер договора")
    contract_date = forms.DateField(
        required=False,
        label="Дата заключения договора",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    director_position = forms.CharField(max_length=100, label="Должность директора")
    director_name = forms.CharField(max_length=100, label="Имя директора")
    special_marks = forms.CharField(max_length=200, label="Специальнные отметки")

    # ЖД реквизиты
    destination_station_name = forms.CharField(max_length=100, label="Имя ЖД станции")
    destination_station_id = forms.IntegerField(label="Номер ЖД станции")
    receiver_name = forms.CharField(max_length=100, label="Имя получателя")
    receiver_id = forms.IntegerField(label="Номер получателя")
    receiver_okpo = forms.IntegerField(label="ОКПО")
    receiver_adress = forms.CharField(max_length=200, label="Адрес получателя")

    # Номер приложения
    last_application_number = forms.CharField(max_length=50, label="Номер приложения")
