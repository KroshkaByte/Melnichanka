from rest_framework import serializers

from .models import City, RailwayStations, TripsAuto, TripsRailway


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class TripsAutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripsAuto
        fields = "__all__"


class RailwayStationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RailwayStations
        fields = "__all__"


class TripsRailwaySerializer(serializers.ModelSerializer):
    class Meta:
        model = TripsRailway
        fields = "__all__"
