from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email")
