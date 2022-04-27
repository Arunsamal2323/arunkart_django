from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django import forms
from .models import Account

# from .models import Account,UserProfile
# from orders.models import Order, OrderProduct
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# # Verification email
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes
# from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

# from carts.views import _cart_id
# from carts.models import Cart, CartItem
# import requests

# Create your views here.



def register(request):
    # breakpoint()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()
            messages.success(request, 'Registraion sucessfully')
            return redirect('register')

    form=RegistrationForm()
            
            
    context={
                'form':form,
                }

    return render(request, 'accounts/register.html',context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')
    


def forgotPassword(request):
    return render(request, 'accounts/forgotPassword.html')



def dashboard(request):
    # orders = Order.objects.order_by('-created_at').filter(user_id=request.user.id, is_ordered=True)
    # orders_count = orders.count()

    # userprofile = UserProfile.objects.get(user_id=request.user.id)
    # context = {
    #     'orders_count': orders_count,
    #     'userprofile': userprofile,
    # }
    return render(request, 'accounts/dashboard.html', context)
