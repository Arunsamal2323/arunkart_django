from django.shortcuts import render
from store.models import Product


def home(request):
    # import pdb; pdb.set_trace()
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products,
        
    }
    return render(request, 'home.html',context)