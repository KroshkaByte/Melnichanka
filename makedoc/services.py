from clients.models import Clients
from logistics.models import RailwayStations
from users.models import CustomUser


def get_rw(request):
    rw = RailwayStations.objects.get(id=1)
    return rw


def get_client(request):
    client = Clients.objects.all().first()
    return client


def get_client_rw(request):
    client = Clients.objects.get(id=5)
    return client


def get_user(request):
    user = CustomUser.objects.get(id=1)
    return user
