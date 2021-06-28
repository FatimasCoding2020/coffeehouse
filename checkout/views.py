import stripe
import datetime
import random
from django.shortcuts import render, HttpResponseRedirect
from coffeehouse.verify_request import verify_request
from django.contrib.auth.decorators import login_required


stripe.api_key="sk_test_51J6EwyCfm5h2C4JqXa6JXlJXrJmoIGVkJOs7ni46ScOEDY4xSCkvAO0m56wEAw2InfhO3to8tKqnzCOmuYmOBsjQ00rEFzBFo0"

# Create your views here.

@verify_request
@login_required
def checkout(request):
    """
    This function includes the posst request which get shipping information and payment card details and proceed for payment 
    and returns to payment complete page

    """
    cart_data = request.session['cart']
    has_item = True if len(cart_data)>0 else False
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        street_address1 = request.POST.get('street_address1')
        street_address2 = request.POST.get('street_address2')
        town_or_city = request.POST.get('town_or_city')
        country = request.POST.getlist('country')[0]
        postcode = request.POST.get('postcode')
        card_number = request.POST.get('cardnumber')
        card_date = request.POST.get('card_date')
        card_cvv = request.POST.get('card_cvv')

        card_date = card_date.split('/')
        card_expmonth = card_date[0]
        card_expyear = card_date[1]

        print(card_number,card_expmonth,card_expyear,country)

        tokenid = generate_card_token(card_number,card_expmonth,card_expyear,card_cvv)

        payment_done = create_payment_charge(tokenid,request.session['grand_total'])
        print("payment_done",payment_done)
        order_date = str(datetime.datetime.now().ctime())
        order_id = str(random.randint(123452,984793))
        cart_result = request.session['cart']

        shipping_price = '.2f' % 3.0 if float(request.session['bag_total']) < 45 else '0.00'
        order_info = dict(name=full_name,street_address1=street_address1,phone_number=phone_number,country=country,
        street_address2=street_address2,town_or_city=town_or_city,postcode=postcode,email=email)
        request.session['order_info'] = order_info
        request.session['order_data'] = cart_result
        request.session['order_date'] = order_date
        request.session['order_id'] = order_id
        return HttpResponseRedirect('/completeorder')


    return render(request,'checkout/checkout.html',{'carts':cart_data,'has_item':has_item})


@verify_request
@login_required
def complete_order(request):
    """
    This is order complete page showing summary of order product
    """
    order_info = request.session['order_info']
    order_data = request.session['order_data']
    billing = dict(bag_total=request.session['bag_total'],
                grand_total=request.session['grand_total'],shipping_price=request.session['shipping_price'])
    del request.session['cart']
    del request.session['bag_total']
    del request.session['grand_total']
    del request.session['shipping_price']
    has_item = False
    return render(request,'checkout/completeorder.html',{'carts':order_data,'billing':billing,'order':order_info,'has_item':has_item})


def generate_card_token(cardnumber,expmonth,expyear,cvv):
    """
    This function generates the stripe card token for payment
    """

    data= stripe.Token.create(
            card={
                "number": str(cardnumber),
                "exp_month": int(expmonth),
                "exp_year": int(expyear),
                "cvc": str(cvv),
            })
    card_token = data['id']

    return card_token


def create_payment_charge(tokenid,amount):
    """
    This function creat the stripe  payment
    """

    payment = stripe.Charge.create(
                amount= int(float(amount))*100,                  # convert amount to cents
                currency='usd',
                description='Example charge',
                source=tokenid,
                )

    payment_check = payment['paid']    # return True for payment

    return payment_check