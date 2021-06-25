from django.shortcuts import render
from products.models import Product
from coffeehouse.verify_request import verify_request


# Create your views here.

@verify_request
def contact(request):
    products = Product.objects.all()
    product_data = []
    product_url = [{'name':p.name} for p in products]
    cart_data = request.session['cart'] if 'cart' in request.session else {}
    has_item = True if len(cart_data)>0 else False
    for product in products:
        product_data.append({
            'image':str(product.image.url).replace('static',''),
            'name':product.name,
            'price':float(product.price),
            'description':product.description,
            'sku':product.sku
        })
    request.session['data'] = product_url
    return render(request, 'contacts/contact.html', {'data':product_data,'cart':cart_data,'has_item':has_item})