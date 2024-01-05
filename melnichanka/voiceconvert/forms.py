from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from phonenumber_field.formfields import PhoneNumberField

from .models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email")


class UserForm(forms.Form):
    phone = PhoneNumberField()
