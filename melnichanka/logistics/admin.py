from django.contrib import admin

from .models import TripsAuto, TripsRailway


@admin.register(TripsAuto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ["departure_city", "destination_city", "cost_per_tonn_auto"]
    list_display_links = ["destination_city"]
    ordering = ["departure_city", "destination_city"]
    list_editable = ["departure_city", "cost_per_tonn_auto"]
    list_per_page = 20
    search_fields = ["departure_city", "destination_city"]
    list_filter = ["departure_city", "destination_city"]


@admin.register(TripsRailway)
class RwAdmin(admin.ModelAdmin):
    list_display = [
        "departure_station_name",
        "destination_station_name",
        "cost_per_tonn_rw",
    ]
    list_display_links = ["destination_station_name"]
    ordering = ["departure_station_name", "destination_station_name"]
    list_editable = ["departure_station_name"]
    list_per_page = 20
    search_fields = ["departure_station_name", "destination_station_name"]
    list_filter = ["departure_station_name", "destination_station_name"]
