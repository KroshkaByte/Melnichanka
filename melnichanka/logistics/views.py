from django.shortcuts import redirect, render

from .forms import (AutoAddForm, AutoAddRequisitesForm, AutoDeleteForm,
                    AutoDeleteRequisitesForm, AutoEditForm,
                    AutoEditRequisitesForm, RwAddForm, RwAddRequisitesForm,
                    RwDeleteForm, RwDeleteRequisitesForm, RwEditForm,
                    RwEditRequisitesForm)
from .models import (LogisticsAuto, LogisticsCity, LogisticsRailwayStations,
                     RailwayStations)


# Выбор вида доставки (авто/жд)
def logistics_home_view(request):
    context = {
        "title": "Выбор вида доставки",
        "title": "Выбор вида доставки",
    }
    return render(request, "logistics/log_home.html", context)


# Таблица всех авто рейсов
def auto_home_view(request):
    data_auto = LogisticsAuto.objects.all()
    context = {
        "logistics_table": data_auto,
        "title": "Таблица рейсов",
    }
    return render(request, "logistics/auto_home.html", context)


# Добавление рейса авто
def auto_add_view(request):
    if request.method == "POST":
        form = AutoAddForm(request.POST)
        form = AutoAddForm(request.POST)
        if form.is_valid():
            form_dep_city = form.cleaned_data["departure_city"]
            form_dest_city = form.cleaned_data["destination_city"]
            dep_city = LogisticsAuto.objects.get(pk=form_dep_city)
            dest_city = LogisticsAuto.objects.get(pk=form_dest_city)
            price = form.cleaned_data["cost_per_tonn_auto"]
            try:
                LogisticsAuto.objects.get(
                    departure_city=dep_city,
                    destination_city=dest_city,
                )
                return redirect("auto_edit")
                return redirect("auto_edit")
            except LogisticsAuto.DoesNotExist:
                LogisticsAuto.objects.create(
                    departure_city=dep_city,
                    destination_city=dest_city,
                    cost_per_tonn_auto=price,
                )
                return redirect("auto_home")
                return redirect("auto_home")
            except LogisticsAuto.MultipleObjectsReturned:
                form.add_error(None, "Больше одного значения найдено")
    else:
        form = AutoAddForm()
        form = AutoAddForm()

    context = {
        "form": form,
        "title": "Добавление рейса",
    }
    return render(request, "logistics/auto_edit.html", context)
    context = {
        "form": form,
        "title": "Добавление рейса",
    }
    return render(request, "logistics/auto_edit.html", context)


# Удаление рейса авто
def auto_delete_view(request):
# Удаление рейса авто
def auto_delete_view(request):
    if request.method == "POST":
        form = AutoDeleteForm(request.POST)
        form = AutoDeleteForm(request.POST)
        if form.is_valid():
            try:
                del_trip = LogisticsAuto.objects.get(id=form.cleaned_data["trip"])
                del_trip.delete()
                return redirect("auto_home")
                return redirect("auto_home")
            except LogisticsAuto.DoesNotExist:
                form.add_error(None, "Ошибка удаления рейса (не найдено)")
                form.add_error(None, "Ошибка удаления рейса (не найдено)")
            except LogisticsAuto.MultipleObjectsReturned:
                form.add_error(None, "Ошибка удаления рейса (найдено больше 1)")
                form.add_error(None, "Ошибка удаления рейса (найдено больше 1)")

    else:
        form = AutoDeleteForm()
        form = AutoDeleteForm()

    context = {
        "form": form,
        "title": "Удаление рейса",
    }
    return render(request, "logistics/auto_edit.html", context)
    context = {
        "form": form,
        "title": "Удаление рейса",
    }
    return render(request, "logistics/auto_edit.html", context)


# Изменение цены рейса авто
def auto_edit_view(request):
# Изменение цены рейса авто
def auto_edit_view(request):
    if request.method == "POST":
        form = AutoEditForm(request.POST)
        form = AutoEditForm(request.POST)
        if form.is_valid():
            price = form.cleaned_data["cost_per_tonn_auto"]
            try:
                query_trip = LogisticsAuto.objects.get(id=form.cleaned_data["trip"])
                query_trip.cost_per_tonn_auto = price
                query_trip.save()
                return redirect("auto_home")
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


