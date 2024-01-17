from django.contrib import admin

from .models import LogisticsAuto


@admin.register(LogisticsAuto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ["departure_city", "destination_city", "cost_per_tonn_auto"]
    list_display_links = ["destination_city"]
    ordering = ["departure_city", "destination_city"]
    list_editable = ["departure_city", "cost_per_tonn_auto"]
    list_per_page = 20
    search_fields = ["departure_city", "destination_city"]
    list_filter = ["departure_city", "destination_city"]
