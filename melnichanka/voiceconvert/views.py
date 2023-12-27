from django.shortcuts import render
from .services import recognize_speech


def index_view(request):
    return render(request, 'voiceconvert/index.html')


def recognize_speech_view(request):
    return recognize_speech(request)
