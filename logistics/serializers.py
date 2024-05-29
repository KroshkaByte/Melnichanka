from rest_framework import serializers

from .models import City, RailwayStation, TripAuto, TripRailway


class CitySerializer(serializers.ModelSerializer[City]):
    class Meta:
        model = City
        fields = "__all__"


class TripAutoSerializer(serializers.ModelSerializer[TripAuto]):
    departure_city: serializers.CharField = serializers.CharField()
    destination_city: serializers.CharField = serializers.CharField()

    class Meta:
        model = TripAuto
        fields = "__all__"


class RailwayStationSerializer(serializers.ModelSerializer[RailwayStation]):
    class Meta:
        model = RailwayStation
        fields = "__all__"


class TripRailwaySerializer(serializers.ModelSerializer[TripRailway]):
    departure_station_name: serializers.CharField = serializers.CharField()
    destination_station_name: serializers.CharField = serializers.CharField()

    class Meta:
        model = TripRailway
        fields = "__all__"
