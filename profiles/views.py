from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from products.models import Product
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate
from coffeehouse.verify_request import verify_request


# Create your views here.

@verify_request
@login_required
def view_profile(request):
    """
    This function dsiplay the user profile and his/her details
    """
    products = Product.objects.all().order_by('name')
    product_data = []
    profile = UserProfile.objects.filter(user_id=request.user.id).first()
    print("profile:", profile)
    has_profile = False if profile is None else True
    product_url = [{'name':p.name} for p in products]
    cart_data = request.session['cart'] if 'cart' in request.session else {}
    has_item = True if len(cart_data)>0 else False
    request.session['data'] = product_url
    return render(request, 'profiles/profile.html', {'profile':profile,'carts':cart_data, 'has_profile':has_profile, 'has_item':has_item})


@verify_request
@login_required
def add_profile(request):
    """
    This function includes the code to update the user info to complete the profile
    """

    if request.method == 'POST':
        data = request.POST.dict()
        data['country'] = data['country']
        data['user_id'] = request.user.id
        form = UserProfileForm(data)
        print("form------------------------",data, form.is_valid())
        if form.is_valid():
            user_profile = UserProfile.objects.get(user_id=request.user.id)
            if user_profile is not None:
                user_profile.full_name = data['full_name']
                user_profile.phone_number = data['phone_number']
                user_profile.country = data['country']
                user_profile.postcode = data['postcode']
                user_profile.street_address1 = data['street_address1']
                user_profile.town_or_city = data['town_or_city']
                user_profile.street_address2 = data['street_address2']
                user_profile.save()
            else:
                UserProfile.objects.create(**data)
        messages.info(request, "Delivery information updated")
        return HttpResponseRedirect('/userprofile')


@verify_request
@login_required
def change_password(request):
    """
    This function includes the code to change the user password
    """

    products = Product.objects.all().order_by('name')
    product_data = []
    profile = User.objects.get(id=request.user.id)

    product_url = [{'name':p.name} for p in products]
    cart_data = request.session['cart'] if 'cart' in request.session else {}
    has_item = True if len(cart_data)>0 else False
    request.session['data'] = product_url
    if request.method == 'POST':
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        user = authenticate(username=request.user.username, password=password)
        if user is None:
            messages.error(request, "Your current password doesn't match")
            return HttpResponseRedirect('/changepassword')

        if new_password != confirm_password:
            messages.error(request, "New password fields doesn't match")
            return HttpResponseRedirect('/changepassword')

        user = User.objects.get(id=request.user.id)
        user.set_password(confirm_password)
        messages.info(request, "Password has been changed successfully ")
        return HttpResponseRedirect('/userprofile')


    return render(request, 'profiles/changepassword.html', {'profile':profile,'carts':cart_data,'has_item':has_item})


