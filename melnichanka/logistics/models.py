from django.db import models

from .constants import BRANCHES, FACTORY_STATION, FED_DISCTRICT


class LogisticsCity(models.Model):
    city = models.CharField(
        max_length=100,
        blank=False,
        verbose_name="Населенный пункт",
    )
    region = models.CharField(
        max_length=100,
        blank=False,
        verbose_name="Субъект федерации",
    )
    federal_district = models.CharField(
        max_length=100,
        blank=False,
        verbose_name="Федеральный округ",
        choices=FED_DISCTRICT,
    )

    class Meta:
        verbose_name = "Населенный пункт"
        verbose_name_plural = "Населенные пункты"
        ordering = ["city"]
        unique_together = ["city", "region", "federal_district"]

    def __str__(self):
        return f"{self.city}, {self.region}"


# Данные по логистике авто
class LogisticsAuto(models.Model):
    departure_city = models.ForeignKey(
        "LogisticsCity",
        db_column="departure_city",
        on_delete=models.PROTECT,
        related_name="departure_city",
    )
    destination_city = models.ForeignKey(
        "LogisticsCity",
        db_column="destination_city",
        on_delete=models.PROTECT,
        related_name="destination_city",
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
        return f"{self.departure_city} - {self.destination_city}: {self.cost_per_tonn_auto} руб./тн"


# Таблица ж/д станций
class RailwayStations(models.Model):
    station_name = models.CharField(
        max_length=100,
        choices=FACTORY_STATION,
        blank=False,
        verbose_name="Станция",
    )

    station_id = models.PositiveIntegerField()
    station_branch = models.CharField(
        max_length=255,
        choices=BRANCHES,
    )

    class Meta:
        verbose_name = "Ж/д станция"
        verbose_name_plural = "Ж/д станции"
        ordering = ["station_name"]
        unique_together = ["station_name", "station_id"]

    def __str__(self):
        return self.station_name


# Данные по логистике жд
class LogisticsRailwayStations(models.Model):
    departure_station_name = models.ForeignKey(
        "RailwayStations",
        db_column="departure_station_name",
        on_delete=models.PROTECT,
        related_name="departure_station_name",
    )

    destination_station_name = models.ForeignKey(
        "RailwayStations",
        db_column="destination_station_name",
        on_delete=models.PROTECT,
        related_name="destination_station_name",
    )

    destination_station_name = models.ForeignKey(
        "RailwayStations",
        db_column="destination_station_name",
        on_delete=models.PROTECT,
        related_name="destination_station_name",
    )
    cost_per_tonn_rw = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Логистика ж/д"
        verbose_name_plural = "Логистика ж/д"
        ordering = ["departure_station_name", "destination_station_name"]
        unique_together = ["departure_station_name", "destination_station_name"]

    def __str__(self):
        return f"{self.departure_station_name} - {self.destination_station_name}: {self.cost_per_tonn_rw} руб./тн"
