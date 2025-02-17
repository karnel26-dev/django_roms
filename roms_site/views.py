from django.views.generic import (CreateView, UpdateView,
                                  DetailView, ListView, DeleteView)
from django.urls import reverse_lazy

from .forms import MenuItemForm, OrderForm
from .models import MenuItem, Order


class CreateMenuItemView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'roms_site/menu/menu_add_item.html'
    success_url = reverse_lazy('menu')

class ListMenuItemView(ListView):
    model = MenuItem
    template_name = 'roms_site/menu/menu.html'
    context_object_name = 'menu_items'

class DetailMenuItemView(DetailView):
    pass

class UpdateMenuItemView(UpdateView):
    pass

class DeleteMenuItemView(DeleteView):
    pass

class CreateOrderView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'roms_site/orders/orders_add.html'
    success_url = reverse_lazy('orders')

    def form_valid(self, form):
        order = form.save(commit=False)
        order.save()
        menu_items = self.request.POST.getlist('items')
        for item_id in menu_items:
            order.items.add(MenuItem.objects.get(pk=item_id))
        order.total_price = sum(item.price for item in order.items.all())

        return super().form_valid(form)

class ListOrderView(ListView):
    model = Order
    template_name = 'roms_site/orders/orders.html'
    context_object_name = 'orders'

class DetailOrderView(DetailView):
    model = Order
    template_name = 'roms_site/orders/orders_detail.html'
    context_object_name = 'order'

class UpdateOrderView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'roms_site/orders/orders_update.html'
    success_url = reverse_lazy('orders')

    def form_valid(self, form):
        order = form.save(commit=False)
        order.items.clear()
        order.save()
        menu_items = self.request.POST.getlist('items')
        for item_id in menu_items:
            order.items.add(MenuItem.objects.get(pk=item_id))
        order.total_price = sum(item.price for item in order.items.all())

        return super().form_valid(form)
