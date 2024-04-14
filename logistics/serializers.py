from rest_framework import serializers

from .models import City, RailwayStation, TripAuto, TripRailway


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class TripAutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripAuto
        fields = "__all__"


class RailwayStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RailwayStation
        fields = "__all__"


class TripRailwaySerializer(serializers.ModelSerializer):
    class Meta:
        model = TripRailway
        fields = "__all__"
