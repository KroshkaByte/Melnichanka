from django.contrib import admin

from .models import CustomUser, Department, Position


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        "full_name",
        "is_active",
        "email",
        "phone_number_work",
        "position",
        "department",
    ]
    list_per_page = 10
    search_fields = ["email", "full_name"]
    ordering = ["email", "full_name"]


admin.site.register(Department)
admin.site.register(Position)
