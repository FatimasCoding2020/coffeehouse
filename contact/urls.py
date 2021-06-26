from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('sendmessage', views.send_message, name='sendmessage'),
]
