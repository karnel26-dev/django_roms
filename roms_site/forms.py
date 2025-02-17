from django import forms
from .models import MenuItem, Order


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

        labels = {
            'name': 'Название блюда',
            'price': 'Стоимость',
            'description': 'Описание',
        }

class OrderForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(
        queryset=MenuItem.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='Блюда'
    )
    class Meta:
        model = Order
        fields = ('table_number', 'comment', 'items')

        labels = {
            'table_number': 'Номер столика',
            'items': 'Состав заказа',
            'comment': 'Комментарий к заказу',
        }

class UpdateOrderForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(
        queryset=MenuItem.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='Блюда'
    )
    class Meta:
        model = Order
        fields = ('table_number', 'comment', 'items', 'status')

        labels = {
            'table_number': 'Номер столика',
            'items': 'Состав заказа',
            'comment': 'Комментарий к заказу',
            'status': 'Статус заказа',
        }
