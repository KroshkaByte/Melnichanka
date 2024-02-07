from django import forms

from .constants import BRANCHES
from .services import (get_all_auto_choices, get_all_rw_choices,
                       get_all_rw_stations, get_auto_dep_choices,
                       get_dest_choices, get_rw_dep_choices,
                       get_rw_dest_choices)


class AutoAddForm(forms.Form):
    departure_city = forms.CharField(max_length=255, label="Город отправления")
    destination_city = forms.CharField(max_length=255, label="Город назначения")
    cost_per_tonn_auto = forms.IntegerField(
        label="Цена, руб./тн", step_size=100, min_value=0
    )


class AutoEditForm(forms.Form):
    departure_city = forms.ChoiceField(
        label="Город отправления",
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=get_auto_dep_choices,
    )
    destination_city = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=get_dest_choices,
        label="Город назначения",
    )
    cost_per_tonn_auto = forms.IntegerField(
        label="Цена, руб./тн", step_size=100, min_value=0
    )


class AutoDeleteForm(forms.Form):
    trip = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=get_all_auto_choices,
        label="Рейс",
    )


class RwAddForm(forms.Form):
    departure_station_name = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=get_all_rw_stations,
        label="Станция отправления",
    )
    destination_station_name = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=get_all_rw_stations,
        label="Станция назначения",
    )
    cost_per_tonn_rw = forms.IntegerField(
        label="Цена, руб./тн", step_size=100, min_value=0
    )


class RwDeleteForm(forms.Form):
    trip = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=get_all_rw_choices,
        label="Ж/д перевозка",
    )


class RwEditForm(forms.Form):
    departure_station_name = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=get_rw_dep_choices,
        label="Станция отправления",
    )
    destination_station_name = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=get_rw_dest_choices,
        label="Станция назначения",
    )
    cost_per_tonn_rw = forms.IntegerField(
        label="Цена, руб./тн", step_size=100, min_value=0
    )


class RwAddRequisitesForm(forms.Form):
    station_name = forms.CharField(
        max_length=255, label="Станция"
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


class RwDeleteRequisitesForm(forms.Form):
    station = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=get_all_rw_stations,
        label="Ж/д станция",
    )


class RwEditRequisitesForm(forms.Form):
    station_name = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=get_all_rw_stations,
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
