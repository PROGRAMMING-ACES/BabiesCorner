from django.urls import path
from .views import Add_Product_To_Cart, HomeView, CartView, CategoryView, CheckoutView, ContactView, ProductView, Remove_Product_From_Cart, Remove_Single_Product_From_Cart, PaymentView, SuccessView

urlpatterns = [
    path('', HomeView, name="home"),
    path('cart', CartView, name="cart"),
    path('category/<str:category_name>', CategoryView, name="category"),
    path('checkout', CheckoutView, name="checkout"),
    path('contact', ContactView, name="contact"),
    path('product/<str:product_name>', ProductView, name="product"),
    path('payment', PaymentView, name="payment"),
    path('success', SuccessView, name="success"),

    # CART FUNCTIONALITY    
    path('add/<str:product_name>', Add_Product_To_Cart, name = 'add_product_to_cart'),
    path('remove/<str:product_name>', Remove_Product_From_Cart, name = 'remove_product_from_cart'),
    path('remove_product/<str:product_name>', Remove_Single_Product_From_Cart, name = 'remove_single_product_from_cart'),
]
