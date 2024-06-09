from django.db import models

from .constants import BRANCHES


class City(models.Model):
    city = models.CharField(
        max_length=100,
        blank=False,
        verbose_name="Населенный пункт",
    )
    region = models.CharField(
        max_length=100,
        blank=False,
        verbose_name="Регион",
    )

    class Meta:
        verbose_name = "Населенный пункт"
        verbose_name_plural = "Населенные пункты"
        ordering = ["city"]
        unique_together = ["city", "region"]

    def __str__(self) -> str:
        return f"{self.city}, {self.region}"


# Данные по логистике авто
class TripAuto(models.Model):
    departure_city = models.ForeignKey(
        "City",
        db_column="departure_city",
        on_delete=models.PROTECT,
        related_name="departure_city",
    )
    destination_city = models.ForeignKey(
        "City",
        db_column="destination_city",
        on_delete=models.PROTECT,
        related_name="destination_city",
    )
    cost_per_tonn_auto = models.PositiveIntegerField(verbose_name="Цена за рейс, руб./тн")

    class Meta:
        verbose_name = "Перевозки авто"
        verbose_name_plural = "Перевозки авто"
        ordering = ["departure_city", "destination_city"]
        unique_together = ["departure_city", "destination_city"]

    def __str__(self) -> str:
        return (
            f"{self.departure_city} - {self.destination_city}: {self.cost_per_tonn_auto} руб./тн"
        )


# Таблица ж/д станций
class RailwayStation(models.Model):
    station_name = models.CharField(
        max_length=100,
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

    def __str__(self) -> str:
        return f"{self.station_name}, {self.station_branch}, {self.station_id}"


# Данные по логистике жд
class TripRailway(models.Model):
    departure_station_name = models.ForeignKey(
        "RailwayStation",
        db_column="departure_station_name",
        on_delete=models.PROTECT,
        related_name="departure_station_name",
    )

    destination_station_name = models.ForeignKey(
        "RailwayStation",
        db_column="destination_station_name",
        on_delete=models.PROTECT,
        related_name="destination_station_name",
    )
    cost_per_tonn_rw = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Перевозки ж/д"
        verbose_name_plural = "Перевозки ж/д"
        ordering = ["departure_station_name", "destination_station_name"]
        unique_together = ["departure_station_name", "destination_station_name"]

    def __str__(self) -> str:
        return f"{self.departure_station_name} - {self.destination_station_name}: {self.cost_per_tonn_rw} руб./тн"  # noqa 501


class Factory(models.Model):
    full_name = models.CharField(
        max_length=100, blank=False, verbose_name="Полное название предприятия"
    )
    short_name = models.CharField(
        max_length=100, blank=False, verbose_name="Краткое название предприятия"
    )
    full_address = models.CharField(max_length=100, blank=False, verbose_name="Адрес предприятия")
    departure_city = models.CharField(
        max_length=100,
        blank=False,
        verbose_name="Город отправления",
    )
    departure_station_branch = models.CharField(
        max_length=100, blank=False, verbose_name="Ветка ж/д стации", choices=BRANCHES
    )
    departure_station_id = models.PositiveIntegerField(verbose_name="Код ж/д стации")
    departure_station_name = models.CharField(
        max_length=100, blank=False, verbose_name="Ж/Д станция"
    )

    class Meta:
        verbose_name = "Предприятие"
        verbose_name_plural = "Предприятия"
        ordering = ["-full_name"]
        unique_together = [
            (
                "full_name",
                "short_name",
                "full_address",
            )
        ]

    def __str__(self) -> str:
        return self.full_name
