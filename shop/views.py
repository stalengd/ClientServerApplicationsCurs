from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddProductForm

def catalog(request, pk = None):
    if pk is None:
        category = None
        products = Product.objects.all()
    else:
        category = get_object_or_404(Category, pk = pk)
        products = Product.objects.filter(category = category)

    return render(request, 'shop/product/list.html', 
    {
        'category': category,
        'categories': Category.objects.all(),
        'products': products,
    })

def detail(request, pk):
    product = get_object_or_404(Product, pk = pk, available = True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', 
    {
        'product': product,
        'cart_product_form': cart_product_form
    })