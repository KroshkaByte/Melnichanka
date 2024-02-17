from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render


from .forms import ClientsAddForm, ClientsEditForm
from .models import Clients


# Таблица клиентов
def clients_home_view(request):
    data = Clients.objects.order_by("client_name")
    context = {"clients_table": data, "title": "Список клиентов"}
    return render(request, "clients/clnt_home.html", context)


# Добавление клиента
def clients_add_view(request):
    if request.method == "POST":
        form = ClientsAddForm(request.POST)
        if form.is_valid():
            try:
                Clients.objects.create(**form.cleaned_data)
                return redirect("clients_home")
            except Clients.MultipleObjectsReturned:
                form.add_error(
                    None,
                    "Ошибка добавления клиента, клиент с такими данными уже существует",
                )
            except Exception as e:
                form.add_error(None, f"Произошла ошибка: {str(e)}")

    else:
        form = ClientsAddForm()

    context = {"form": form, "title": "Добавить клиента"}
    return render(request, "clients/clnt_add.html", context)


# Редактирование клиента
def clients_edit_view(request, pk):
    instance = get_object_or_404(Clients, id=pk)
    form = ClientsEditForm(request.POST or None, instance=instance)

    if request.method == "POST" and form.is_valid():
        try:
            form.save()
            return redirect("clients_home")
        except Exception as e:
            form.add_error(None, f"Не удаллось сохранить, произошла ошибка: {str(e)}")

    context = {"form": form, "title": "Редактирование записи"}
    return render(request, "clients/clnt_edit.html", context)


# Удаление клиента
def clients_delete_view(request, pk):
    instance = get_object_or_404(Clients, id=pk)

    if request.method == "POST":
        if "confirm_delete" in request.POST:
            try:
                instance.delete()
                return redirect("clients_home")
            except Clients.DoesNotExist:
                raise Http404("Ошибка удаления (запись не найдена)")

        else:
            return redirect("clients_home")

    context = {"instance": instance, "title": "Подтверждение удаления записи"}
    return render(request, "clients/clnt_delete_confirm.html", context)
