from rest_framework import serializers
from .models import Clients
from logistics.models import RailwayStations


class ClientSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField()
    contract_number = serializers.CharField()
    contract_date = serializers.DateField()
    director_position = serializers.CharField()
    director_name = serializers.CharField()
    # ЖД реквизиты
    # Обратите внимание, что если не существует экземпляра RailwayStations с указанным идентификатором,
    # Django REST framework вернет ошибку 400 Bad Request
    # ПОКА ОСТАВЛЯЕМ ТАК, ПОКА ЖД НЕТ СЕРИАЛИЗАЦИИ
    destination_city = serializers.SlugRelatedField(
        slug_field="id", queryset=RailwayStations.objects.all()
    )
    # Остальные данные
    receiver_name = serializers.CharField()
    receiver_id = serializers.IntegerField(min_value=0)
    receiver_okpo = serializers.IntegerField(min_value=0)
    receiver_adress = serializers.CharField()
    special_marks = serializers.CharField()
    # Номер приложения
    last_application_number = serializers.CharField()

    def create(self, validated_data):
        return Clients.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.client_name = validated_data.get("client_name", instance.client_name)
        instance.contract_number = validated_data.get(
            "contract_number", instance.contract_number
        )
        instance.contract_date = validated_data.get(
            "contract_date", instance.contract_date
        )
        instance.director_position = validated_data.get(
            "director_position", instance.director_position
        )
        instance.director_name = validated_data.get(
            "director_name", instance.director_name
        )
        instance.destination_city = validated_data.get(
            "destination_city", instance.destination_city
        )
        instance.receiver_name = validated_data.get(
            "receiver_name", instance.receiver_name
        )
        instance.receiver_id = validated_data.get("receiver_id", instance.receiver_id)
        instance.receiver_okpo = validated_data.get(
            "receiver_okpo", instance.receiver_okpo
        )
        instance.receiver_adress = validated_data.get(
            "receiver_adress", instance.receiver_adress
        )
        instance.special_marks = validated_data.get(
            "special_marks", instance.special_marks
        )
        instance.last_application_number = validated_data.get(
            "last_application_number", instance.last_application_number
        )
        instance.save()
        return instance

    class Meta:
        model = Clients
        fields = "__all__"
