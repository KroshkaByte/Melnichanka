from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import UserCreationForm
from .services import recognize_speech


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def home_view(request):
    return render(request, "home.html")

def recognize_speech_view(request):
    return recognize_speech(request)

def page_not_found_view(request, exception):
    pass
