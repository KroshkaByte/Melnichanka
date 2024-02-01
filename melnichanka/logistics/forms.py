from django import forms

from .services import get_all_choices, get_dep_choices, get_dest_choices


class LogisticsAddForm(forms.Form):
    departure_city = forms.CharField(max_length=255, label="Город отправления")
    destination_city = forms.CharField(max_length=255, label="Город назначения")
    cost_per_tonn_auto = forms.IntegerField(
        label="Цена, руб./тн", step_size=100, min_value=0
    )


class LogisticsEditForm(forms.Form):
    departure_city = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=get_dep_choices,
        label="Город отправления",
    )
    destination_city = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=get_dest_choices,
        label="Город назначения",
    )
    cost_per_tonn_auto = forms.IntegerField(
        label="Цена, руб./тн", step_size=100, min_value=0
    )


class LogisticsDeleteForm(forms.Form):
    trip = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "select_form"}),
        choices=get_all_choices,
        label="Рейс",
    )
