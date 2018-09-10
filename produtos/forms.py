from .models import Product

from django.forms import ModelForm


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'name_product',
            'cod_product',
            'amount_product',
            'prince_product',
            'img_product',
            'description',
        ]