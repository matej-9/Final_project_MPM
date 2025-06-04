from django.forms import ModelForm
from product.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        help_texts = {
            'price' : 'Cena v €'
        }