from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from phonenumber_field.formfields import PhoneNumberField

from .models import User
from .constants import DEPARTMENT, POSITION


# Форма регистрации пользователя
class CustomUserCreationForm(UserCreationForm):
    position = forms.ChoiceField(widget=forms.Select(), choices=POSITION)
    department = forms.ChoiceField(widget=forms.Select(), choices=DEPARTMENT)

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


# Форма изменения данных пользователя
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email")


class UserForm(forms.Form):
    phone = PhoneNumberField()
