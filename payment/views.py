from django.shortcuts import render
from django.conf import settings
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse
import stripe
from django.shortcuts import get_object_or_404
from products.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = 'payment/success.html'


class CancelView(TemplateView):
    template_name = 'payment/cancel.html'


class ItemLandingPageView(TemplateView):
    template_name = 'payment/index.html'

    def get_context_data(self, **kwargs):
        item_id = kwargs['pk']
        item = get_object_or_404(Item, pk=item_id)
        context = super(ItemLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "item": item,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        item_id = self.kwargs['pk']
        item = get_object_or_404(Item, pk=item_id)
        YOUR_DOMAIN = 'http://0.0.0.0'
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data':{
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data':{
                            'name': item.name,
                            #'imates': []
                        },
                    },
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
            automatic_tax={'enabled': False},
        )
        return JsonResponse({
            'id': checkout_session.id
        })
