from django.db import models


# Данные по логистике авто
class LogisticsAuto(models.Model):
    class FactoryFlour(models.TextChoices):
        KKHP = "Курск", "АО Курский Комбинат Хлебопродуктов"
        KHPS = "Оскол", "АО Комбинат Хлебопродуктов Старооскольский"
        GKHP = "Волгоград", "АО Городищенский Комбинат Хлебопродуктов"

    departure_city = models.CharField(
        max_length=9,
        choices=FactoryFlour.choices,
        blank=False,
        verbose_name="Комбинат грузоотправитель",
    )
    destination_city = models.CharField(
        max_length=50, blank=False, verbose_name="Город назначения"
    )
    cost_per_tonn_auto = models.PositiveIntegerField(
        verbose_name="Цена за рейс, руб./тн"
    )

    class Meta:
        verbose_name = "Логистика авто"
        verbose_name_plural = "Логистика авто"
        ordering = ["departure_city", "destination_city"]
        unique_together = ["departure_city", "destination_city"]

    def __str__(self):
        return f"Цена за рейс {self.departure_city} - {self.destination_city}: {self.cost_per_tonn_auto} руб./тн"


# Данные по логистике жд
class LogisticsRailwayStations(models.Model):
    departure_station_name = models.CharField(max_length=100)
    departure_station_id = models.PositiveIntegerField()
    departure_station_branch = models.CharField(max_length=100)
    destination_station_name = models.CharField(max_length=100)
    destination_station_id = models.PositiveIntegerField()
    destination_station_branch = models.CharField(max_length=100)
    cost_per_tonn_rw = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Логистика ж/д"
        verbose_name_plural = "Логистика ж/д"
        ordering = ["departure_station_name", "destination_station_name"]
        unique_together = ["departure_station_name", "destination_station_name"]

    def __str__(self):
        return f"Цена за жд перевозку {self.departure_station_name} - {self.destination_station_name}: {self.cost_per_tonn_rw} руб./тн"
