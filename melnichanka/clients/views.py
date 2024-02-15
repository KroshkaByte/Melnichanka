from django.db import IntegrityError
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from logistics.models import RailwayStations

from .forms import ClientsAddForm, ClientsEditForm
from .models import Clients


def clients_home_view(request):
    data = Clients.objects.order_by("client_name")
    context = {"clients_table": data}
    return render(request, "clients/clnt_home.html", context)


def clients_add_view(request):
    if request.method == "POST":
        form = ClientsAddForm(request.POST)
        if form.is_valid():
            try:
                destination_city_id = form.cleaned_data["destination_city"]
                destination_city = RailwayStations.objects.get(id=destination_city_id)
                Clients.objects.create(
                    destination_city=destination_city,
                    **{
                        key: form.cleaned_data[key]
                        for key in form.cleaned_data.keys()
                        if key != "destination_city"
                    },
                )
                return redirect("clients_home")
            except RailwayStations.DoesNotExist:
                form.add_error("destination_city", "Несуществующая ЖД станция")
            except IntegrityError:
                form.add_error(None, "Клиент с таким номером договора уже существует")
            except:
                form.add_error(None, "Ошибка добавления клиента")

    else:
        form = ClientsAddForm()

    data = {"form": form}
    return render(request, "clients/clnt_add.html", data)


def clients_edit_view(request, pk):
    instance = get_object_or_404(Clients, pk=pk)
    form = ClientsEditForm(request.POST or None, instance=instance)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("clients_home")

    return render(request, "clients/clnt_edit.html", {"form": form})


def clients_delete_view(request, pk):
    instance = get_object_or_404(Clients, pk=pk)

    if request.method == "POST":
        if "confirm_delete" in request.POST:
            try:
                instance.delete()
                return redirect("clients_home")
            except Clients.DoesNotExist:
                raise Http404("Ошибка удаления (запись не найдена)")

        else:
            return redirect("clients_home")

    return render(request, "clients/clnt_delete_confirm.html", {"instance": instance})
