from django.shortcuts import render, HttpResponseRedirect
from .models import Subscribe
from coffeehouse.verify_request import verify_request
from django.contrib import messages


# Create your views here.

def email_subscribe(request):
    """
    This function includes the code to subscribe the email and store email adresses of subscribers
    """
    if request.method == "POST":
        email = request.POST.get('email')
        check_subscribe = Subscribe.objects.filter(email=email)
        if check_subscribe.exists():
            messages.info(request, "You are already subscribed!")
            return HttpResponseRedirect('/#subscribe')
        else:
            Subscribe.objects.create(**dict(email=email))
            messages.info(request, "Your are subscribed now")
            return HttpResponseRedirect('/#subscribe')

