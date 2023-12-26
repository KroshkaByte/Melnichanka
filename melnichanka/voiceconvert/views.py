from django.shortcuts import render

from django.http import JsonResponse
import speech_recognition as sr


def index(request):
    return render(request, 'voiceconvert/index.html')


def recognize_speech(request):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите что-нибудь:...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        response_data = {'success': True, 'text': text}
    except sr.UnknownValueError:
        response_data = {'success': False, 'error': 'Речь не распознана'}
    except sr.RequestError as e:
        response_data = {
            'success': False, 'error': f'Ошибка при запросе к сервису распознавания: {e}'}

    return JsonResponse(response_data)
