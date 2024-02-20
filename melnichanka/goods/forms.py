from django import forms

from .models import Goods


class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = "__all__"
