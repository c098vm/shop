from django.shortcuts import render

from shop.models import Product


def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(id=pk),
        'title': product_item.name
    }
    return render(request, 'shop/product.html', context)


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Главная'
    }
    return render(request, 'shop/index.html', context)