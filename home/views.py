from allauth.account.views import LoginView
from django.shortcuts import render

from coffeehouse.verify_request import verify_request
from products.models import Product


@verify_request
def index(request):
    """ View to return the index page """

    products = Product.objects.all().order_by('name')
    product_data = []
    product_url = [{'name': p.name} for p in products]
    cart_data = request.session['cart'] if 'cart' in request.session else []
    has_item = True if len(cart_data) > 0 else False
    for product in products:
        product_data.append({
            'image': str(product.image.url).replace('static', ''),
            'name': product.name,
            'price': float(product.price),
            'description': product.description,
            'sku': product.sku
        })
    request.session['data'] = product_url
    return render(request, 'home/index.html',
                  {'data': product_data,
                   'carts': cart_data,
                   'has_item': has_item})
