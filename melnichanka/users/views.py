from clients.models import Clients
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm


# Класс авторизации пользователя
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# Домашняя страница
def home_view(request):
    data = Clients.objects.order_by("client_name")
    context = {"clients_table": data, "title": "Главная страница"}
    return render(request, "home.html", context)