def auto_add_requisites_view(request):
    if request.method == "POST":
        form = AutoAddRequisitesForm(request.POST)
        if form.is_valid():
            form_city = form.cleaned_data["city"].capitalize()
            form_region = form.cleaned_data["region"].capitalize()
            form_fed_district = form.cleaned_data["federal_district"].capitalize()
            try:
                LogisticsCity.objects.get(
                    city=form_city,
                )
                return redirect("auto_home")
            except LogisticsCity.DoesNotExist:
                LogisticsCity.objects.create(
                    city=form_city,
                    region=form_region,
                    federal_district=form_fed_district,
                )
                return redirect("auto_home")
            except LogisticsCity.MultipleObjectsReturned:
                form.add_error(None, "Больше одного значения найдено")
    else:
        form = AutoAddRequisitesForm()

    context = {"form": form, "title": "Добавление населенного пункта"}
    return render(request, "logistics/auto_edit.html", context)


def auto_edit_requisites_view(request):
    if request.method == "POST":
        form = AutoEditRequisitesForm(request.POST)
        if form.is_valid():
            form_city = form.cleaned_data["city"]
            form_region = form.cleaned_data["region"].capitalize()
            form_fed_district = form.cleaned_data["federal_district"]
            try:
                edit_city = LogisticsCity.objects.get(id=form_city)
                edit_city.region = form_region
                edit_city.federal_district = form_fed_district
                edit_city.save()
                return redirect("auto_home")
            except LogisticsCity.DoesNotExist:
                form.add_error(None, "Ошибка изменения рейса (направление не найдено)")
            except LogisticsCity.MultipleObjectsReturned:
                form.add_error(None, "Ошибка изменения рейса (найдено больше 1)")

    else:
        form = AutoEditRequisitesForm()

    context = {
        "form": form,
        "title": "Изменение населенного пункта",
    }
    return render(request, "logistics/auto_edit.html", context)


def auto_delete_requisites_view(request):
    if request.method == "POST":
        form = AutoDeleteRequisitesForm(request.POST)
        if form.is_valid():
            try:
                del_city = LogisticsCity.objects.get(id=form.cleaned_data["city"])
                del_city.delete()
                return redirect("auto_home")
            except LogisticsCity.DoesNotExist:
                form.add_error(None, "Ошибка удаления насленного пункта (не найдено)")
            except LogisticsCity.MultipleObjectsReturned:
                form.add_error(
                    None, "Ошибка удаления насленного пункта (найдено больше 1)"
                )

    else:
        form = AutoDeleteRequisitesForm()

    context = {
        "form": form,
        "title": "Удаление населенного пункта",
    }
    return render(request, "logistics/auto_edit.html", context)


# Таблица ж/д перевозок
def rw_home_view(request):
    data_rw = LogisticsRailwayStations.objects.all()
    context = {
        "rw_table": data_rw,
        "title": "Таблица ж/д перевозок",
    }
    return render(request, "logistics/rw_home.html", context)


# Добавление ж/д перевозки
def rw_add_view(request):
    if request.method == "POST":
        form = RwAddForm(request.POST)
        if form.is_valid():
            form_dep_station = form.cleaned_data["departure_station_name"]
            form_dest_station = form.cleaned_data["destination_station_name"]
            dep_station = RailwayStations.objects.get(pk=form_dep_station)
            dest_station = RailwayStations.objects.get(pk=form_dest_station)
            cost_per_tonn_rw = form.cleaned_data["cost_per_tonn_rw"]
            try:
                LogisticsRailwayStations.objects.get(
                    departure_station_name=dep_station,
                    destination_station_name=dest_station,
                )
                return redirect("rw_home")
            except LogisticsRailwayStations.DoesNotExist:
                LogisticsRailwayStations.objects.create(
                    departure_station_name=dep_station,
                    destination_station_name=dest_station,
                    cost_per_tonn_rw=cost_per_tonn_rw,
                )
                return redirect("rw_home")
            except LogisticsRailwayStations.MultipleObjectsReturned:
                form.add_error(None, "Больше одного значения найдено")
    else:
        form = RwAddForm()

    context = {"form": form, "title": "Добавление ж/д перевозки"}
    return render(request, "logistics/rw_edit.html", context)


