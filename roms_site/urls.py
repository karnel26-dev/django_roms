from django.urls import path
from .views import ListMenuItemView, CreateMenuItemView


urlpatterns = [
    path('', ListMenuItemView.as_view(), name='menu'),
    path('add/', CreateMenuItemView.as_view(), name='menu_add_item'),
]