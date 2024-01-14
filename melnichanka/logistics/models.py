from django.db import models


# Данные по логистике авто
class LogisticsAuto(models.Model):
    departure_city = models.CharField(max_length=50)
    destination_city = models.CharField(max_length=50)
    cost_per_tonn_auto = models.PositiveIntegerField()

    class Meta:
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
        ordering = ["departure_station_name", "destination_station_name"]
        unique_together = ["departure_station_name", "destination_station_name"]

    def __str__(self):
        return f"Цена за жд перевозку {self.departure_station_name} - {self.destination_station_name}: {self.cost_per_tonn_rw} руб./тн"
