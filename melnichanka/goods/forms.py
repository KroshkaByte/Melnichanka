from django import forms

from melnichanka.goods.constants import BRANDS


class GoodsHomeForm(forms.Form):
    flour_name = forms.CharField(max_length=100, label="Наименование товара")
    unit_weight = forms.IntegerField(label="Вес единицы")
    group_quantity = forms.IntegerField(label="Количество в упаковке")
    pallet_weight = forms.IntegerField(label="Вес на паллете")
    brand = forms.ChoiceField(widget=forms.Select(), choices=BRANDS, label="Брэнд")
    price = forms.NumberInput(label="Цена")

class GoodsAddForm(forms.Form):
    pass

class GoodsEditForm(forms.Form):
    pass

class GoodsDeleteForm(forms.Form):
    pass
