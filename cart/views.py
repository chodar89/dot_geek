from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.core.mail import EmailMessage

import stripe

from products.models import Product, SizeChart
from order.models import Order, OrderItem
from .utility import _cart_id, _get_user_or_none
from .models import Cart, CartItem


def add_to_cart(request, product_id):
    """
    Add product to cart view
    """
    if request.method == 'POST':
        # Get item qnty and size from product card panel form
        get_item_qnty = int(request.POST.get('quantity'))
        get_item_size = request.POST.get('size')
        try:
            size = SizeChart.objects.get(id=get_item_size)
        except ObjectDoesNotExist:
            size = None
        product = Product.objects.get(id=product_id)
        user_id = _get_user_or_none(request)
        session_cart_id = _cart_id(request)
        try:
            # Check if cart already exists in database
            if user_id:
                cart = Cart.objects.get(user=user_id)
                # CartItem.objects.filter(cart__cart_id=session_cart_id).update(cart=cart.id)
            else:
                cart = Cart.objects.get(cart_id=session_cart_id)
        except Cart.DoesNotExist:
            # Insert data to DB
            if user_id:
                cart = Cart.objects.create(
                    cart_id=session_cart_id,
                    user=User(id=user_id)
                )
            else:
                cart = Cart.objects.create(
                    cart_id=session_cart_id,
                )
        try:
            # Try to check if item is in cart and rise quantity
            cart_item = CartItem.objects.get(
                product=product, cart=cart, item_size=size)
            cart_item.quantity += get_item_qnty
        except CartItem.DoesNotExist:
            # Insert item to DB
            cart_item = CartItem.objects.create(
                product=product,
                quantity=get_item_qnty,
                cart=cart,
                item_size=size
            )
    return redirect('cart_details')


def remove_one_cart(request, item_id):
    """
    Remove one from cart with button
    """
    item = get_object_or_404(CartItem, id=item_id)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart_details')


def increase_one_cart(request, item_id):
    """
    Increase one from cart with button
    """
    item = get_object_or_404(CartItem, id=item_id)
    item.quantity += 1
    item.save()
    return redirect('cart_details')


def delete_from_cart(request, item_id):
    """
    Delete item from cart with button
    """
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart_details')


def cart_details(request, total=0, counter=0, cart_items=None):
    """
    Render cart page
    Check all items in cart, count qnty and total-price
    """
    user_id = _get_user_or_none(request)
    session_cart_id = _cart_id(request)
    try:
        if user_id:
            cart = Cart.objects.get(user=user_id)
        else:
            cart = Cart.objects.get(cart_id=session_cart_id)
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for item in cart_items:
            # Check item stock quantity if clothing check size and related stock quantity
            qnty = item.quantity
            if item.item_size:
                size = item.item_size.size
                if size == 'XS':
                    product_stock = item.product.stock_xs
                elif size == 'S':
                    product_stock = item.product.stock_s
                elif size == 'M':
                    product_stock = item.product.stock_m
                elif size == 'L':
                    product_stock = item.product.stock_l
                elif size == 'XL':
                    product_stock = item.product.stock_xl
                elif size == 'XXL':
                    product_stock = item.product.stock_xxl
                elif size == 'XXXL':
                    product_stock = item.product.stock_xxxl
                else:
                    product_stock = item.product.stock
                if qnty > product_stock:
                    item.quantity = product_stock
                    qnty = product_stock
                    item.save()
                    messages.error(
                        request, f'We have only {product_stock} {item.product.name} in stock. Sorry.')
            else:
                product_stock = item.product.stock
                if qnty > product_stock:
                    item.quantity = item.product.stock
                    qnty = product_stock
                    item.save()
                    messages.error(
                        request, f'We have only {product_stock} {item.product.name} in stock. Sorry.')
            total += (item.product.price * qnty)
            counter += qnty
    except ObjectDoesNotExist:
        pass
    # Stripe api settings
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total * 100)
    description = 'DOT GEEK Shop - New Order'
    data_key = settings.STRIPE_PUBLISHABLE_KEY

    if request.method == 'POST':
        # If stripe-pay, get user data from stripe form
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            billing_name = request.POST['stripeBillingName']
            billing_address1 = request.POST['stripeBillingAddressLine1']
            billing_city = request.POST['stripeBillingAddressCity']
            billing_postcode = request.POST['stripeBillingAddressZip']
            billing_country = request.POST['stripeBillingAddressCountryCode']
            shipping_name = request.POST['stripeBillingName']
            shipping_address1 = request.POST['stripeShippingAddressLine1']
            shipping_city = request.POST['stripeShippingAddressCity']
            shipping_postcode = request.POST['stripeShippingAddressZip']
            shipping_country = request.POST['stripeShippingAddressCountryCode']
            customer = stripe.Customer.create(
                email=email,
                source=token
            )
            charge = stripe.Charge.create(
                amount=stripe_total,
                currency="gbp",
                description=description,
                customer=customer.id
            )
            # Create the order
            try:
                order_details = Order.objects.create(
                    token=token,
                    total=total,
                    email_address=email,
                    billing_name=billing_name,
                    billing_address1=billing_address1,
                    billing_city=billing_city,
                    billing_postcode=billing_postcode,
                    billing_country=billing_country,
                    shipping_name=shipping_name,
                    shipping_address1=shipping_address1,
                    shipping_city=shipping_city,
                    shipping_postcode=shipping_postcode,
                    shipping_country=shipping_country,
                )
                if user_id:
                    order_details.user = User(id=user_id)
                    order_details.save()
                for item in cart_items:
                    OrderItem.objects.create(
                        product=item.product.name,
                        quantity=item.quantity,
                        price=item.product.price,
                        order=order_details,
                        item_size=item.item_size
                    )
                    # Deducate product qnty from stock
                    product = Product.objects.get(id=item.product.id)
                    product.stock = int(product_stock - item.quantity)
                    product.buys = int(product.buys + item.quantity)
                    product.save()
                    item.delete()
                    request.session['thankyou'] = order_details.id
                    send_order_email(order_details.id)
                return redirect('thankyou')
            except ObjectDoesNotExist:
                pass
        except stripe.error.CardError as e:
            # Stripe card error
            return False, e

    context = {
        'cart_items': cart_items,
        'total': total,
        'counter': counter,
        'data_key': data_key,
        'stripe_total': stripe_total,
        'description': description
    }
    return render(request, 'cart/cart.html', context)

def send_order_email(order_id):
    """
    Send order template email to customer
    """
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    if order is not None:
        subject = "DOT GEEK Store - Your order #{}".format(order.id)
        email_to = ['{}'.format(order.email_address)]
        from_email = 'dotgeekstore@gmail.com'
        context = {
            'order': order,
            'order_items': order_items,
        }
        email = get_template('emails/email_order.html').render(context)
        msg = EmailMessage(subject, email, to=email_to, from_email=from_email)
        msg.content_subtype = 'html'
        msg.send()
