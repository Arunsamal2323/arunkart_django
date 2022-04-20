from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
# from carts.models import Cart
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
# Create your views here.

def cart(request):
    # try:
    #     tax = 0
    #     grand_total = 0
    #     if request.user.is_authenticated:
    #         cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    #     else:
    #         cart = Cart.objects.get(cart_id=_cart_id(request))
    #         cart_items = CartItem.objects.filter(cart=cart, is_active=True)
    #     for cart_item in cart_items:
    #         total += (cart_item.product.price * cart_item.quantity)
    #         quantity += cart_item.quantity
    #     tax = (2 * total)/100
    #     grand_total = total + tax
    # except ObjectDoesNotExist:
    #     pass #just ignore

    # context = {
    #     'total': total,
    #     'quantity': quantity,
    #     'cart_items': cart_items,
    #     'tax'       : tax,
    #     'grand_total': grand_total,
    # }
    return render(request, 'store/cart.html')