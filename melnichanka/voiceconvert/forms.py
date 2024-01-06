from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from phonenumber_field.formfields import PhoneNumberField

from .models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "patronymic",
            "position",
            "department",
            "phone_number_work",
            "phone_number_personal",
        )


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email")


class UserForm(forms.Form):
    phone = PhoneNumberField()
