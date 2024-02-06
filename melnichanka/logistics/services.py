from .models import LogisticsAuto, LogisticsRailwayStations


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
    a = LogisticsRailwayStations.objects.values(
        "departure_station_name", "destination_station_name"
    )
    set_choice = set()
    for x in a:
        set_choice.add(x.get("departure_station_name"))
        set_choice.add(x.get("destination_station_name"))
    return [(x, x) for x in set_choice]
