from rest_framework import serializers

from .models import City, RailwayStation, TripAuto, TripRailway, Factory


class CitySerializer(serializers.ModelSerializer[City]):
    """
    Serializer for City model.

    Serializes all fields of the City model.
    """

    class Meta:
        model = City
        fields = "__all__"


class TripAutoSerializer(serializers.ModelSerializer[TripAuto]):
    """
    Serializer for TripAuto model.

    Serializes all fields of the TripAuto model, and includes
    additional fields for departure_city and destination_city.
    """

    departure_city: serializers.CharField = serializers.CharField()
    destination_city: serializers.CharField = serializers.CharField()

    class Meta:
        model = TripAuto
        fields = "__all__"


class RailwayStationSerializer(serializers.ModelSerializer[RailwayStation]):
    """
    Serializer for RailwayStation model.
    """

    class Meta:
        model = RailwayStation
        fields = "__all__"


class TripRailwaySerializer(serializers.ModelSerializer[TripRailway]):
    """
    Serializer for TripRailway model.
    """

    departure_station_name: serializers.CharField = serializers.CharField()
    destination_station_name: serializers.CharField = serializers.CharField()

    class Meta:
        model = TripRailway
        fields = "__all__"


class FactorySerializer(serializers.ModelSerializer[Factory]):
    """
    Serializer for Factory model.
    """

    class Meta:
        model = Factory
        fields = "__all__"
