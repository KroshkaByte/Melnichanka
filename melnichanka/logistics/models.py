from django.db import models

from .constants import (BRANCHES, FACTORY_ADRESS, FACTORY_BRANCH,
                        FACTORY_BRANCH_ID, FACTORY_CITY, FACTORY_NAME_FULL,
                        FACTORY_NAME_SHORT, FACTORY_STATION)


# Данные по заводам
class Factory(models.Model):
    full_name = models.CharField(
        max_length=100,
        blank=False,
        choices=FACTORY_NAME_FULL,
    )
    short_name = models.CharField(
        max_length=50, blank=False, choices=FACTORY_NAME_SHORT
    )
    full_address = models.CharField(max_length=255, blank=False, choices=FACTORY_ADRESS)
    departure_city = models.CharField(max_length=50, blank=False, choices=FACTORY_CITY)
    departure_station_branch = models.CharField(
        max_length=9, blank=False, choices=FACTORY_BRANCH
    )
    departure_station_id = models.CharField(
        max_length=9, blank=False, choices=FACTORY_BRANCH_ID
    )

    class Meta:
        verbose_name = "Комбинат"
        verbose_name_plural = "Комбинаты"
        ordering = ["full_name"]


# Данные по логистике авто
class LogisticsAuto(models.Model):
    departure_city = models.CharField(
        max_length=100, blank=False, verbose_name="Комбинат грузоотправитель"
    )
    destination_city = models.CharField(
        max_length=100, blank=False, verbose_name="Город назначения"
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
        max_length=255,
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

    def __str__(self):
        return f"{self.station_name}, {self.station_id}, {self.station_branch}"


# Данные по логистике жд
class LogisticsRailwayStations(models.Model):
    departure_station_name = models.ForeignKey(
        "RailwayStations",
        db_column="departure_station_name",
        on_delete=models.DO_NOTHING,
        related_name="departure_station_name",
    )

    destination_station_name = models.ForeignKey(
        "RailwayStations",
        db_column="destination_station_name",
        on_delete=models.DO_NOTHING,
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
