from django.urls import path
from . import views

urlpatterns = [
    path('checkout', views.checkout, name='checkout'),
    path('completeorder', views.complete_order, name='complete_order'),

]
