from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from products.models import Product
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate


# Create your views here.

@login_required
def view_profile(request):
    products = Product.objects.all()
    product_data = []
    profile = User.objects.get(id=request.user.id)

    product_url = [{'name':p.name} for p in products]
    cart_data = request.session['cart'] if 'cart' in request.session else {}
    has_item = True if len(cart_data)>0 else False
    request.session['data'] = product_url
    return render(request, 'profiles/profile.html', {'profile':profile,'cart':cart_data,'has_item':has_item})


def add_profile(request):
    if request.method == 'POST':
        data = request.POST.dict()
        print("data",data)
        data['country'] = data['country'][0]
        data['user_id'] = request.user.id
        form = UserProfileForm(data)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/userprofile')


def change_password(request):
    products = Product.objects.all()
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
        return HttpResponseRedirect('/userprofile')


    return render(request, 'profiles/changepassword.html', {'profile':profile,'cart':cart_data,'has_item':has_item})


