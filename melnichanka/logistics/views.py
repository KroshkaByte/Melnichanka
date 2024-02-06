from django.shortcuts import redirect, render

from .forms import (AutoAddForm, AutoDeleteForm, AutoEditForm, RwAddForm,
                    RwDeleteForm, RwEditPriceForm, RwEditRequisitesForm)
from .models import LogisticsAuto, LogisticsRailwayStations


def logistics_home_view(request):
    context = {
        "title": "Выбор вида доставки",
    }
    return render(request, "logistics/log_home.html", context)


def auto_home_view(request):
    data_auto = LogisticsAuto.objects.all()
    context = {
        "logistics_table": data_auto,
        "title": "Таблица рейсов",
    }
    return render(request, "logistics/auto_home.html", context)


def auto_add_view(request):
    if request.method == "POST":
        form = AutoAddForm(request.POST)
        if form.is_valid():
            dep_city = form.cleaned_data.get("departure_city").capitalize()
            dest_city = form.cleaned_data.get("destination_city").capitalize()
            price = form.cleaned_data.get("cost_per_tonn_auto")
            try:
                LogisticsAuto.objects.get(
                    departure_city=dep_city,
                    destination_city=dest_city,
                )
                return redirect("auto_edit")
            except LogisticsAuto.DoesNotExist:
                LogisticsAuto.objects.create(
                    departure_city=dep_city,
                    destination_city=dest_city,
                    cost_per_tonn_auto=price,
                )
                return redirect("auto_home")
            except LogisticsAuto.MultipleObjectsReturned:
                form.add_error(None, "Больше одного значения найдено")
    else:
        form = AutoAddForm()

    context = {
        "form": form,
        "title": "Добавление рейса",
    }
    return render(request, "logistics/auto_edit.html", context)


def auto_delete_view(request):
    if request.method == "POST":
        form = AutoDeleteForm(request.POST)
        if form.is_valid():
            try:
                del_trip = LogisticsAuto.objects.get(id=form.cleaned_data["trip"])
                del_trip.delete()
                return redirect("auto_home")
            except LogisticsAuto.DoesNotExist:
                form.add_error(None, "Ошибка изменения рейса (не найдено)")
            except LogisticsAuto.MultipleObjectsReturned:
                form.add_error(None, "Ошибка изменения рейса (найдено больше 1)")

    else:
        form = AutoDeleteForm()

    context = {
        "form": form,
        "title": "Удаление рейса",
    }
    return render(request, "logistics/auto_edit.html", context)


def auto_edit_view(request):
    if request.method == "POST":
        form = AutoEditForm(request.POST)
        if form.is_valid():
            dep_city = form.cleaned_data.get("departure_city").capitalize()
            dest_city = form.cleaned_data.get("destination_city").capitalize()
            price = form.cleaned_data.get("cost_per_tonn_auto")
            try:
                query_trip = LogisticsAuto.objects.get(
                    departure_city=dep_city, destination_city=dest_city
                )
                query_trip.cost_per_tonn_auto = price
                query_trip.save()
                return redirect("auto_home")
            except LogisticsAuto.DoesNotExist:
                form.add_error(None, "Ошибка изменения рейса (направление не найдено)")
            except LogisticsAuto.MultipleObjectsReturned:
                form.add_error(None, "Ошибка изменения рейса (найдено больше 1)")

    else:
        form = AutoEditForm()

    context = {
        "form": form,
        "title": "Изменение цены рейса",
    }
    return render(request, "logistics/auto_edit.html", context)


def rw_home_view(request):
    data_rw = LogisticsRailwayStations.objects.all()
    context = {
        "rw_table": data_rw,
        "title": "Таблица ж/д перевозок",
    }
    return render(request, "logistics/rw_home.html", context)


