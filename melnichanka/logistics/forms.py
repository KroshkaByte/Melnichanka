from django import forms

from .models import LogisticsCity

from .constants import BRANCHES, FED_DISCTRICT
from .services import get_auto_trips, get_cities, get_rw_stations, get_rw_trips


class AutoAddRequisitesForm(forms.ModelForm):
    class Meta:
        model = LogisticsCity
        fields = "__all__"



# Форма удаления населенного пункта
class AutoDeleteRequisitesForm(forms.Form):
    class Meta:
        model = LogisticsCity
        fields = ["city"]
        widgets = {
            "city": forms.Select(attrs={"class": "select_form"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = LogisticsCity.objects.all()

# Форма редактирования населенного пункта
class AutoEditRequisitesForm(forms.Form):
    city = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=get_cities,
        label="Населенный пункт",
    )
    region = forms.CharField(max_length=255, label="Субъект федерации")
    federal_district = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=FED_DISCTRICT,
        label="Федеральный округ",
    )


# Форма добавления перевозки (авто)
class AutoAddForm(forms.Form):
    cities = get_cities
    departure_city = forms.ChoiceField(
        label="Город отправления",
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=cities,
    )
    destination_city = forms.ChoiceField(
        label="Город назначения",
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=cities,
    )
    cost_per_tonn_auto = forms.IntegerField(
        label="Цена, руб./тн", step_size=100, min_value=0
    )


# Форма редактирования перевозки (авто)
class AutoEditForm(forms.Form):
    trip = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=get_auto_trips,
        label="Рейс",
    )
    cost_per_tonn_auto = forms.IntegerField(
        label="Цена, руб./тн", step_size=100, min_value=0
    )


# Форма удаления перевозки (авто)
class AutoDeleteForm(forms.Form):
    trip = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=get_auto_trips,
        label="Рейс",
    )


# Форма добавления ж/д станции
class RwAddRequisitesForm(forms.Form):
    station_name = forms.CharField(max_length=255, label="Станция")
    station_id = forms.IntegerField(
        label="Код ж/д станции",
        min_value=0,
    )
    station_branch = forms.ChoiceField(
        label="Ветка ж/д станции",
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=BRANCHES,
    )


# Форма удаления ж/д станции
class RwDeleteRequisitesForm(forms.Form):
    station = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=get_rw_stations,
        label="Ж/д станция",
    )


# Форма редактирования ж/д станции
class RwEditRequisitesForm(forms.Form):
    station_name = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=get_rw_stations,
        label="Ж/д станция",
    )
    station_id = forms.IntegerField(
        label="Код ж/д станции",
        min_value=0,
    )
    station_branch = forms.ChoiceField(
        label="Ветка ж/д станции",
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=BRANCHES,
    )


# Форма добавления ж/д перевозки
class RwAddForm(forms.Form):
    stations = get_rw_stations
    departure_station_name = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=stations,
        label="Станция отправления",
    )
    destination_station_name = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=stations,
        label="Станция назначения",
    )
    cost_per_tonn_rw = forms.IntegerField(
        label="Цена, руб./тн", step_size=100, min_value=0
    )


# Форма удаления ж/д перевозки
class RwDeleteForm(forms.Form):
    trip = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=get_rw_trips,
        label="Ж/д перевозка",
    )


# Форма редактирования ж/д перевозки
class RwEditForm(forms.Form):
    trip = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=get_rw_trips,
        label="Ж/д перевозка",
    )
    cost_per_tonn_rw = forms.IntegerField(
        label="Цена, руб./тн", step_size=100, min_value=0
    )
