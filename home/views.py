from django.shortcuts import render
from products.models import Product
from allauth.account.views import LoginView


def index(request):
    """ This is a View function mapped to homepage returning the list of product"""

    products = Product.objects.all()
    product_data = []
    for product in products:
        product_data.append({
            'image':str(product.image.url).replace('static',''),
            'name':product.name,
            'price':float(product.price),
            'description':product.description,
            'sku':product.sku
        })
    request.session['data'] = product_data
    return render(request, 'home/index.html', {'data':product_data})
