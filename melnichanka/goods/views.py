from django.shortcuts import render

from .models import Goods


def goods_home_view(request):
    goods_data = Goods.objects.all()
    context = {
        "goods_table": goods_data,
        "title": "Таблица товаров",
    }
    return render(request, "goods/goods_home.html", context)
