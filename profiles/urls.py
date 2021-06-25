from django.urls import path
from . import views

urlpatterns = [
    path('userprofile', views.view_profile, name='userprofile'),
    path('addprofile', views.add_profile, name='addprofile'),
    path('changepassword', views.change_password, name='changepassword'),
]
