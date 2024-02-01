from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [
        "first_name",
        "last_name",
        "email",
        "username",
        "position",
        "department",
        "is_staff",
        "phone_number_personal",
        "phone_number_work",
    ]
    list_display_links = [
        "first_name",
        "last_name",
        "username",
    ]
    list_editable = ["is_staff"]
