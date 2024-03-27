from rest_framework import serializers

from .models import Clients, Director_position


class DirectorpositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director_position
        fields = ["id", "director_position"]


class ClientSerializer(serializers.ModelSerializer):
    # Устанавливает текущего авторизованого пользователя в поле user
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Clients
        fields = "__all__"
