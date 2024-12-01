from django.urls import path
from product import views
from .views import ShowAllProduct


urlpatterns=[
    path('',views.ShowAllProduct,name='showProducts'),
    path('product/<int:pk>',views.ProductDetails,name='Product'),
    #path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('reset-cart/', views.reset_cart, name='reset_cart'),
    path('cart/', views.CartView, name='cart_view'),
    path('checkout/', views.order_success, name='checkout'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('submit_form/', views.submit_form,name="submit_form"),
    
]