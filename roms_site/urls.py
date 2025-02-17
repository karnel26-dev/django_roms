from django.urls import path
from .views import (ListMenuItemView, CreateMenuItemView,
                    CreateOrderView, ListOrderView,
                    UpdateOrderView, DetailOrderView)


urlpatterns = [
    path('menu/add/', CreateMenuItemView.as_view(), name='menu_add_item'),
    path('menu/', ListMenuItemView.as_view(), name='menu'),

    path('orders/add/', CreateOrderView.as_view(), name='orders_add'),
    path('orders/<int:pk>/edit/', UpdateOrderView.as_view(), name='orders_update'),
    path('orders/<int:pk>/detail/', DetailOrderView.as_view(), name='orders_detail'),
    path('orders/', ListOrderView.as_view(), name='orders'),

]