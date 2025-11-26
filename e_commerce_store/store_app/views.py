from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem
# Create your views here.

#creat product_list page
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store_app/product_list.html', {'products': products})

#create add_to_cart page
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

#creat shopping cart page
def cart(request):
    items = CartItem.objects.all()
    total = sum(item.total_price() for item in items)
    return render(request, 'store_app/cart.html', {'items': items, 'total': total})

# check out page
def checkout(request):
    items = CartItem.objects.all()
    total = sum(item.total_price() for item in items)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')

        items.delete()

        return render(request, 'store_app/checkout_success.html', {'name': name, 'total': total})
    return render(request, 'store_app/checkout.html', {'items': items, 'total': total})