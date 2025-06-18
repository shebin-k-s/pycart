from django.shortcuts import redirect, render

from products.models import Product
from .models import Order, OrderedItem

from django.contrib.auth.decorators import login_required

@login_required(login_url='account')
def cart_view(request):

    if request.POST:
        item_id = request.POST.get('item_id')

        item = OrderedItem.objects.get(id=item_id)
        item.delete()

        return redirect('cart')

    user = request.user

    customer = user.profile

    cart = Order.objects.get(
        owner=customer,
        order_status=Order.CART_STAGE
    )

    cart_items = cart.added_items.all()

    return render(request, 'cart.html', {'cart_items': cart_items})


@login_required(login_url='account')
def add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.profile
        quantity = request.POST.get('quantity')
        product_id = request.POST.get('product_id')

        product = Product.objects.get(pk=product_id)

        print(product_id)
        print(quantity)

        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )

        ordered_item = OrderedItem.objects.create(
            product=product,
            owner=cart_obj,
            quantity=quantity
        )

        return redirect('cart')

    return render(request, 'cart.html')
