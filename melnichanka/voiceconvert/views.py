from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import UserCreationForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def home_view(request):
    return render(request, "home.html")


def page_not_found_view(request, exception):
    return render(request, template_name="404.html")


def server_error_view(request):
    return render(request, template_name="500.html")
