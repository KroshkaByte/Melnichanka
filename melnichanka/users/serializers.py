from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "full_name",
            "position",
            "department",
            "phone_number_work",
            "phone_number_personal",
            "password",
            "password_confirm",
        ]

    def validate(self, data):
        password = data.get("password")
        if len(password) < 8:
            raise serializers.ValidationError(
                "Пароль должен содержать не менее 8 символов"
            )
        if not any(char.isdigit() for char in password):
            raise serializers.ValidationError(
                "Пароль должен содержать хотя бы одну цифру"
            )
        if not any(char.isalpha() for char in password):
            raise serializers.ValidationError(
                "Пароль должен содержать хотя бы одну букву"
            )
        if data["password"] != data["password_confirm"]:
            raise serializers.ValidationError("Пароли не совпадают")
        return data

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
