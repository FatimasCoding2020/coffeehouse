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
    cart_data = request.session['cart'] if 'cart' in request.session else []
    has_item = True if len(cart_data)>0 else False
    request.session['has_item'] = has_item
    if not has_item:
        return render(request, 'shopping_bag/emptybag.html')
    return render(request, 'shopping_bag/shoppingbag.html',{'carts': cart_data,'has_item':has_item})


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
        shipping_price = '%.2f' % 3 if subtotal < 45 else 0
        total = '%.2f' % total
        subtotal = '%.2f' % subtotal
        cart_data =dict(name=product_data.name,image_link=image,quantity=quantity,pid=product_id,price=price,
        subtotal=subtotal,sku=product_data.sku,total=total,shipping_price=shipping_price)
        cart_result = [] if 'cart' not in request.session else request.session['cart']
        cart_result.append(cart_data)
        print("***************************")
        print(cart_result,cart_data)
        print("***************************")
        request.session['cart'] = cart_result
        grand_total = sum([float(d['total']) for d in cart_result])
        bag_total = sum([float(d['subtotal']) for d in cart_result])
        bag_total = '%.2f' % grand_total
        grand_total = '%.2f' % grand_total
        request.session['bag_total'] = bag_total
        request.session['grand_total'] = grand_total
        request.session['shipping_price'] = '%.2f' % 3 if float(bag_total) < 45 else '0.00'
        has_item = True if len(cart_result)>0 else False
        request.session['has_item'] = has_item
        messages.info(request, str(product_data.name) + " added to bag!")
        return HttpResponseRedirect('/bag')


@verify_request
def delete_from_shopping_bag(request,pid):
    
    """Delete the item from the shopping bag"""
    cart_list = request.session['cart']
    for i in range(0,len(cart_list)):
        if str(cart_list[i]['pid']) == str(pid):
            del cart_list[i]
            break
    request.session['cart'] = cart_list
    grand_total = sum([float(d['total']) for d in cart_list])
    bag_total = sum([float(d['subtotal']) for d in cart_list])
    bag_total = '%.2f' % grand_total
    grand_total = '%.2f' % grand_total
    request.session['bag_total'] = bag_total
    request.session['grand_total'] = grand_total
    request.session['shipping_price'] = '%.2f' % 3 if float(bag_total) < 45 else '0.00'

    return HttpResponseRedirect('/bag')


def update_bag(request):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        product_id = request.POST.get('pid')
        price = request.POST.get('price')
        product_data = Product.objects.get(id=int(product_id))
        subtotal = round(float(price) * int(quantity),2)
        total = subtotal+3.00 if subtotal < 45 else subtotal
        image = str(product_data.image.url).replace('static','')
        shipping_price = '%.2f' % 3 if subtotal < 45 else 0
        total = '%.2f' % total
        subtotal = '%.2f' % subtotal
        cart_data =dict(name=product_data.name,image_link=image,quantity=quantity,pid=product_id,price=price,
        subtotal=subtotal,sku=product_data.sku,total=total,shipping_price=shipping_price)

        cart_result = request.session['cart']
        new_result = []
        for d  in cart_result:
            print("d['pid'] == product_id ",d['pid'] == product_id )
            if str(d['pid']) == str(product_id) :
                d['quantity'] = quantity
                d['subtotal'] = subtotal
                d['total'] = total
                d['shipping_price'] = shipping_price
            new_result.append(d)

        print("***************************")
        print(cart_data)
        print("***************************")
        print(new_result)
        print("***************************")
        request.session['cart'] = new_result
        grand_total = sum([float(d['total']) for d in new_result])
        bag_total = sum([float(d['subtotal']) for d in new_result])
        bag_total = '%.2f' % grand_total
        grand_total = '%.2f' % grand_total
        request.session['bag_total'] = bag_total
        request.session['grand_total'] = grand_total
        request.session['shipping_price'] = '%.2f' % 3 if float(bag_total) > 45 else '0.00'
        has_item = True if len(cart_data)>0 else False
        request.session['has_item'] = has_item
        messages.info(request, str(product_data.name) + " added to bag!")
        return HttpResponseRedirect('/bag')


def merge(dict1, dict2):
    return(dict1.update(dict2))