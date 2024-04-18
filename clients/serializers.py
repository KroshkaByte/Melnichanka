from rest_framework import serializers

from .models import Client, DirectorPosition


class DirectorPositionSerializer(serializers.ModelSerializer[DirectorPosition]):
    class Meta:
        model = DirectorPosition
        fields = ["id", "director_position"]


class ClientSerializer(serializers.ModelSerializer[Client]):
    # Устанавливает текущего авторизованого пользователя в поле user
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Client
        fields = "__all__"
