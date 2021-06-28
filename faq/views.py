from django.shortcuts import render
from products.models import Product
from coffeehouse.verify_request import verify_request


# Create your views here.

@verify_request
def view_faq(request):
    """
    This function dsiplay the faq page which includes multiple QnA
    """
    products = Product.objects.all().order_by('name')
    product_data = []
    product_url = [{'name':p.name} for p in products]
    cart_data = request.session['cart'] if 'cart' in request.session else {}
    has_item = True if len(cart_data)>0 else False
    request.session['data'] = product_url
    return render(request, 'faq/faq.html', {'cart':cart_data,'has_item':has_item})