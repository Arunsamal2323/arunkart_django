from django.shortcuts import render, redirect, get_object_or_404
# from .forms import RegistrationForm, UserForm, UserProfileForm
# from .models import Account, UserProfile
# from orders.models import Order, OrderProduct
# from django.contrib import messages, auth
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

# # Verification email
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes
# from django.contrib.auth.tokens import default_token_generator
# from django.core.mail import EmailMessage

# from carts.views import _cart_id
# from carts.models import Cart, CartItem
# import requests

# Create your views here.



def register(request):
    return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')


def dashboard(request):
    # orders = Order.objects.order_by('-created_at').filter(user_id=request.user.id, is_ordered=True)
    # orders_count = orders.count()

    # userprofile = UserProfile.objects.get(user_id=request.user.id)
    # context = {
    #     'orders_count': orders_count,
    #     'userprofile': userprofile,
    # }
    return render(request, 'accounts/dashboard.html', context)
