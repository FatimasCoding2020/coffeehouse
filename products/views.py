from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product




def view_product(request,name):

    """ This is a View function mapped to product detail page returning the a particular data of the product
        here this function takes product name as function arguement
    
    """

    product = Product.objects.filter(name__iexact=name).first()
    products = Product.objects.all()
    context = {
        'data': products,
        'product':product,
        'image':str(product.image.url).replace('static','')
    
    }
    print("context:", context)
    return render(request, 'products/product_detail.html', context)