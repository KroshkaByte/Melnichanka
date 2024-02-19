from django import forms

from .models import Goods


class GoodsHomeForm(forms.ModelForm):
    model = Goods
    fields = "__all__"


class GoodsEditForm(forms.Form):
    pass


class GoodsDeleteForm(forms.Form):
    pass
