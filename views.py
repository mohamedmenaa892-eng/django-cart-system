from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpRequest
from stor.models import Product 
from .models import Cart , CartItem
from django.db import IntegrityError


def view_cart(request:HttpRequest):
    if request.user.is_authenticated:
        cart , _ = Cart.objects.get_or_create(user=request.user)
    else: 
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key
        cart , _ = Cart.objects.get_or_create(session_key=session_key)
    cartitem = cart.cartitem_set.select_related('product').all()
    return render(request,'cart/cart.html',{'cart':cart,
                                            'cartitem':cartitem})


def get_user_cart(request:HttpRequest):
    if request.user.is_authenticated:
        cart , created = Cart.objects.get_or_create(user=request.user)
    else:
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key
        cart , created = Cart.objects.get_or_create(session_key=session_key,user=None)
    return cart


def add_to_cart(request:HttpRequest , product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product,id=product_id)
        cart = get_user_cart(request)
        try:
            cartitem , created = CartItem.objects.get_or_create(
                cart = cart ,
                product = product
            )
        except IntegrityError :
            created = False
            cartitem = CartItem.objects.get(
                cart=cart,
                product=product
            )
        if not created :
            cartitem.quantity += 1
            cartitem.save()
    return redirect('home')


def remove_cartitem(request:HttpRequest , cartitem_id):
    if request.method == 'POST':
        user_cart = get_user_cart(request)
        cartitem = get_object_or_404(CartItem,
                                    id=cartitem_id,
                                    cart=user_cart)
        cartitem.delete()
    return redirect('cart')


def increase_item(request:HttpRequest , cartitem_id):
    if request.method == 'POST':
        user_cart = get_user_cart(request)
        cartitem = get_object_or_404(CartItem,
                                    id=cartitem_id,
                                    cart=user_cart)
        if cartitem.quantity < cartitem.product.quantity :
            cartitem.quantity += 1
            cartitem.save()
    return redirect('cart')


def decrease_item(request:HttpRequest , cartitem_id):
    if request.method == 'POST':
        user_cart = get_user_cart(request)
        cartitem = get_object_or_404(CartItem,
                                    id=cartitem_id,
                                    cart=user_cart)
        if cartitem.quantity > 1 :
            cartitem.quantity -= 1
            cartitem.save()
    return redirect('cart')