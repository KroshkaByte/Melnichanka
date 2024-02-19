from django.shortcuts import redirect, render

from .forms import GoodsHomeForm
from .models import Goods


def goods_home_view(request):
    goods_data = Goods.objects.all()
    context = {
        "goods_table": goods_data,
        "title": "Таблица товаров",
    }
    return render(request, "goods/goods_home.html", context)


def goods_add_view(request):
    if request.method == "POST":
        form = GoodsHomeForm(request.POST)
        if form.is_valid():
            goods_data = form.cleaned_data
            try:
                Goods.objects.create(**goods_data)
                return redirect("goods_home")
            except Goods.MultipleObjectsReturned:
                form.add_error(None, "Товар добавлен ранее")
    else:
        form = GoodsHomeForm()

    context = {"form": form, "title": "Добавление товара"}
    return render(request, "goods/goods_add.html", context)


def goods_edit_view(request):
    if request.method == "POST":
        form = GoodsHomeForm(request.POST)
        if form.is_valid():
            # goods_data = form.cleaned_data
            try:
                form.save()
                return redirect("goods_home")
            except Exception as e:
                form.add_error(None, f"Не удаллось сохранить, произошла ошибка: {str(e)}")
    else:
        form = GoodsHomeForm()

    context = {"form": form, "title": "Добавление товара"}
    return render(request, "goods/goods_edit.html", context)
