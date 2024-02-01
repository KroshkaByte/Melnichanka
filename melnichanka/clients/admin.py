from django.contrib import admin

from .models import Clients


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ["client_name", "contract_number"]
