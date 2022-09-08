from multiprocessing import context
from unicodedata import category
from django.shortcuts import render, redirect
from .models import Category, Order, OrderItem, Product, ShippingAddress
from .forms import ShippingAddressForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
import random
PAYSTACK_PUBLIC_KEY = "pk_test_4d5007ad7bd59da7fc379331b8a7b070dc98fc7a"
random_index = 2

def HomeView(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, "babiesCorner/home.html", context)

def CartView(request):
    try:
        order = Order.objects.get(user=request.user)
    except ObjectDoesNotExist:
        order = 0
        messages.error(request, 'You do not have an active order.')

    context = {
        'order': order,
    }

    return render(request, "babiesCorner/cart.html", context)

def CategoryView(request, category_name):
    categories = Category.objects.all()
    single__category = Category.objects.get(name=category_name)
    category__products = Product.objects.filter(category=single__category)

    context = {
        'productCategories': categories,
        'category': single__category,
        'products': category__products
    }

    return render(request, "babiesCorner/category.html", context)

def Add_Product_To_Cart(request, product_name):
    single_product = Product.objects.get(name=product_name)
    order_product = OrderItem.objects.get(product=single_product)
    order_set = Order.objects.filter(user=request.user)[0]

    if order_set:
        order = order_set

        # Checking if the order item is in the order
        if order.products.filter(product=single_product.id).exists():
            order_product.quantity += 1
            order_product.save()
        else:
            order.products.add(order_product)
    else:
        order = Order.objects.create(user=request.user)
        order.items.add(order_product)

    return redirect('cart')

def Remove_Product_From_Cart(request, product_name):
    single_product = Product.objects.get(name=product_name)
    order_set = Order.objects.filter(user=request.user)

    if order_set.exists():
        order = order_set[0]
        
        # Checking if the order item is in the order
        if order.products.filter(product__name=single_product.name).exists():
            order_product = OrderItem.objects.filter(product=single_product)[0]
            order.products.remove(order_product)
        else:
            return redirect('product', product_name)
    else:
        return redirect('product', product_name)

    return redirect('cart')
    
def Remove_Single_Product_From_Cart(request, product_name):
    single_product = Product.objects.get(name=product_name)
    order_set = Order.objects.filter(user=request.user)

    if order_set.exists():
        order = order_set[0]
        
        if order.products.filter(product__name=single_product.name).exists():
            order_product = OrderItem.objects.filter(product=single_product)[0]
            if order_product.quantity > 1:
                order_product.quantity -= 1
                order_product.save()
            else:
                order.products.remove(order_product)

            messages.info(request, 'This item was updated.')
            return redirect('cart')
        else:
            messages.info(request, 'This item was not in  your cart')
            return redirect('product', product_name)
    else:
        messages.info(request, 'You do not have an active order.')
        return redirect('product', product_name)

def CheckoutView(request):
    try:
        order = Order.objects.get(user=request.user)
        shipping = ShippingAddress.objects.get(user=request.user)
    except ObjectDoesNotExist:
        order = 0
        messages.error(request, 'You do not have an active order.')

    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)

        if form.is_valid():
            newShippingAddress = form.save(commit=False)
            newShippingAddress.user = request.user
            newShippingAddress.save()

            # messages.success(request, 'Shipping address saved')
        
        return redirect('allvisitors')
    else:
        form = ShippingAddressForm()
    
    context = {
        'form': form,
        'order': order,
        'shipping': shipping,
        'user': request.user
    }
    
    return render(request, "babiesCorner/checkout.html", context)

def ContactView(request):

    return render(request, "babiesCorner/contact.html")

def ProductView(request, product_name):
    try:
        single__product = Product.objects.get(name=product_name)
        related__products = Product.objects.filter(category=single__product.category)
        order = Order.objects.get(user=request.user)
    except ObjectDoesNotExist:
        order = 0
        messages.error(request, 'You do not have an active order.')

    context = {
        'single__product': single__product,
        'relatedProducts': random.sample(list(related__products), random_index),
        'order': order,
    }

    return render(request, "babiesCorner/product.html", context)

def PaymentView(request):
    order = Order.objects.get(user=request.user)
    shipping = ShippingAddress.objects.filter(user=request.user).last()

    context = {
        'price': order.getSumTotal(),
        'object': order,
        'shipping': shipping,
        'PAYSTACK_PUBLIC_KEY': PAYSTACK_PUBLIC_KEY,
    }

    return render(request, 'babiesCorner/payment.html', context)

def SuccessView(request):

    return render(request, "babiesCorner/success.html")