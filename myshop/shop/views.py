from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm
from .models import Category, Product
from cart.forms import CartAddProductForm

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,
        slug=category_slug)
        products = products.filter(category=category)
    return render(request,
        'shop/product/list.html',
        {'category': category,
        'categories': categories,
        'products': products})
    
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
    id=id,
    slug=slug,
    available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
        'shop/product/detail.html',
        {'product': product,
         'cart_product_form': cart_product_form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=['password'])

            if user is not None:
                if user.is_active():
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                form = LoginForm()
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'shop/login.html', {'form': form})

def user_logout(request):
    logout(request)
    render(request, 'product/product_list.html')

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form':form})


