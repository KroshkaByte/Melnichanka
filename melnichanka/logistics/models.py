from django.db import models

from .constants import (BRANCHES, FACTORY_ADRESS, FACTORY_BRANCH,
                        FACTORY_BRANCH_ID, FACTORY_CITY, FACTORY_NAME_FULL,
                        FACTORY_NAME_SHORT, FACTORY_STATION)


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


# Данные по логистике жд
class LogisticsRailwayStations(models.Model):
    departure_station_name = models.CharField(
        max_length=255,
        choices=FACTORY_STATION,
        blank=False,
        verbose_name="Комбинат грузоотправитель",
    )

    departure_station_id = models.PositiveIntegerField()
    departure_station_branch = models.CharField(
        max_length=255,
        choices=BRANCHES,
    )
    destination_station_name = models.CharField(max_length=100)
    destination_station_id = models.PositiveIntegerField()
    destination_station_branch = models.CharField(
        max_length=255,
        choices=BRANCHES,
    )
    cost_per_tonn_rw = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Логистика ж/д"
        verbose_name_plural = "Логистика ж/д"
        ordering = ["departure_station_name", "destination_station_name"]
        unique_together = ["departure_station_name", "destination_station_name"]

    def __str__(self):
        return f"{self.departure_station_name} - {self.destination_station_name}: {self.cost_per_tonn_rw} руб./тн"
