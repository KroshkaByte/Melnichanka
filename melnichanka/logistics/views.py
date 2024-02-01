from django.shortcuts import redirect, render

from .forms import LogisticsAddForm, LogisticsDeleteForm, LogisticsEditForm
from .models import LogisticsAuto


def logistics_home_view(request):
    data = LogisticsAuto.objects.all()
    context = {
        "logistics_table": data,
    }

    return render(request, "logistics/log_home.html", context)


def logistics_add_view(request):
    if request.method == "POST":
        form = LogisticsAddForm(request.POST)
        if form.is_valid():
            dep_city = form.cleaned_data.get("departure_city").capitalize()
            dest_city = form.cleaned_data.get("destination_city").capitalize()
            price = form.cleaned_data.get("cost_per_tonn_auto")
            try:
                LogisticsAuto.objects.get(
                    departure_city=dep_city,
                    destination_city=dest_city,
                )
                return redirect("logistics_edit")
            except LogisticsAuto.DoesNotExist:
                LogisticsAuto.objects.create(
                    departure_city=dep_city,
                    destination_city=dest_city,
                    cost_per_tonn_auto=price,
                )
                return redirect("logistics_home")
            except LogisticsAuto.MultipleObjectsReturned:
                form.add_error(None, "Больше одного значения найдено")
    else:
        form = LogisticsAddForm()

    context = {"form": form, "title": "Добавление рейса"}
    return render(request, "logistics/log_edit.html", context)


def logistics_delete_view(request):
    if request.method == "POST":
        form = LogisticsDeleteForm(request.POST)
        if form.is_valid():
            try:
                del_trip = LogisticsAuto.objects.get(id=form.cleaned_data["trip"])
                del_trip.delete()
                return redirect("logistics_home")
            except LogisticsAuto.DoesNotExist:
                form.add_error(None, "Ошибка изменения рейса (не найдено)")
            except LogisticsAuto.MultipleObjectsReturned:
                form.add_error(None, "Ошибка изменения рейса (найдено больше 1)")

    else:
        form = LogisticsDeleteForm()

    context = {"form": form, "title": "Удаление рейса"}
    return render(request, "logistics/log_edit.html", context)


def logistics_edit_view(request):
    if request.method == "POST":
        form = LogisticsEditForm(request.POST)
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
                return redirect("logistics_home")
            except LogisticsAuto.DoesNotExist:
                form.add_error(None, "Ошибка изменения рейса (направление не найдено)")
            except LogisticsAuto.MultipleObjectsReturned:
                form.add_error(None, "Ошибка изменения рейса (найдено больше 1)")

    else:
        form = LogisticsEditForm()

    context = {"form": form, "title": "Изменение цены рейса"}
    return render(request, "logistics/log_edit.html", context)
