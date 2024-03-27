from django.contrib import admin

from .models import Clients, Director_position


admin.site.register(Director_position)


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = [
        "client_name",
        "contract_number",
        "director_name",
        "destination_city",
    ]
    list_per_page = 10
    search_fields = ["client_name", "director_name", "destination_city"]
    ordering = ["client_name", "destination_city"]
