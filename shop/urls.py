from django.urls import path

from shop.apps import ShopConfig
from shop.views import ProductListView, ProductDetailView

app_name = ShopConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
]