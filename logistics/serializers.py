from rest_framework import serializers

from .models import City, RailwayStation, TripAuto, TripRailway


class CitySerializer(serializers.ModelSerializer[City]):
    class Meta:
        model = City
        fields = "__all__"


class TripAutoSerializer(serializers.ModelSerializer[TripAuto]):
    class Meta:
        model = TripAuto
        fields = "__all__"


class RailwayStationSerializer(serializers.ModelSerializer[RailwayStation]):
    class Meta:
        model = RailwayStation
        fields = "__all__"


class TripRailwaySerializer(serializers.ModelSerializer[TripRailway]):
    class Meta:
        model = TripRailway
        fields = "__all__"
