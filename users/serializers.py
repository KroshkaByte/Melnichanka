from django.contrib.auth.hashers import check_password
from rest_framework import serializers

from .models import CustomUser, Department, Position


class CustomUserSerializer(serializers.ModelSerializer[CustomUser]):
    """
    Serializer for creating a new user record.
    """

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
        """
        Validate password complexity and match between password and confirmation.
        """
        password = data.get("password")
        if len(password) < 8:
            raise serializers.ValidationError("Пароль должен содержать не менее 8 символов")
        if not any(char.isdigit() for char in password):
            raise serializers.ValidationError("Пароль должен содержать хотя бы одну цифру")
        if not any(char.isalpha() for char in password):
            raise serializers.ValidationError("Пароль должен содержать хотя бы одну букву")
        if data["password"] != data["password_confirm"]:
            raise serializers.ValidationError("Пароли не совпадают")
        return data

    def create(self, validated_data):
        """
        Create a new user instance after validating data.
        """
        validated_data.pop("password_confirm")
        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer[CustomUser]):
    """
    Serializer for updating existing user records.
    """

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
        ]


class UserUpdatePasswordSerializer(serializers.ModelSerializer[CustomUser]):
    """
    Serializer for updating user password.
    """

    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)
    new_password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = [
            "old_password",
            "new_password",
            "new_password_confirm",
        ]

    def validate(self, data):
        """
        Validate old password, new password complexity,
        and match between new password and confirmation.
        """
        # Проверяем, что старый пароль верный
        old_password = data.get("old_password")
        user = self.context["request"].user
        if not check_password(old_password, user.password):
            raise serializers.ValidationError("Старый пароль неверный")
        new_password = data.get("new_password")
        new_password_confirm = data.get("new_password_confirm")

        # Проверяем что новый пароль не такой как старый и подходит
        if new_password or new_password_confirm:
            if new_password == old_password:
                raise serializers.ValidationError("Новый пароль не должен совпадать со старым")
            if new_password != new_password_confirm:
                raise serializers.ValidationError("Новые пароли не совпадают")
            if len(new_password) < 8:
                raise serializers.ValidationError("Пароль должен содержать не менее 8 символов")
            if not any(char.isdigit() for char in new_password):
                raise serializers.ValidationError("Пароль должен содержать хотя бы одну цифру")
            if not any(char.isalpha() for char in new_password):
                raise serializers.ValidationError("Пароль должен содержать хотя бы одну букву")
        return super().validate(data)

    def update(self, instance, validated_data):
        """
        Update user instance with new password if provided.
        """
        # Если предоставлены новые пароли, устанавливаем новый пароль
        new_password = validated_data.pop("new_password", None)
        if new_password is not None:
            instance.set_password(new_password)
            instance.save()
        return super().update(instance, validated_data)


class LogoutSerializer(serializers.Serializer):  # type: ignore
    """
    Serializer for logging out a user.
    """

    refresh_token = serializers.CharField()


class DepartmentSerializer(serializers.ModelSerializer[Department]):
    """
    Serializer for Department model.
    """

    class Meta:
        model = Department
        fields = ["id", "department"]


class PositionSerializer(serializers.ModelSerializer[Position]):
    """
    Serializer for Position model.
    """

    class Meta:
        model = Position
        fields = ["id", "position"]