# Удаление ж/д перевозки
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
                form.add_error(None, "Ошибка изменения (не найдено)")
            except LogisticsRailwayStations.MultipleObjectsReturned:
                form.add_error(None, "Ошибка изменения (найдено больше 1)")

    else:
        form = RwDeleteForm()

    context = {
        "form": form,
        "title": "Удаление ж/д перевозки",
    }
    return render(request, "logistics/rw_edit.html", context)


# Изменение ж/д перевозки
def rw_edit_view(request):
    if request.method == "POST":
        form = RwEditForm(request.POST)
        if form.is_valid():
            try:
                query_trip = LogisticsRailwayStations.objects.get(
                    id=form.cleaned_data["trip"]
                )
                cost_per_tonn_rw = form.cleaned_data["cost_per_tonn_rw"]
                query_trip.cost_per_tonn_rw = cost_per_tonn_rw
                query_trip.save()
                return redirect("rw_home")
            except LogisticsRailwayStations.DoesNotExist:
                form.add_error(None, "Ошибка изменения (не найдено)")
            except LogisticsRailwayStations.MultipleObjectsReturned:
                form.add_error(None, "Ошибка изменения (найдено больше 1)")

    else:
        form = RwEditForm()

    context = {
        "form": form,
        "title": "Изменение цены ж/д перевозки",
    }
    return render(request, "logistics/rw_edit.html", context)


# Добавление реквизитов ж/д перевозки
def rw_add_requisites_view(request):
    if request.method == "POST":
        form = RwAddRequisitesForm(request.POST)
        if form.is_valid():
            form_station_name = form.cleaned_data["station_name"].capitalize()
            form_station_id = form.cleaned_data["station_id"]
            form_station_branch = form.cleaned_data["station_branch"].upper()
            try:
                RailwayStations.objects.get(
                    station_name=form_station_name,
                )
                return redirect("rw_home")
            except RailwayStations.DoesNotExist:
                RailwayStations.objects.create(
                    station_name=form_station_name,
                    station_id=form_station_id,
                    station_branch=form_station_branch,
                )
                return redirect("rw_home")
            except RailwayStations.MultipleObjectsReturned:
                form.add_error(None, "Больше одного значения найдено")
    else:
        form = RwAddRequisitesForm()

    context = {"form": form, "title": "Добавление реквизитов ж/д перевозки"}
    return render(request, "logistics/rw_edit.html", context)


# Удаление реквизитов ж/д перевозки
def rw_delete_requisites_view(request):
    if request.method == "POST":
        form = RwDeleteRequisitesForm(request.POST)
        if form.is_valid():
            try:
                del_trip = RailwayStations.objects.get(id=form.cleaned_data["station"])
                del_trip.delete()
                return redirect("rw_home")
            except RailwayStations.DoesNotExist:
                form.add_error(None, "Ошибка удаления ж/д реквизитов (не найдено)")
            except RailwayStations.MultipleObjectsReturned:
                form.add_error(
                    None, "Ошибка удаления ж/д реквизитов (найдено больше 1)"
                )

    else:
        form = RwDeleteRequisitesForm()

    context = {
        "form": form,
        "title": "Удаление реквизитов ж/д перевозки",
    }
    return render(request, "logistics/auto_edit.html", context)


# Изменение реквизитов ж/д перевозки
def rw_edit_requisites_view(request):
    if request.method == "POST":
        form = RwEditRequisitesForm(request.POST)
        if form.is_valid():
            form_station_name = form.cleaned_data["station_name"].capitalize()
            form_station_id = form.cleaned_data["station_id"]
            form_station_branch = form.cleaned_data["station_branch"].upper()
            try:
                edit_trip = RailwayStations.objects.get(station_name=form_station_name)
                edit_trip.station_id = form_station_id
                edit_trip.station_branch = form_station_branch
                edit_trip.save()
                return redirect("rw_home")
            except RailwayStations.DoesNotExist:
                form.add_error(
                    None, "Ошибка изменения ж/д реквизитов (направление не найдено)"
                )
            except RailwayStations.MultipleObjectsReturned:
                form.add_error(
                    None, "Ошибка изменения ж/д реквизитов (найдено больше 1)"
                )

    else:
        form = RwEditRequisitesForm()

    context = {
        "form": form,
        "title": "Изменение реквизитов ж/д перевозки",
    }
    return render(request, "logistics/rw_edit.html", context)
