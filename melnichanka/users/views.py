from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rest_framework import generics, viewsets
from .models import User
from .serializers import UserSerializer
from .forms import CustomUserCreationForm
from clients.models import Clients
from rest_framework import generics


# class UserAPIView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class MyUserViewSet(generics.RetrieveUpdateDestroyAPIView, generics.ListCreateAPIView):
#     # ListCreateAPIView поддерживает только операции списка и создания
#     # RetrieveUpdateDestroyAPIView добавляет поддержку добавления и удаления
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]


# class MyUserListCreateViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     http_method_names = ["get", "post"]


# class MyUserRetrieveUpdateDestroyViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     http_method_names = ["get", "put", "delete"]


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def home_view(request):
    data = Clients.objects.order_by("client_name")
    context = {"clients_table": data, "title": "Главная страница"}
    return render(request, "home.html", context)
