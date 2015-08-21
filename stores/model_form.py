from django.forms import ModelForm
from .models import Store


class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'category', 'city', 'area',
                  'address', 'post_code', 'telephone',
                  'website']
