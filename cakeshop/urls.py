from django.urls import path
from . import views

app_name = 'cakeshop'

urlpatterns = [
    path('', views.cake_list, name='menu'),
    path('cake/<int:pk>/', views.cake_detail, name='cake_detail'),
    path('cate/<int:pk>/', views.cate_detail, name='cate_detail'),
    path('shop', views.cakes_list, name='shop'),
    path('addtocart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart', views.cart_list, name='cart'),
    path('search', views.search, name='search'),
    path('update/<int:pk>/', views.cart_update, name='update_item'),
    path('remove/<int:pk>/', views.cart_remove, name='remove_item'),
]
