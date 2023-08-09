from django.urls import path

from shop.apps import ShopConfig
from shop.views import index, product

app_name = ShopConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:pk>', product, name='product'),
]