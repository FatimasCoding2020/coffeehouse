from django.shortcuts import render
from products.models import Product

# Create your views here.

def view_faq(request):
    products = Product.objects.all()
    product_data = []
    product_url = [{'name':p.name} for p in products]
    cart_data = request.session['cart'] if 'cart' in request.session else {}
    has_item = True if len(cart_data)>0 else False
    request.session['data'] = product_url
    return render(request, 'faq/faq.html', {'cart':cart_data,'has_item':has_item})