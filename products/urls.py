from django.urls import path
from . import views

urlpatterns = [
    path('product/<str:name>', views.view_product, name='product'),
    path('search', views.search_product, name='search'),
]