def rw_add_view(request):
    if request.method == "POST":
        form = RwAddForm(request.POST)
        if form.is_valid():
            dep_station_name = form.cleaned_data.get(
                "departure_station_name"
            ).capitalize()
            dep_station_id = form.cleaned_data.get("departure_station_id")
            dep_station_branch = form.cleaned_data.get(
                "departure_station_branch"
            ).upper()
            dest_station_name = form.cleaned_data.get(
                "destination_station_name"
            ).capitalize()
            dest_station_id = form.cleaned_data.get("destination_station_id")
            dest_station_branch = form.cleaned_data.get(
                "destination_station_branch"
            ).upper()
            cost_per_tonn_rw = form.cleaned_data.get("cost_per_tonn_rw")
            try:
                LogisticsRailwayStations.objects.get(
                    departure_station_name=dep_station_name,
                    destination_station_name=dest_station_name,
                )
                return redirect("rw_edit")
            except LogisticsRailwayStations.DoesNotExist:
                LogisticsRailwayStations.objects.create(
                    departure_station_name=dep_station_name,
                    departure_station_id=dep_station_id,
                    departure_station_branch=dep_station_branch,
                    destination_station_name=dest_station_name,
                    destination_station_id=dest_station_id,
                    destination_station_branch=dest_station_branch,
                    cost_per_tonn_rw=cost_per_tonn_rw,
                )
                return redirect("rw_home")
            except LogisticsRailwayStations.MultipleObjectsReturned:
                form.add_error(None, "Больше одного значения найдено")
    else:
        form = RwAddForm()

    context = {"form": form, "title": "Добавление ж/д перевозки"}
    return render(request, "logistics/rw_edit.html", context)


def rw_delete_view(request):
    if request.method == "POST":
        form = RwDeleteForm(request.POST)
        if form.is_valid():
            try:
                del_trip = LogisticsRailwayStations.objects.get(
                    id=form.cleaned_data["trip"]
                )
                del_trip.delete()
                return redirect("rw_home")
            except LogisticsRailwayStations.DoesNotExist:
                form.add_error(None, "Ошибка изменения рейса (не найдено)")
            except LogisticsRailwayStations.MultipleObjectsReturned:
                form.add_error(None, "Ошибка изменения рейса (найдено больше 1)")

    else:
        form = RwDeleteForm()

    context = {
        "form": form,
        "title": "Удаление ж/д перевозки",
    }
    return render(request, "logistics/rw_edit.html", context)


def rw_edit_price_view(request):
    if request.method == "POST":
        form = RwEditPriceForm(request.POST)
        if form.is_valid():
            dep_station = form.cleaned_data.get("departure_station_name").capitalize()
            dest_station = form.cleaned_data.get(
                "destination_station_name"
            ).capitalize()
            price = form.cleaned_data.get("cost_per_tonn_rw")
            try:
                query_trip = LogisticsRailwayStations.objects.get(
                    departure_station_name=dep_station,
                    destination_station_name=dest_station,
                )
                query_trip.cost_per_tonn_rw = price
                query_trip.save()
                return redirect("rw_home")
            except LogisticsRailwayStations.DoesNotExist:
                form.add_error(None, "Ошибка изменения рейса (направление не найдено)")
            except LogisticsRailwayStations.MultipleObjectsReturned:
                form.add_error(None, "Ошибка изменения рейса (найдено больше 1)")

    else:
        form = RwEditPriceForm()

    context = {
        "form": form,
        "title": "Изменение цены ж/д перевозки",
    }
    return render(request, "logistics/rw_edit.html", context)


def rw_edit_requisites_view(request):
    if request.method == "POST":
        form = RwEditRequisitesForm(request.POST)
        if form.is_valid():
            dep_station = form.cleaned_data.get("departure_station_name").capitalize()
            dep_station_id = form.cleaned_data.get("departure_station_id")
            dep_station_branch = form.cleaned_data.get(
                "departure_station_branch"
            ).upper()
            try:
                query_trip = LogisticsRailwayStations.objects.get(
                    departure_station_name=dep_station
                )
                query_trip.departure_station_id = dep_station_id
                query_trip.departure_station_branch = dep_station_branch
                query_trip.save()
                return redirect("rw_home")
            except LogisticsRailwayStations.DoesNotExist:
                form.add_error(None, "Ошибка изменения рейса (направление не найдено)")
            except LogisticsRailwayStations.MultipleObjectsReturned:
                form.add_error(None, "Ошибка изменения рейса (найдено больше 1)")

    else:
        form = RwEditRequisitesForm()

    context = {
        "form": form,
        "title": "Изменение реквизитов ж/д перевозки",
    }
    return render(request, "logistics/rw_edit.html", context)
