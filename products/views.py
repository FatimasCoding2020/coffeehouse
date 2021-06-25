from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product




def view_product(request,name):
    product = Product.objects.filter(name__iexact=name).first()
    cart_data = request.session['cart'] if 'cart' in request.session else {}
    has_item = True if len(cart_data)>0 else False
    context = {
        'product':product,
        'image':str(product.image.url).replace('static',''),
        'cart': cart_data,
        'has_item':has_item
    }
    print("context:", context)
    return render(request, 'products/product_detail.html', context)