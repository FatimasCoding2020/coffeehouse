from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from coffeehouse.verify_request import verify_request
from products.models import Product


@verify_request
def view_shopping_bag(request):
    """ 
    View that renders the shopping bag page  which show the product that has been added to cart
    
    """
    cart_data = request.session['cart'] if 'cart' in request.session else {}
    has_item = True if len(cart_data)>0 else False
    if not has_item:
        return render(request, 'shopping_bag/emptybag.html')
    return render(request, 'shopping_bag/shoppingbag.html',{'cart': cart_data,'has_item':has_item})


@verify_request
def add_to_shopping_bag(request, product_id):

    """ Add a quantity of the specified product to the shoppingbag """

    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        product_data = Product.objects.get(id=int(product_id))
        subtotal = round(float(price) * int(quantity),2)
        total = subtotal+3.0 if subtotal < 45 else subtotal
        image = str(product_data.image.url).replace('static','')
        shipping_price = 3.0 if subtotal < 45 else 0
        cart_data =dict(name=product_data.name,image_link=image,quantity=quantity,pid=product_id,price=price,
        subtotal=subtotal,sku=product_data.sku,total=total,shipping_price=shipping_price)
        print("***************************")
        print(cart_data)
        print("***************************")
        request.session['cart'] = cart_data
        request.session['cart_price'] = cart_data['subtotal']
        has_item = True if len(cart_data)>0 else False
        request.session['has_item'] = has_item
        messages.info(request, "Item added to your bag")
        return HttpResponseRedirect('/bag')


@verify_request
def delete_from_shopping_bag(request):
    
    """Delete the item from the shopping bag"""

    del request.session['cart']
    return HttpResponseRedirect('/bag')


def update_bag(request):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        product_id = request.POST.get('pid')
        price = request.POST.get('price')
        product_data = Product.objects.get(id=int(product_id))
        subtotal = round(float(price) * int(quantity),2)
        total = subtotal+3.0 if subtotal < 45 else subtotal
        image = str(product_data.image.url).replace('static','')
        shipping_price = 3.0 if subtotal < 45 else 0
        cart_data =dict(name=product_data.name,image_link=image,quantity=quantity,pid=product_id,price=price,
        subtotal=subtotal,sku=product_data.sku,total=total,shipping_price=shipping_price)
        print("***************************")
        print(cart_data)
        print("***************************")
        request.session['cart'] = cart_data
        request.session['cart_price'] = cart_data['subtotal']
        has_item = True if len(cart_data)>0 else False
        request.session['has_item'] = has_item
        messages.info(request, "Item updated to your bag")
        return HttpResponseRedirect('/bag')
