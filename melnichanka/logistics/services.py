from .models import (
    LogisticsAuto,
    LogisticsCity,
    LogisticsRailwayStations,
    RailwayStations,
)


def get_auto_trips():
    return [(trip.id, trip) for trip in LogisticsAuto.objects.all()]


def get_rw_trips():
    return [(trip.id, trip) for trip in LogisticsRailwayStations.objects.all()]


def get_rw_stations():
    stations = RailwayStations.objects.all()
    return [(station.id, station) for station in stations]


def get_cities():
    cities = LogisticsCity.objects.all()
    return [(city.id, city) for city in cities]
