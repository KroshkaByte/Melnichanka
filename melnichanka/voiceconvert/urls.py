from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('recognize_speech/', views.recognize_speech, name='recognize_speech')
]
