from django.shortcuts import render, get_list_or_404

from .models import OrderItem

def order(request, order_id):
    """
    Render order page with order items
    """
    get_order_items = get_list_or_404(OrderItem, order=order_id)

    context = {
        'get_order_items': get_order_items,
        'order_number': order_id
    }

    return render(request, 'order/order.html', context)


def thankyou(request):
    """
    Render thank you page with order number,
    after transaction is made.
    """
    order_id = request.session['thankyou']

    context = {
        'order': order_id,
    }
    return render(request, 'pages/thankyou.html', context)
