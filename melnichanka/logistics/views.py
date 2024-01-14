from django.shortcuts import render

from .models import LogisticsAuto


def logistics_home_view(request):
    data = LogisticsAuto.objects.all()
    context = {"logistics_table": data}
    return render(request, "logistics/log_home.html", context)
