from django.views.generic import (CreateView, UpdateView,
                                  DetailView, ListView, DeleteView)
from django.urls import reverse_lazy

from .forms import MenuItemForm
from .models import MenuItem


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

