from django.http import JsonResponse
import speech_recognition as sr


def recognize_speech(request):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        # что бы видеть что оно запускается, потом удалим print
        print("Говорите что-нибудь:...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        response_data = {'success': True, 'text': text}

        # Тут хранится наш текст
        print(type(text))
        print(text)
    except sr.UnknownValueError:
        response_data = {'success': False, 'error': 'Речь не распознана'}
    except sr.RequestError as e:
        response_data = {
            'success': False, 'error': f'Ошибка при запросе к сервису распознавания: {e}'}

    return JsonResponse(response_data)
