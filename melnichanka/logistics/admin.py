from django.contrib import admin

from .models import City, RailwayStations, TripsAuto, TripsRailway


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["city", "region", "federal_district"]
    list_display_links = ["city", "region", "federal_district"]
    ordering = ["city"]
    list_per_page = 20
    search_fields = ["city", "region", "federal_district"]
    list_filter = ["city", "region", "federal_district"]


@admin.register(RailwayStations)
class RailwayStationsAdmin(admin.ModelAdmin):
    list_display = ["station_name", "station_id", "station_branch"]
    list_display_links = ["station_name", "station_id", "station_branch"]
    ordering = ["station_name"]
    list_per_page = 20
    search_fields = ["station_name", "station_id", "station_branch"]
    list_filter = ["station_name", "station_id", "station_branch"]


@admin.register(TripsAuto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ["departure_city", "destination_city", "cost_per_tonn_auto"]
    list_display_links = ["departure_city", "destination_city"]
    ordering = ["departure_city", "destination_city"]
    list_editable = ["cost_per_tonn_auto"]
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
