from rest_framework import serializers

from .models import Clients


class ClientSerializer(serializers.ModelSerializer):
    # Устанавливает текущего авторизованого пользователя в поле user
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Clients
        fields = "__all__"
