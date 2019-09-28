from django.shortcuts import render
from django.http import HttpResponse


def display_checkout(request):
    return render(request, 'payment/index.html')

# def process_payment(request):
#     order_id = request.session.get('order.id')
#     order = get_object_or_404(Order, id=order_id)
#     host = request.get_host()
#
#     paypal_dict = {
#         'business': settings.PAYPAL_RECEIVER_EMAIL,
#         'amount': '%.2f' % order.total_cost().quantize(
#             Decimal('.01')),
#         'item_name': 'Order {}'.format(order.id),
#         'invoice': str(order.id),
#         'currency_code': 'USD',
#         'notify_url': 'http://{}{}'.format(host,
#                                            reverse('paypal-ipn')),
#         'return_url': 'http://{}{}'.format(host,
#                                            reverse('payment_done')),
#         'cancel_return': 'http://{}{}'.format(host,
#                                               reverse('payment_cancelled')),
#     }
#
#     form = PayPalPaymentsForm(initial=paypal_dict)
#     return render(request, 'ecommerce_app/process_payment.html', {'order': order, 'form': form})
