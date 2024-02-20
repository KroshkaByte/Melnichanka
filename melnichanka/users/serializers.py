from rest_framework import serializers
from .models import User
from phonenumber_field.serializerfields import PhoneNumberField


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "patronymic",
            "position",
            "department",
            "email",
            "password",
            "phone_number_work",
            "phone_number_personal",
        )
