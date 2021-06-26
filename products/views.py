from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .models import Product
from coffeehouse.verify_request import verify_request



@verify_request
def view_product(request,name):
    """
    This function dsiplay the single product and all product details
    """
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


@verify_request
def search_product(request):
    """
    This function search the product and displayed the matched product
    """

    if request.method == 'POST':
        searchstring = request.POST.get('searchstring')
        if len(searchstring) !=0:
            product_data = Product.objects.filter(name__contains=searchstring).first()
            url = '/product/'+product_data.name if product_data is not None else '/#collection'
            return HttpResponseRedirect(url)

        else:
            return HttpResponseRedirect('/')
