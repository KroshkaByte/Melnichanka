from django.forms import model_to_dict
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


from .forms import ClientsAddForm, ClientsEditForm
from .serializers import ClientSerializer
from .models import Clients


class ClientsAPIView(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer


class ClientsAPIUpdateView(generics.UpdateAPIView):
    # queryset из за того что используем ClientsAPIUpdateView юзеру будет возвращатся только 1 запись, а не все, как может показатся из запроса
    # Это ленивый запрос
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer


class ClientsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer


# class ClientAPIView(APIView):
#     def get(self, request):
#         clients = Clients.objects.all()
#         # clients, many=True - передаем список клиентов, many  т.к передаем не одну запись, а список
#         # .data - словарь преобразованыз данных из табл Clients
#         return Response({"clients": ClientSerializer(clients, many=True).data})

#     def post(self, request):
#         serializer = ClientSerializer(data=request.data)
#         # raise_exception=True - выводит ошибку в виде json строки {"client_name":["Обязательное поле."]}
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # client_new = Clients.objects.create(**serializer.validated_data)
#         return Response({"post": serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         try:
#             isinstance = Clients.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})

#         serializer = ClientSerializer(data=request.data, instance=isinstance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})

#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#         try:
#             isinstance = Clients.objects.get(pk=pk).delete()
#         except:
#             return Response({"error": "Object does not exists"})

#         return Response({"post": "delete client" + str(pk)})


# class ClientAPIView(generics.ListAPIView):
#     queryset = Clients.objects.all()
#     serializer_class = ClientSerializer


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
