from django.shortcuts import render


def logistics_home_view(request):
    return render(request, "logistics/log_home.html")
