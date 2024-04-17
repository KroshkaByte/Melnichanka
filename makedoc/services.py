import datetime
import openpyxl

from django.http import HttpResponse
from dateutil.relativedelta import relativedelta
from clients.models import Clients, Director_position
from logistics.models import City, RailwayStations, TripsAuto, TripsRailway
from users.models import CustomUser
from .constants import MONTHS_AGREEMENT, MONTHS_SHIPMENT


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
