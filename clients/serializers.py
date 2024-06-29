from rest_framework import serializers

from .models import Client, DirectorPosition


class DirectorPositionSerializer(serializers.ModelSerializer[DirectorPosition]):
    """
    Serializer for the DirectorPosition model.

    Serializes the 'id' and 'director_position' fields of DirectorPosition.
    """

    class Meta:
        model = DirectorPosition
        fields = ["id", "director_position"]


class ClientSerializer(serializers.ModelSerializer[Client]):
    """
    Serializer for the Client model.

    Serializes all fields of the Client model including nested serialization of 'director_position'.
    Adds 'destination_city' and 'railway_station' as CharField serializers.
    Sets the current authenticated user as the value for the 'user' field using HiddenField.

    Fields:
    - id: IntegerField
    - director_position: Nested serialization using DirectorPositionSerializer
    - destination_city: CharField for destination city name
    - railway_station: CharField for railway station name
    - user: HiddenField that defaults to the current authenticated user

    Note: 'user' field is automatically populated with the current user making the request.
    """
    director_position = DirectorPositionSerializer()
    destination_city: serializers.CharField = serializers.CharField()
    railway_station: serializers.CharField = serializers.CharField()

    # Устанавливает текущего авторизованого пользователя в поле user
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Client
        fields = "__all__"
