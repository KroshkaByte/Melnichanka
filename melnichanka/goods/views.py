from django.shortcuts import render

# from .forms import GoodsAddForm
from .models import Goods


def goods_home_view(request):
    goods_data = Goods.objects.all()
    context = {
        "goods_table": goods_data,
        "title": "Таблица товаров",
    }
    return render(request, "goods/goods_home.html", context)


# def goods_add_view(request):
#     if request.method == "POST":
#         form = GoodsAddForm(request.POST)
#         if form.is_valid():
#             goods_data = form.cleaned_data
#             try:
#                 Goods.objects.get(
#                     flour_name=goods_data["flour_name"],
#                     brand=goods_data["brand"],
#                     unit_weight=goods_data["unit_weight"],
#                 )
#             except Goods.DoesNotExist:
#                 Goods.objects.create(**goods_data)
#                 return redirect("goods_home")
#             except Goods.MultipleObjectsReturned:
#                 form.add_error(None, "Товар добавлен ранее")
#     else:
#         form = GoodsAddForm()

#     context = {"form": form, "title": "Добавление товара"}
#     return render(request, "goods/goods_add.html", context)
