from django.shortcuts import render, get_list_or_404

from .models import Order, OrderItem

def order(request, order_id):

    get_order_items = get_list_or_404(OrderItem, order=order_id)

    context = {
        'get_order_items': get_order_items,
        'order_number': order_id
    }

    return render(request, 'order/order.html', context)


def thankyou(request):
    order_id = request.session['thankyou']

    context = {
        'order': order_id,
    }
    return render(request, 'pages/thankyou.html', context)
