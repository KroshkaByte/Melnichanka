from django.shortcuts import get_object_or_404, redirect, render

from .forms import ClientsAddForm, ClientsEditForm
from .models import Clients


def clients_home_view(request):
    data = Clients.objects.all()
    context = {"clients_table": data}
    return render(request, "clients/clnt_home.html", context)


def clients_add_view(request):
    if request.method == "POST":
        form = ClientsAddForm(request.POST)
        if form.is_valid():
            try:
                Clients.objects.create(**form.cleaned_data)
                return redirect("clients_home")
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
