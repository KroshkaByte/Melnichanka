from logistics.models import RailwayStations


def get_rw_stations():
    stations = RailwayStations.objects.all()
    return [(station.id, station.station_name) for station in stations]
