from django import forms

from .models import LogisticsAuto


class LogisticsAddForm(forms.Form):
    departure_city = forms.CharField(max_length=255, label="Город отправления")
    destination_city = forms.CharField(max_length=255, label="Город назначения")
    cost_per_tonn_auto = forms.IntegerField(
        label="Цена, руб./тн", step_size=100, min_value=0
    )


class LogisticsEditForm(forms.Form):
    DEP_CHOICES = (
        LogisticsAuto.objects.order_by()
        .values_list("departure_city", "departure_city")
        .distinct()
    )
    DEST_CHOICES = (
        LogisticsAuto.objects.order_by()
        .values_list("destination_city", "destination_city")
        .distinct()
    )

    departure_city = forms.CharField(
        widget=forms.Select(choices=DEP_CHOICES, attrs={"class": "select_form"}),
        label="Город отправления",
    )
    destination_city = forms.CharField(
        widget=forms.Select(choices=DEST_CHOICES, attrs={"class": "select_form"}),
        label="Город назначения",
    )
    cost_per_tonn_auto = forms.IntegerField(
        label="Цена, руб./тн", step_size=100, min_value=0
    )


class LogisticsDeleteForm(forms.Form):
    TRIP_CHOICES = LogisticsAuto.objects.order_by()

    trip = forms.CharField(
        widget=forms.Select(choices=TRIP_CHOICES, attrs={"class": "select_form"}),
        label="Рейс",
    )
