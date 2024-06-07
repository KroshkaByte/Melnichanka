from django.contrib import admin

from .models import City, RailwayStation, TripAuto, TripRailway, Factory


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["city", "region"]
    list_display_links = ["city", "region"]
    ordering = ["city"]
    list_per_page = 20
    search_fields = ["city", "region"]
    list_filter = ["city", "region"]


@admin.register(RailwayStation)
class RailwayStationAdmin(admin.ModelAdmin):
    list_display = ["station_name", "station_id", "station_branch"]
    list_display_links = ["station_name", "station_id", "station_branch"]
    ordering = ["station_name"]
    list_per_page = 20
    search_fields = ["station_name", "station_id", "station_branch"]
    list_filter = ["station_name", "station_id", "station_branch"]


@admin.register(TripAuto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ["departure_city", "destination_city", "cost_per_tonn_auto"]
    list_display_links = ["departure_city", "destination_city"]
    ordering = ["departure_city", "destination_city"]
    list_editable = ["cost_per_tonn_auto"]
    list_per_page = 20
    search_fields = ["departure_city", "destination_city"]
    list_filter = ["departure_city", "destination_city"]


@admin.register(TripRailway)
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


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = [
        "full_name",
        "full_address",
        "departure_city",
        "departure_station_branch",
        "departure_station_id",
        "departure_station_name",
    ]
    list_display_links = [
        "full_name",
        "full_address",
        "departure_city",
        "departure_station_branch",
        "departure_station_id",
        "departure_station_name",
    ]
    ordering = ["full_name"]
    list_per_page = 10
    search_fields = [
        "full_name",
        "full_address",
        "departure_city",
        "departure_station_branch",
        "departure_station_id",
        "departure_station_name",
    ]

    class Meta:
        verbose_name = "Предприятие"
        verbose_name_plural = "Предприятия"
        ordering = ["full_name"]
