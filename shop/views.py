from django.shortcuts import render
from django.views.generic import ListView, DetailView

from shop.models import Product


class ProductListView(ListView):
    model = Product
    extra_context = {'title': 'Каталог'}


class ProductDetailView(DetailView):
    model = Product
    extra_context = {'title': 'Подробно'}
