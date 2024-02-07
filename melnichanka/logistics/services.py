from .models import LogisticsAuto, LogisticsRailwayStations, RailwayStations


def get_auto_dep_choices():
    return (
        LogisticsAuto.objects.order_by()
        .values_list("departure_city", "departure_city")
        .distinct()
    )


def get_dest_choices():
    return (
        LogisticsAuto.objects.order_by()
        .values_list("destination_city", "destination_city")
        .distinct()
    )


def get_all_auto_choices():
    return [(trip.id, trip) for trip in LogisticsAuto.objects.all()]


def get_all_rw_choices():
    return [(trip.id, trip) for trip in LogisticsRailwayStations.objects.all()]


def get_rw_dep_choices():
    return (
        LogisticsRailwayStations.objects.order_by()
        .values_list("departure_station_name", "departure_station_name")
        .distinct()
    )


def get_rw_dest_choices():
    return (
        LogisticsRailwayStations.objects.order_by()
        .values_list("destination_station_name", "destination_station_name")
        .distinct()
    )


def get_all_rw_stations():
    stations = RailwayStations.objects.all()
    return [(x.id, x.station_name) for x in stations]
