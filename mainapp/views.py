from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product
# from basketapp.models import Basket
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

tit = 'amado - the best furniture store'


# def get_basket(user):
#     if user.is_authenticated:
#         return Basket.objects.filter(user=user)
#     else:
#         return []


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def main(request):
    title = tit + ' | Home'
    products = Product.objects.all()[:9]
    content = {
        'title': title,
        'products': products,
        # 'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None, page=1):
    title = tit + ' | Shop'
    links_menu = ProductCategory.objects.filter(is_active=True)
    # basket = get_basket(request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
            category = {
                'name': 'all',
                'pk': 0
            }
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by(
                'price')

        paginator = Paginator(products, 4)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
            # 'basket': basket
        }
        return render(request, 'mainapp/products.html', content)

    hot_product = get_hot_product()

    content = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        # 'basket': basket
    }
    return render(request, 'mainapp/products.html', content)


def product(request, pk):
    title = tit + ' | Product details'
    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        # 'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/product.html', content)
