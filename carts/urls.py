from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_cart/<int:product_id>/', views.remove_to_cart, name='remove_to_cart'),
    path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),

]