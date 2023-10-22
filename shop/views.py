from django.shortcuts import render
from .models import Product, Category

def catalog(request, pk = None):
    if pk is None:
        category = None
        products = Product.objects.all()
    else:
        category = Category.objects.get(pk = pk)
        products = Product.objects.filter(category = category)

    return render(request, 'shop/product/list.html', 
    {
        'category': category,
        'categories': Category.objects.all(),
        'products': products,
    })

def detail(request, pk):
    return render(request, 'shop/product/detail.html', 
    {
        'product': Product.objects.get(pk = pk),
    })