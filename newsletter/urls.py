from django.urls import path
from . import views

urlpatterns = [
    path('subscribe', views.email_subscribe, name='subscribe'),
]
