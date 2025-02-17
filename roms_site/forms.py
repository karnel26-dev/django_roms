from django import forms
from .models import MenuItem


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

        labels = {
            'name': 'Название блюда',
            'price': 'Стоимость',
            'description': 'Описание',
        }