from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect

from coffeehouse.verify_request import verify_request
from .models import Subscribe


# Create your views here.

def email_subscribe(request):
    """
    This function includes the code
    to subscribe the email and store email addresses of subscribers
    """
    if request.method == "POST":
        email = request.POST.get('email')
        check_subscribe = Subscribe.objects.filter(email=email)
        if check_subscribe.exists():
            messages.info(request, "You are already subscribed!")
            return HttpResponseRedirect('/')
        else:
            Subscribe.objects.create(**dict(email=email))
            email_to = email
            message = " Thank you, you are now " \
                      "subscribed to coffeehouse and will receive coffee news"

            send_mail("Subscription",
                      message, settings.EMAIL_HOST_USER, [email_to])
            messages.info(request, "You are now subscribed!")
            return HttpResponseRedirect('/')
