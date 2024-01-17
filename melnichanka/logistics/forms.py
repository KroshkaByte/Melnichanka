from django.forms import ModelForm

from .models import LogisticsAuto


class LogisticsAddForm(ModelForm):
    class Meta:
        model = LogisticsAuto
        fields = (
            "departure_city",
            "destination_city",
            "cost_per_tonn_auto",
        )
        labels = {
            "departure_city": "Город отправления",
            "destination_city": "Город назначения",
            "cost_per_tonn_auto": "Цена, руб./тн",
        }
