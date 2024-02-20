from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import GoodsForm
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
        form = GoodsForm(request.POST)
        if form.is_valid():
            goods_data = form.cleaned_data
            try:
                Goods.objects.create(**goods_data)
                return redirect("goods_home")
            except Goods.MultipleObjectsReturned:
                form.add_error(None, "Товар добавлен ранее")
    else:
        form = GoodsForm()

    context = {"form": form, "title": "Добавление товара"}
    return render(request, "goods/goods_add.html", context)


def goods_edit_view(request, pk):
    if request.method == "POST":
        form = GoodsForm(request.POST)
        if form.is_valid():
            # goods_data = form.cleaned_data
            try:
                form.save()
                return redirect("goods_home")
            except Exception as e:
                form.add_error(None, f"Не удалось сохранить, произошла ошибка: {str(e)}")
    else:
        form = GoodsForm()

    context = {"form": form, "title": "Редактирование товара"}
    return render(request, "goods/goods_edit.html", context)


def goods_delete_view(request, pk):
    instance = get_object_or_404(Goods, id=pk)

    if request.method == "POST":
        if "confirm_delete" in request.POST:
            try:
                instance.delete()
                return redirect("goods_home")
            except Goods.DoesNotExist:
                raise Http404("Ошибка удаления (запись не найдена)")

        else:
            return redirect("goods_home")

    context = {"instance": instance, "title": "Подтверждение удаления записи"}
    return render(request, "goods/goods_delete_confirm.html", context)
