from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='home'),
    path('recognize_speech/', views.recognize_speech_view, name='recognize_speech')
]
