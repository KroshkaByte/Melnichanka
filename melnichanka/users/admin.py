from django.contrib import admin

from .models import CustomUser, Department, Position


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["is_active", "email", "full_name"]
    exclude = [
        "password",
    ]
    list_per_page = 10
    search_fields = ["email", "full_name"]
    ordering = ["email", "full_name"]


admin.site.register(Department)
admin.site.register(Position)
