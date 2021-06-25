from django.urls import path
from . import views

urlpatterns = [
    path('faq', views.view_faq, name='faq'),
]
