from rest_framework import serializers

from .models import LogisticsAuto


class LogisticsAutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogisticsAuto
        fields = "__all__"


class LogisticsModel:
    def __init__(self, city, region, federal_district):
        self.city = city
        self.region = region
        self.federal_district = federal_district


class LogisticsSerializer(serializers.Serializer):
    class Meta:
        model = LogisticsAuto
        fields = ("city", "region", "federal_disctrict")
