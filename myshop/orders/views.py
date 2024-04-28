from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity'])
            # clear the cart
            cart.clear()
        return render(request,
        'orders/order/created.html',
        {'order': order})
    else:
        user = request.user
        initial_data = {'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}
        form = OrderCreateForm(initial=initial_data)
    return render(request,
        'orders/order/create.html',
        {'cart': cart, 'form': form})
