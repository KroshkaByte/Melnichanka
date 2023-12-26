from django.shortcuts import render


def index_view(request):
    return render(request, 'voiceconvert/index.html')


def page_not_found_view(request, exception):
    pass
